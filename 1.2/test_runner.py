#!/usr/bin/env python
# $Id: test_runner.py 2151 2009-09-24 13:05:43Z lsc $
# 
# Copyright (c) 2009 STFC Rutherford Appleton Laboratory 
# Author: Lee-Shawn Chin 
# Date  : June 2009
#
# NOTE: This is a proof-of-concept implementation. It was not designed for
#       production use but merely to explore what is possible
#       Use at your own risk ;)
#

import os
import re
import sys
from subprocess import call
from flamedb import db
from xmmlreader import agentdata

# for now, hardcode all input file paths
outfile   = "generated_tests.py"
#dbfile    = "/home/rzk76414/Desktop/iters.db"
#xmmlfile  = "/home/rzk76414/docs/eclipse/eurace/EURACE_Model/branches/Integrated_Model/eurace_model.xml"
#rulesfile = "./test.rules"

# get input arguments
if len(sys.argv) != 4:
    print >>sys.stderr, "Usage: %s <db_file> <xmml_file> <rules_file>" % sys.argv[0]
    sys.exit(0)
dbfile = sys.argv[1]
xmmlfile = sys.argv[2]
rulesfile = sys.argv[3]
    
coloured_text = True
if "SIMVAL_DISABLE_COLOUR" in os.environ.keys():
    if os.environ["SIMVAL_DISABLE_COLOUR"] == "1": coloured_text = False
    
# ASCII text colour info
if coloured_text:
    C_RED   = "\\033[1;31m"
    C_BOLD   = "\\033[1m"
    C_GREEN = "\\033[1;32m"
    C_END   = "\\033[0m"
else:
    C_RED   = ""
    C_BOLD  = ""
    C_GREEN = ""
    C_END   = ""
STR_OK   = "%sOK%s" % (C_GREEN, C_END)
STR_FAIL = "%sFAIL%s" % (C_RED, C_END)

def error(mesg):
    print >>sys.stderr, ">>>>> (Error): %s" % mesg
    sys.exit(1)

def warn(mesg):
    print >>sys.stderr, ">> (Warning): %s" % mesg
    
def ensure_file_exists(fname):
    try: 
        file = open(fname, "r")
    except:
        error("Could not open file: %s" % fname)
    file.close()
    
# check files exists
ensure_file_exists(dbfile)
ensure_file_exists(xmmlfile)
ensure_file_exists(rulesfile)

# parse rules
try: 
    file = open(rulesfile, "r")
except:
    error("Count not read file: %s" % file);

print " * Parsing rules file ... "
# parse rules file
content = {}
stage = None
header_delim = "::"
acceptable_stages = ["VARIABLES", "CONSTANTS", "RULES"]
acceptable_varname = "[a-zA-Z_][a-zA-Z0-9_]*"
for line in file.readlines():
    line = line.strip() # remove trailing and leading spaces
    if "#" in line: line = line[:line.index("#")] # remove comments
    if not line: continue # ignore empty lines
    
    if line[:len(header_delim)] == header_delim:
        line = line[len(header_delim):]
        if line in acceptable_stages: 
            stage = line
            content[stage] = []
            continue
        else:
            error("Unknown header found - %s%s" % (header_delim, line))
    
    if not stage:
        warn("Ignoring line : %s" % line)
        continue
    
    content[stage].append(line)        
file.close()

# load db and agent data
print " * Loading model definition ... "
model = agentdata(xmmlfile)
print " * Loading result data ... "
data  = db(dbfile, model)


print " * Translating variables ... "
# process variables
maxvlen = 0
sums = {}
re_variable = re.compile("(%s)\s*=\s*([^\s]+)" % acceptable_varname)
re_stmt     = re.compile("(%s)\((.*)\)" % acceptable_varname)
for line in content["VARIABLES"]:
    match = re_variable.match(line)
    if not match: error("(variable) Invalid format: %s" % line)
    varname = match.group(1)
    stmt    = match.group(2)
    match = re_stmt.match(stmt)
    if not match: error("(variable) Invalid statement format: %s" % line)
    aname = match.group(1)
    vname = match.group(2)
    if not model.is_usable_agent_var(aname, vname): error(" \"%s\" " % line)

    #sums[varname] = data.get_sum_per_iteration(aname, vname)
    sums[varname] = (aname, vname)
    maxvlen = max(len(varname), maxvlen)

print " * Translating constants ... "
# process constants
constants = {}
re_constant = re.compile("(%s)\s*=\s*([0-9.\-]+)" % acceptable_varname)
for line in content["CONSTANTS"]:
    match = re_constant.match(line)
    if not match: error("(constant) Invalid format: %s" % line)
    constants[match.group(1)] = float(match.group(2))
    
print " * Translating rules ... "
# order is important. define longer patterns first
pyfuncs = ["abs", "min", "max", "pow", "round"] # supported python functions
eval_ops = ["==", ">=", "<=", "<", ">", "!="]
math_ops = ["(", "+", "-", "*", "/", "%", ")"]
ops = []
ops.extend(eval_ops)
ops.extend(math_ops)

rules = []
for line in content["RULES"]:
    has_eval = False
    rule = []
    vars = []
    lhs  = []
    rhs  = []
    eop = ""
    # make sure ops are seen as one token
    for op in ops: line = line.replace(op, " %s "%op)
    
    side = lhs
    tokens = line.split()
    i = -1
    for t in tokens:
        t = t.strip()
        i += 1
        
        # skip empty tokens
        if not t: continue
        
        # evaluation operator
        if t in eval_ops:
            if has_eval:
                error("Each rule should contain only one evaluation operator : %s" % line)
            else:
                has_eval = True
            rule.append(t)
            eop = t
            side = rhs # switch to right hand side
            continue
        
        if t in math_ops:
            rule.append(t)
            side.append(t)
            continue
        
        # python functions
        if t in pyfuncs:
            if i < len(tokens):
                if tokens[i+1] == "(":
                    rule.append(t)
                    side.append(t)
                    continue
                
        # replace variables
        if t in sums.keys():
            string = "sums['%s'][i]" % t
            vars.append((t, string))
            rule.append(string)
            side.append(string)
            continue
        
        # replace constants
        if t in constants.keys():
            rule.append("%f" % constants[t])
            side.append("%f" % constants[t])
            continue
        
        
        # this should not be reached
        error("Unknown token (%s) in rule: %s"% (t, line))
        
    if not has_eval: error("rule does not contain an evaluation operator: \n *** %s" % line)
    rules.append((line, " ".join(rule), vars, " ".join(lhs), " ".join(rhs), eop  ))

print " * Generating test code ... "
# write test code
try:
    file = open(outfile, "w")
except:
    error("Could not open file for writing: %s" % outfile)

file.write("#!/usr/bin/env python\n")
file.write("# This file was generated using %s\n" % sys.argv[0])
file.write("""
# import libs
import sys
import math
from flamedb import db
from xmmlreader import agentdata

# load model data
model = agentdata("%s")
# load database
data  = db("%s", model)

C_RED   = "%s"
C_GREEN = "%s"
C_END   = "%s"

def print_equation_evaluation(lhs, rhs, op, passed):
    global C_RED, C_GREEN, C_END
    
    OP_INVERSE = {}
    OP_INVERSE["=="] = "!="
    OP_INVERSE["!="] = "=="
    OP_INVERSE["<"]  = ">="
    OP_INVERSE[">"]  = "<="
    OP_INVERSE["<="] = ">"
    OP_INVERSE[">="] = "<"
    
    if passed: C_START = C_GREEN
    else: C_START = C_RED
    
    L = float(lhs)
    R = float(rhs)
    S = L + R
    LP = "%%.4f%%%%" %% (abs(L / S) * 100)
    RP = "%%.4f%%%%" %% (abs(R / S) * 100)
    
    if not passed: op = OP_INVERSE[op]
    
    print "                     LHS                         RHS"
    print "    ----------------------------------------------------"
    print "    %%20s      %%s%%s%%s %%20s" %% (lhs, C_START, op, C_END, rhs)
    print "                %%8s                     %%8s   " %% (LP, RP)
    print "    ----------------------------------------------------"
failed = 0
total  = %d
sums = {}
# user generated variables
""" % (xmmlfile, dbfile, C_RED, C_GREEN, C_END, len(rules)))

for var in sums.keys():
    aname,vname = sums[var]
    file.write("sums[\"%s\"] = data.get_sum_per_iteration(\"%s\",\"%s\")\n" % (var,aname,vname))

i = 0
rcount = len(rules)
for rule,rulestr,vars,lhs,rhs,eop in rules:
    i += 1
    file.write("""

def test_rule_%d_of_%d():
    global failed
    success = True
    print ""    
    print " %%s" %% ("."*76)
    print ""
    print "RULE %d : %s%s%s"
    for i in data.get_list_of_iterations():
        print ""
        print ""
        print "              ---- [ Iteration %%d : " %% i,
        if %s: 
            print "%s ] ----"
        else:
            success = False
            print "%s ] ----"
        lhs = eval("%s")
        rhs = eval("%s")
        print ""
        print_equation_evaluation(lhs, rhs, "%s", success)
        print ""
""" % (i, rcount, i, C_BOLD, rule, C_END, rulestr, STR_OK, STR_FAIL, lhs, rhs, eop))
    for v,vs in vars: file.write("""
        maxintlen = 10
        vv = eval("%s")
        
        # if negative value, make vvv positive and remove one space to make 
        #  way for -ve sign
        if vv < 0: vvv = vv / -10.0
        elif vv == 0: vvv = 1
        else: vvv = vv
        
        digits_before_dot = int(math.log10(vvv)) + 1
        if digits_before_dot < 1: digits_before_dot = 1
        spacer = maxintlen -  digits_before_dot
        
        print "    %s%s = %%s%%f" %% ((" " * spacer),vv)""" % (vs, v, " "*(maxvlen - len(v))))
    
    file.write("""
    if not success: failed += 1
""")
    
file.write("""
# run tests
print " * Running tests ..."
""")

for i in xrange(rcount):
    file.write("test_rule_%d_of_%d()\n" % (i+1, rcount))
    
file.write("""

print ""
print ""
print " %s " % ("="*76)
print "  SUMMARY: %d rules tested, %d failed" % (total, failed)
print " %s " % ("="*76)

if failed == 0: sys.exit(0)
else: sys.exit(failed)
""")
file.close()

cmd = "python %s" % outfile
try:
    retcode = call(cmd, shell=True)
    sys.exit(retcode * 11)
except OSError, e:
    print >>sys.stderr, "Execution failed:", e
    sys.exit(1)

