#!/bin/bash
#Script to run test_runner.py
#Usage: 
#python test_runner.py <db_file> <xmml_file> <rules_file>
#output files: generated_tests.py stdout.txt

#Script to convert results to html
#python results2html.py <infile.txt> <rules.txt> <modelurl> <revision> <modelname>
#infile.txt: stdout.txt from test_runner.py

#Use this line to toggle colour output
export SIMVAL_DISABLE_COLOUR=1  #for output to file
#unset SIMVAL_DISABLE_COLOUR 	#for colour output to display

#DB_DIR='/media/DOCS/Docs/EURACE/X-models/SVN_linux/xagents/sim_validation/iters'
#RULESFILE='/media/DOCS/Docs/EURACE/X-models/SVN_linux/xagents/sim_validation/eurace.rules'

#DB location:
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/no_data_input/db/allvars_everyits/v2'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/no_data_input/db/selectvars_everyits'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/no_data_input/db/allvars_every20'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/no_data_input/db/selectvars_every20/v2'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/no_data_input/db/selectvars_every20/v3'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/no_data_input/db/allvars_everyits/v3'
XML_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/no_data_input/db/allvars_everyits/v4/validation'
DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/no_data_input/db/allvars_everyits/v4'

#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_1600/db/allvars_everyits/v1'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_1600/db/selectvars_everyits/v1'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_1600/db/allvars_every20/v1'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_1600/db/selectvars_every20/v1'

#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_16K/db/allvars_everyits/v1'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_16K/db/allvars_every20/v1'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_16K/db/selectvars_everyits/v1'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_16K/db/selectvars_every20/v1'

#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_160K/db/allvars_everyits/v1'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_160K/db/allvars_every20/v1'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_160K/db/selectvars_everyits/v1'
#DB_DIR='/media/sander/DataStorage-2/Housing_Market_Dataset/sandbox/validation/results/data_input_160K/db/selectvars_every20/v1'


#Housing Model:
#For gendb
XMMLFILE='/media/sander/DataStorage1/GIT/GitLab/ABM@ECB/ABM_at_ECB/code/Financial_Fragility_Network_Model_2.0/eurace_model.xml'

#For xml2hdf5
#XMMLDIR='/media/sander/DataStorage1/GIT/GitLab/ABM@ECB/ABM_at_ECB/code/Financial_Fragility_Network_Model_2.0'
#XMMLFILE='eurace_model.xml'

#Rules: default eurace
RULESFILE_1='/media/sander/DataStorage1/GIT/GitLab/ABM@ECB/ABM_at_ECB/code/utils/sim_validation_rules/rules/xeurace.rules'
#Rules: housing market
RULESFILE_2='/media/sander/DataStorage1/GIT/GitLab/ABM@ECB/ABM_at_ECB/code/utils/sim_validation_rules/rules/housing.rules'

URL='https://gitlab.ub.uni-bielefeld.de/hoog/ABM_at_ECB/tree/master/code/Financial_Fragility_Network_Model_2.0'
REV='29 Sept 2016'
MODEL='Financial Fragility Network Housing Model'

#Generate DB
#python gendb.py $XMMLFILE $XML_DIR

#Create and Run tests
python test_runner.py $DB_DIR/set_1_run_1_iters.db $XMMLFILE $RULESFILE_1 
#python test_runner.py $DB_DIR/set_1_run_1_iters.db $XMMLFILE $RULESFILE_1 >stdout.txt 2>stderr.txt
#python test_runner.py $DB_DIR/set_1_run_1_iters.db $XMMLFILE $RULESFILE_2 >stdout.txt 2>stderr.txt

#Run tests explicitly
python generated_tests.py >output.txt

#Convert results to html
#results2html.py <infile.txt> <rules.txt> <modelurl> <revision> <modelname>
#infile.txt: stdout.txt
#python results2html.py stdout.txt ${RULESFILE_1} $URL $REV $MODEL

#Default
python results2html.py output.txt ${RULESFILE_1} "url" "rev" "model name"

#Copy results to DB folder:
mv out.html output.txt stdout.txt stderr.txt $DB_DIR

echo 'Done checking validation rules.'
