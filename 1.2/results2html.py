#!/usr/bin/env python
# $Id: results2html.py 2156 2009-09-25 14:02:46Z lsc $
# 
# Copyright (c) 2009 STFC Rutherford Appleton Laboratory 
# Author: Lee-Shawn Chin 
# Date  : Sept 2009
#
# NOTE: Another quick hack to convert output of test_runner to HTML 
#       so that the latest validation run can be exported by buildbot
#

import re
import os
import sys
from time import strftime

DATE = strftime("%d/%m/%Y %H:%M:%S")

# get input arguments
if len(sys.argv) != 6:
    print >>sys.stderr, "Usage: %s <infile.txt> <rules.txt> <modelurl> <revision> <modelname>" % sys.argv[0]
    sys.exit(0)
infilename = sys.argv[1]
rulesfilename  = sys.argv[2]
MODELURL   = sys.argv[3]
REVISION   = sys.argv[4]
MODELNAME  = sys.argv[5]

outfilename = "out.html"

def error(mesg):
    print >>sys.stderr, ">>>>> (Error): %s" % mesg
    sys.exit(1)

def warn(mesg):
    print >>sys.stderr, ">> (Warning): %s" % mesg

varmap = {}
def markup_rule(rule):
    global varmap
    out = []
    ops = ["==", ">=", "<=", "<", ">", "!=", "(", "+", "-", "*", "/", "%", ")"]
    
    for op in ops: rule = rule.replace(op, " %s "%op)
    for word in rule.split():
        if word in varmap.keys():
            tip = varmap[word].replace("(", "(&nbsp;").replace(")", "&nbsp;)")
            out.append("<a class='tip' href='#'>%s<span>%s</span></a>" % (word, tip))
        else:
            out.append("<span class='op'>%s</span>"%word)
    return " ".join(out)

re_rule = re.compile("RULE (\d+) : (.+)$")
re_iter = re.compile("\s*---- \[ Iteration (\d+) :  (OK|FAIL) ] ----\s*")

header = """
<html>
    <head>
        <title>Validation results for %s (rev %s)</title>
        <style type="text/css">
        
        * {
            font-family: sans-serif, Cursor;
            font-size: 12px;
            font-weight: normal;
        }
        
        a:link,a:visited,a:active {
            font-weight: bold;
            color: #555555;
        }
        
        a:hover {
            font-weight: bold;
            color: blue;
        }
        
        h1 {
            text-decoration: underline;
            font-weight: bold;
        }
        
        h2 {
            font-weight: bold;
        }
        
        .table {
            border-spacing: 2px;
        }
        
        th {
            background: #369;
            padding: 5px 1px;
        
            color: #ffffff;
            font-weight: bold;
            font-size: 14px;
            border-bottom: 3px solid #444;
        }
        
        .content {
            background: #ddd;
            padding: 20px 30px;
        }
        
        .footer {
            color: #369;
            text-align: center;
            font-size: 9px;
            border-bottom: 1px solid #666;
            border-top: 1px solid #666;
        }

        .breakdown_ok
        {
            display: none;
            background-color: #fff;
            border-color: green;
            border-style: solid;
            border-width: thin;
        }
        
        .breakdown_nook
        {
            display: none;
            background-color: #fff;
            border-color: red;
            border-style: solid;
            border-width: thin;
        }
        
        a.rule_ok
        {
            font-weight: bold;
            color: green;
            cursor: pointer;
        }
        
        a.rule_nook
        {
            font-weight: bold;
            color: red;
            cursor: pointer;
        }
        
        .op {font-family:courier, "courier new", monospace;}
        pre {font-family:courier, "courier new", monospace;}
        
        a.tip {
            position: relative;
            font-weight: bold;
            color: navy;
            cursor: help;
            text-decoration: none;
        }
        
        a.tip:hover {
            background-color: yellow; 
        }
        
        a.tip span {display:none}
        a.tip:hover span {
            display: block;
            position: absolute;
            top:2em; left:0em;
            padding: 5px 5px 5px 5px;
            border: 1px solid #000000;
            background-color: beige;
        }
    
        </style>
        
        <script type="text/javascript">
        <!--
        function toggle(id) {
            var e = document.getElementById(id);
            if(e.style.display == 'block')
                e.style.display = 'none';
            else
                e.style.display = 'block';
            return false;
        }
        //-->
        </script>

    </head>
    <body>
        
        Generated on %s<br />
        SVN URL : <a href="%s">%s</a><br /><br />
        
        <table>
            <tr><th>%s (rev %s)</th></tr>
            <tr><td class="content">
            

            
""" % (MODELNAME, REVISION, DATE, MODELURL, MODELURL, MODELNAME, REVISION )

footer = """
            </td></tr>
            <tr><td class="footer">
                Software Engineering Group, Computational Science and Engineering Department<br />
                For more info, contact Shawn Chin (shawn.chin@rem0veMe.stfc.ac.uk)
            </td></tr>
        </table>

    </body>
</html>
"""

try:
    file = open(rulesfilename, "r")
except:
    error("could not open file %s for reading" % rulesfilename)

line = ""
acceptable_varname = "[a-zA-Z_][a-zA-Z0-9_]*"
re_leqr  = re.compile("(%s)\s*=\s*(%s\(.*\))" % (acceptable_varname, acceptable_varname))
re_const = re.compile("(%s)\s*=\s*([0-9.\-]+)" % acceptable_varname)
while line != "::VARIABLES": line = file.readline().strip()

line = file.readline()
while line:
    L = line.strip();
    if L == "::CONSTANTS": break
    line = file.readline()
    
    if "#" in L: L = L[:L.index("#")] # remove comments
    if not L: continue # ignore empty lines
    
    match = re_leqr.match(L)
    if not match: warn("Unknown VAR line - %s" % L)
    else: varmap[match.group(1)] = match.group(2)

line = file.readline()
while line:
    L = line.strip();
    if L == "::RULES": break
    line = file.readline()
    
    if "#" in L: L = L[:L.index("#")] # remove comments
    if not L: continue # ignore empty lines
    
    match = re_const.match(L)
    if not match: warn("Unknown CONST line - %s" % L)
    else: varmap[match.group(1)] = match.group(2)
    
file.close()

try:
    file = open(infilename, "r")
except:
    error("could not open file %s for reading" % infilename)

try:
    ofile = open(outfilename, "w")
except:
    error("could not open file %s for writing" % outfilename)

rules = []

line = file.readline()
rule = None
iter = None
while line[:4] != "RULE": line = file.readline()

while line:
    L = line[:-1]
    line = file.readline()
    if not L: continue
    if L[:12] == " ===========": break
    if L[:12] == " ...........": continue
    
    if L[:4] == "RULE":
        match = re_rule.match(L)
        if not match: raise Exception, "Invalid string found - %s" % L
        
        newrule = {} # new rule
        newrule["rule"] = match.group(2)
        newrule["num"] = int(match.group(1))
        newrule["iters"] = []
        rules.append(newrule) # add to list
        rule = newrule # get ref for convenience
        continue
    
    if L.strip()[:16] == "---- [ Iteration":
        match = re_iter.match(L)
        if not match: raise Exception, "Invalid string found - %s" % L
        
        newiter = {}
        newiter["num"] = int(match.group(1))
        newiter["state"] = match.group(2)
        newiter["content"] = []
        
        rule["iters"].append(newiter)
        iter = newiter
        continue
    
    iter["content"].append(L)

file.close()

i = 0
ofile.write(header)
for R in rules:
    ofile.write("<h2>RULE %d : %s</h2>\n" % (R["num"], markup_rule(R["rule"])))
    ofile.write("<ul>\n")
    for I in R["iters"]:
        i = i + 1
        id = "content_%d" % i
        if I["state"] == "OK": suffix = "ok"
        else: suffix = "nook"
             
        ofile.write("<li>")
        ofile.write("<a class='rule_%s' onclick='toggle(\"%s\")'>" % (suffix, id))
        
        ofile.write("Iteration %d : %s" % (I["num"], I["state"]))
        ofile.write("</a></li>\n")

        ofile.write("<div class='breakdown_%s' id='%s'><pre>\n" % (suffix, id))
        ofile.write("\n".join(I["content"]))
        ofile.write("\n</pre></div>\n")
        
    ofile.write("</ul>\n")
ofile.write(footer)
ofile.close()
