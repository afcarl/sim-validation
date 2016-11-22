Readme file for Simulation validation tool
(Sander van der Hoog, 29.9.2016)

Copyright (C) Shawn-Lee Chin

This is version 2 of the toole that has some adjustments wrt. the original code from Shawn-Lee Chin.

Modified files:

xmmlreader.py
test_runner.py

When reading XML models, the original scripts could not read nested models 2 levels deep. 
The solution was to only once set the root path to the main model.xml file, whereas in the original the path was updated with each new model.xml file found in the hierarchy.
Since the nested models are referenced using hard paths to the model.xml files, this produced an error.