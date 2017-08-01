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
rungms_path="misc/automation/rungms"

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
      print(l_box_small("Skipping input file"),file_progress(filenum,len(input_file_paths)),input_file_path)
      continue

  try:
    run_command=rungms_path+" "+input_file_path+" 00 "+run_arguments["ncpus"]+" "+run_arguments["ncpus"]+ " > "+input_file_path.replace(".inp",".log")+" 2>&1"
    print(l_box_small("Running input file"),file_progress(filenum,len(input_file_paths)),input_file_path)
    os.system(run_command)
  except:
    sys.exit(1)
