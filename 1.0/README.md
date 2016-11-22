Simulation validation tool

See files test.rules in version folders for more information.

Copyright (c) 2009 STFC Rutherford Appleton Laboratory 
Author: Lee-Shawn Chin 
Date  : June 2009

This is a simulation validation tool to test invariant relationships between agent memory variables, aggregated across all agents of a certain type.
The current implementation only works for simple, scalar agent memory variables (no array indexes or ADT attribtues, nor any nested xml models).

Features:
The HTML output can be included into a Build-Bot that is automatically checking out a FLAME model from SVN or GIT repository, and running the validation tool only if a new commit has been detected.

Inputs:
- a rules file (see test.rules)
- simulation output XML files

Outputs:
- SQL database file iters.db with values extracted from XML output files (created using gendb.py script)
- plain text file with validation results (output.txt)
- HTML file with validation results (out.html)

HTML output:
- Output is shown per validation rule.
- For each iteration present in the XML output files, the result of the validation test is shown given the precision that is set in the rules file.
