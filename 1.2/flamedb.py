#!/usr/bin/env python
# $Id: flamedb.py 2006 2009-07-31 14:22:56Z lsc $
# 
# Copyright (c) 2009 STFC Rutherford Appleton Laboratory 
# Author: Lee-Shawn Chin 
# Date  : June 2009
#
# NOTE: This is a proof-of-concept implementation. It was not designed for
#       production use but merely to explore what is possible
#       Use at your own risk ;)
#

import sqlite3
import sys
import re

# If builtin "set" datatype not available (pre Python2.3) load the sets module
try: dummy = set()
except NameError: from sets import Set as set

def error(mesg):
    print >>sys.stderr, ">>>>> (Error): %s" % mesg
    sys.exit(1)
def info(mesg):
    print ">> (Info): %s" % mesg
def ensure_file_exists(fname):
    try: 
        file = open(fname, "r")
    except:
        error("Could not open file: %s" % fname)
    file.close()    

class db:
    
    def __init__(self, dbfile, modeldata):
        
        ensure_file_exists(dbfile)
        self.conn   = sqlite3.connect(dbfile)
        self.cursor = self.conn.cursor()
        self.model  = modeldata
        self._get_iterlist()
        
    def _get_iterlist(self):
        
        # Assume Eurostat always printed
        # Should instead get expGUI to have table with list of iters?
        
        query = "SELECT _ITERATION_NO FROM Eurostat"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        
        iter_set = set() # use set() to remove duplicates
        for row in rows: iter_set.add(row[0])
        
        self.iters = list(iter_set) # store as list
        self.iters.sort()
        
    def get_list_of_iterations(self):
        return self.iters
    
    def get_sum_per_iteration(self, agent_name, var_name):
        
        if not self.model.is_valid_agent(agent_name):
            error("%s is not a valid agent name" % agent_name)
        
        if not self.model.is_usable_agent_var(agent_name, var_name):
            error("%s is not a usable agent variable" % var_name)
        
        out = {} # return as dict of values
        
        if "." in var_name:
            v = var_name.split(".")
            if len(v) != 2: error("We do not (yet) support nested datatypes : %s" % var_name)
            var_name = v[0]
            mem_name = v[1]
        else:
            mem_name = None    
        
        if var_name[-2:] == "[]": # array
            var_name = var_name[:-2]
            
            if mem_name: 
                var_type = self.model.agents[agent_name]["vartype"][var_name+"[]"]
                index = self.model.get_datatype_member_index(var_type, mem_name)
                
            query = "SELECT %s FROM %s WHERE _ITERATION_NO=%d"
                                
            for i in self.iters:
                out[i] = 0.0
                self.cursor.execute(query % (var_name, agent_name, i))
                row = self.cursor.fetchone()
                while row:
                    if not mem_name:
                        line = row[0][1:-1].replace(" ", "") # remove {...} around texts
                        vals = line.split(",")
                        for v in vals: out[i] += float(v.strip())
                    else:
                        line = row[0][2:-2].replace(" ", "") # remove {{...}} around texts
                        vals = line.split("},{")
                        for v in vals:
                            e = v.split(",")
                            out[i] += float(e[index])                  
                    row = self.cursor.fetchone()
        else:
            if not mem_name: # basic int or double
                query = "SELECT SUM(%s) FROM %s WHERE _ITERATION_NO=%d"
                for i in self.iters:
                    try:
                        self.cursor.execute(query % (var_name, agent_name, i))
                    except sqlite3.OperationalError:
                        error("The database does not contain data for %s.%s" % (agent_name, var_name))
                        
                    rows = self.cursor.fetchall()
                    out[i] = float(rows[0][0])

            else: # user-define datatype
                
                query = "SELECT %s FROM %s WHERE _ITERATION_NO=%d"
                var_type = self.model.agents[agent_name]["vartype"][var_name]
                index = self.model.get_datatype_member_index(var_type, mem_name)
                for i in self.iters:
                    out[i] = 0.0
                    self.cursor.execute(query % (var_name, agent_name, i))
                    row = self.cursor.fetchone()
                    while row:
                        line = row[0][1:-1].replace(" ", "") # remove {...} around texts
                        # this line has nested data hidden somewhere within
                        if "{" in line: line = re.sub("{[^}]*}", "{}", line)
                        vals = line.split(",")
                        out[i] += float(vals[index])
                        row = self.cursor.fetchone()
                
        return out
