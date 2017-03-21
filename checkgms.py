#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json
import sys

from checkgms_utils import *
from checkgms_stable import *

run_arguments=parse_arguments()

print(c_box("Run parameters"))
print (json.dumps(run_arguments,indent=2))

#Populate the parser_groups array
parse_groups=[]
parse_groups=get_parse_groups(run_arguments=run_arguments)

#Populate the log_file_paths array
log_file_paths=[]
log_file_paths=get_log_file_paths(folder_string_match=run_arguments["filter_folder"],file_string_match=run_arguments["filter_file"])

#Loop through the log_file_paths array and validate
for filenum, log_file_path in enumerate(log_file_paths,start=1):
  validation_result=checkgms(filenum=filenum,log_file_path=log_file_path,log_file_count=len(log_file_paths),run_arguments=run_arguments,parse_groups=parse_groups)

  if run_arguments["exit_on_fail"]:
    if validation_result == "fail":
      sys.exit(1)
