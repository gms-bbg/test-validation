#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json
import sys
import os

import mmap

from checkgms_utils import *
from checkgms_stable import *

run_arguments=parse_arguments(validation=False)
ppn=6

print(c_box("Run parameters"))
print (json.dumps(run_arguments,indent=2))

script_path = os.path.dirname(os.path.realpath(__file__))

#Populate the log_file_paths array
input_file_paths=[]
input_file_paths=get_input_file_paths(folder_string_match=run_arguments["filter_folder"],file_string_match=run_arguments["filter_file"],folder_string_skip=run_arguments["skip_folder"],file_string_skip=run_arguments["skip_file"],script_path=script_path)

#Loop through the log_file_paths array and validate
for filenum, input_file_path in enumerate(input_file_paths,start=1):

  #Search for prescence of "TRAVIS-CI SKIP"
  with open(input_file_path,'r',encoding="utf-8",errors='ignore') as opened_file:
    parse_memory_map = mmap.mmap(opened_file.fileno(), 0, access=mmap.ACCESS_READ)
    regex_string="TRAVIS-CI SKIP"
    regex=re.compile(str.encode(regex_string,'ascii'), re.MULTILINE)
    match = regex.search(parse_memory_map)
    #If found then skip
    if match:
     #print(l_box_small("Skipping input file"),file_progress(filenum,len(input_file_paths)),input_file_path)
      continue

    #If --test_type is passed in:
    if "small" in run_arguments["test_type"]:
      regex_string="TRAVIS-CI SMALL"
    elif "medium" in run_arguments["test_type"]:
      regex_string="TRAVIS-CI MEDIUM"
    elif "large" in run_arguments["test_type"]:
      regex_string="TRAVIS-CI LARGE"

    if len(run_arguments["test_type"]) > 0:
      regex=re.compile(str.encode(regex_string,'ascii'), re.MULTILINE)
      match = regex.search(parse_memory_map)
      if not match:
       #print(l_box_small("Skipping input file"),file_progress(filenum,len(input_file_paths)),input_file_path)
        continue


  try:
    if (int(run_arguments["ncpus"]) <= ppn):
      job_submission_command="sarom-gms"+" "+input_file_path+" -l "+input_file_path.replace(".inp",run_arguments["output_extension"])+" "+"-p "+run_arguments["ncpus"]+" "+"-ppn "+run_arguments["ncpus"]+" "+"-w 240:0:0"
    else:
      job_submission_command="sarom-gms"+" "+input_file_path+" -l "+input_file_path.replace(".inp",run_arguments["output_extension"])+" "+"-p "+run_arguments["ncpus"]+" "+"-ppn "+str(ppn)+" "+"-w 240:0:0"
    print(l_box_small("Submitting job for input file"),file_progress(filenum,len(input_file_paths)),input_file_path)
    print(job_submission_command)
   #os.system(job_submission_command)
  except KeyboardInterrupt:
    sys.exit(1)
  except:
    sys.exit(1)
