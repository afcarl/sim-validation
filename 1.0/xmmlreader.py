#!/usr/bin/env python
# $Id: xmmlreader.py 2006 2009-07-31 14:22:56Z lsc $
# 
# Copyright (c) 2009 STFC Rutherford Appleton Laboratory 
# Author: Lee-Shawn Chin 
# Date  : June 2009
#
# NOTE: This is a proof-of-concept implementation. It was not designed for
#       production use but merely to explore what is possible
#       Use at your own risk ;)
#
import re
import os
import sys
from xml.dom import minidom
from xml.parsers.expat import ExpatError

def error(mesg):
    print >>sys.stderr, ">>>>> (Error): %s" % mesg
    sys.exit(1)
def info(mesg):
    print ">> (Info): %s" % mesg
    
class agentdata:
    
    def __init__(self, filename):
        
        self.datatypes = {}
        self.agents    = {}
        self.basic_datatypes = ["int", "double"]
        # parses xmml file
        self._parse_xmml(filename)
    
    def get_datatype_member_index(self, dt, member):
        if dt not in self.datatypes.keys():
            error("Unknown datatype: %s" % dt)
        try:
            index = self.datatypes[dt]["members"].index(member)
        except ValueError:
            error("Datatype '%s' does not contain member: %s" % (dt, member))
        
        return index
        
    def is_valid_agent(self, agent_name):
        if agent_name in self.agents.keys(): return True
        else: return False
    
    def is_usable_agent_var(self, agent_name, var_name):
        if not self.is_valid_agent(agent_name): 
            error("Invalid agent type: %s" % agent_name)
        
        if "." not in var_name:
            if var_name in self.agents[agent_name]["variables"]:
                var_type = self.agents[agent_name]["vartype"][var_name]
                
                # only basic datatypes can be used
                if var_type not in self.basic_datatypes:
                    info("%s is not a basic type" % var_type)
                    return False
                else:
                    return True
                
            else: 
                info("Unknown agent variable: %s" % var_name)
                return False # unknown agent variable
            
        else:
            var_parts = var_name.split(".")
            if len(var_parts) != 2: 
                error("We do not (yet) support nested datatypes : %s" % var_name)
            
            var_name = var_parts[0] 
            mem_name = var_parts[1]

            try:
                var_type = self.agents[agent_name]["vartype"][var_name]
            except KeyError:
                info("Unknown agent variable: %s" % var_name)
                return False # unknown agent variable
            
            # check if dataype has specific member
            #if not var_type in self.datatypes["members"][var_type]: return False
            # check if it is a basic type
            try:
                mem_type = self.datatypes[var_type]["memtype"][mem_name]
            except KeyError:
                info("datatype %s does not contain member: %s" % var_type, mem_name)
                return False # unknown type
            
            
            if mem_type in self.basic_datatypes: return True
            else: 
                info("%s.%s uses a defined datatype (%s). Only basic types can be used." % (var_name, mem_name, mem_type))
                return False # target var is also a user-defined datatype
            
    def _get_node_text(self, node):
        if len(node.childNodes) != 1 or node.childNodes[0].nodeType != node.TEXT_NODE:
            error("getText() routine used on non-text XML node")
        return node.childNodes[0].data.strip()
    def _parse_xmml(self, filename):
        
        xml_filelist = [filename]
        while len(xml_filelist) > 0:
            filename = xml_filelist.pop()
            dirname = os.path.dirname(filename)
            
            # load xml file
            try:
                dom = minidom.parse(filename)
            except IOError:
                error("Unable to read input file (%s)" % filename)
            except ExpatError:
                error("Invalid XML file (%s)" % filename)
            
            # detect nested models. add to file list.
            nodes = dom.getElementsByTagName("model")
            for node in nodes:
                status = self._get_node_text(node.getElementsByTagName("enabled")[0])
                if status != "true": continue
                
                # look for nested models
                modelfile = self._get_node_text(node.getElementsByTagName("file")[0])
                new_filename = os.path.join(dirname, modelfile) # since path is relative
                #print ("  - Found nested model : %s" % new_filename)
                xml_filelist.append(new_filename)
            del(nodes) # free memory
            
            # Note: we do not yet support nested datatypes!
            # look for datatypes
            dt = dom.getElementsByTagName("dataType")
            for d in dt:
                vars = []
                var_type = {}
                
                dname = self._get_node_text(d.getElementsByTagName("name")[0])
                if dname in self.datatypes.keys(): error("Datatype (%s) redefined" % dname)
                #print "  - Found datatype : %s" % dname
                
                # look for variables in datatype
                elements = d.getElementsByTagName("variable")
                for elem in elements:
                    etype = self._get_node_text(elem.getElementsByTagName("type")[0])
                    ename = self._get_node_text(elem.getElementsByTagName("name")[0])
                    #print ("    + (%s) %s" % (etype, ename))
                    vars.append(ename)
                    var_type[ename] = etype

                new_dt = {}
                new_dt["members"] = vars
                new_dt["memtype"] = var_type
                self.datatypes[dname] = new_dt
            del(dt) # free memory
            
            # look for agents
            agents = dom.getElementsByTagName("xagent")
            for a in agents:
                aname = self._get_node_text(a.getElementsByTagName("name")[0])
                
                #if aname in agent.keys(): # flame supports split definitions of agents
                #    print "  - Found duplicate agent definition (%s). Merging." % aname
                #else: print "  - Found agent : %s" % aname
                vars = []
                var_type = {}
                # determine agent size
                elements = a.getElementsByTagName("variable")
                for elem in elements:
                    etype = self._get_node_text(elem.getElementsByTagName("type")[0])
                    ename = self._get_node_text(elem.getElementsByTagName("name")[0])
                    #print ("    + (%s) %s" % (etype, ename))
                    
                    if etype[-6:] == "_array": # of array type
                        etype = etype[:-6]
                        ename = "%s[]" % ename
                        
                    # get size of this var type
                    if etype not in self.datatypes.keys() and etype not in self.basic_datatypes:
                        error("Unknown datatype (%s) used by %s.%s" % (etype, aname, ename))
                    
                    vars.append(ename)
                    var_type[ename] = etype
                del(elements)
                
                if aname in self.agents.keys(): # merge
                    # TODO: check if there are duplilcate vars
                    self.agents[aname]["variables"].extend(vars)
                    current_types = self.agents[aname]["vartype"].keys()
                    for k in var_type.keys():
                        if k in current_types: 
                            error("Multiple definitions of %s.%s" % (aname,k))
                        self.agents[aname]["vartype"][k] = var_type[k]
                else: # add
                    new_agent = {}
                    new_agent["variables"] = vars
                    new_agent["vartype"]   = var_type
                    self.agents[aname] = new_agent
                    
            # free up memory
            dom.unlink()