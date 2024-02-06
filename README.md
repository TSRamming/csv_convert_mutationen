# csv_convert_mutationen
 Tool for converting Mutationen entries in BZKF study registry import files to another format
 
# how to use this tool
1. Rename your source csv file to "studien.csv" and put it next to csv_convert_mutationen.py
1. Copy MolMarkerMapping.csv.example to MolMarkerMapping.csv and adapt entries in the table to your needs
1. execute csv_convert_mutationen.py with Python
1. you will get a converted csv file named studien_modMolMarker.csv and a log file error.log with all unknown entries in studien.csv
1. add entries to MolMarkerMapping.csv and repeat
