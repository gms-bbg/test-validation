#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json
import sys

from checkgms_utils import *
from checkgms_stable import *

#A way to have log files containing values you wish to reproduce without having the extension .log
file_extension=".SERIAL"
#A way to selectively protect the overwritting of existing validation files when --json_create is passed in
json_protect="protect.json"

run_arguments=parse_arguments()

print(c_box("Run parameters"))
print (json.dumps(run_arguments,indent=2))

#Populate the parser_groups array
parse_groups=[]
parse_groups=get_parse_groups(run_arguments=run_arguments)

#Populate the log_file_paths array
log_file_paths=[]
if run_arguments["json_create"]:
  log_file_paths=get_log_file_paths(folder_string_match=run_arguments["filter_folder"],file_string_match=run_arguments["filter_file"],folder_string_skip=run_arguments["skip_folder"],file_string_skip=run_arguments["skip_file"],file_extension=file_extension)
else:
  log_file_paths=get_log_file_paths(folder_string_match=run_arguments["filter_folder"],file_string_match=run_arguments["filter_file"],folder_string_skip=run_arguments["skip_folder"],file_string_skip=run_arguments["skip_file"])

#Loop through the log_file_paths array and validate
for filenum, log_file_path in enumerate(log_file_paths,start=1):
  if run_arguments["json_create"]:
    validation_result=checkgms(filenum=filenum,log_file_path=log_file_path,log_file_count=len(log_file_paths),run_arguments=run_arguments,parse_groups=parse_groups,file_extension=file_extension,json_protect=json_protect)
  else:
    validation_result=checkgms(filenum=filenum,log_file_path=log_file_path,log_file_count=len(log_file_paths),run_arguments=run_arguments,parse_groups=parse_groups)

  if "skip" in str(validation_result):
    continue

  if run_arguments["exit_on_fail"]:
    if "pass" not in str(validation_result):
      print("Exiting on failure!")
      sys.exit(1)
