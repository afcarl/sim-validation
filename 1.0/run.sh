#!/bin/bash
#Script to run test_runner.py
#Usage: 
#python test_runner.py <db_file> <xmml_file> <rules_file>

#Use this line to toggle colour output
export SIMVAL_DISABLE_COLOUR=1  #for output to file
#unset SIMVAL_DISABLE_COLOUR 	#for colour output to display

#DB_DIR='/media/DOCS/Docs/EURACE/X-models/SVN_linux/xagents/sim_validation/iters'
#RULESFILE='/media/DOCS/Docs/EURACE/X-models/SVN_linux/xagents/sim_validation/eurace.rules'

#Eurace Model:
DB_DIR='/home/svdhoog/files-server/Experiment_isolated_banks/exp7-bank20-gamma24-cash-0.25-debt-0.3-int-0.01/its/alfa/1.0/run_1'
XMMLFILE='/home/svdhoog/files-server/SVN/unibi-svn/tags/Unified_Test_Market_Model_2.0_gsl/eurace_model_rules_dummy.xml'
RULESFILE='//home/svdhoog/files-server/SVN/unibi-svn/tags/Unified_Test_Market_Model_2.0_gsl/xeurace.rules'

#Generate DB
#python gendb.py $XMMLFILE $DB_DIR

#Run tests
python test_runner.py $DB_DIR/iters.db $XMMLFILE $RULESFILE >output.txt

#results2html.py <infile.txt> <rules.txt> <modelurl> <revision> <modelname>
python results2html.py output.txt $RULESFILE "modelurl" "revision" "model"
