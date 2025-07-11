import os
import re
import sys


def parser(regex_string, file_handle, parse_memory_map=None, parse_value_index=0, parse_line_offset=0,
           parse_instance=1, parse_integer=False, parse_case_sensitive=True, parse_multiline=False, parse_mode=None):
    if parse_mode is None:
        print(lr_box("parse_mode is undefined!"))
        return

    # parse_memory_map filter
    if parse_case_sensitive:
        regex = re.compile(str.encode(regex_string, 'ascii'), re.MULTILINE)
    else:
        regex = re.compile(
            str.encode(
                regex_string,
                'ascii'),
            re.IGNORECASE | re.MULTILINE)

    if parse_memory_map is not None:
        match = regex.search(parse_memory_map)
        if not match:
            return

    instanceCount = 0
    component = []
    component.append(None)

    """
  The regex below will allow us to parse out the floats/scientific notation with 1 digit or more to the right of the decimal:

  re_value = re.compile(r"([-]{0,1}[0-9]{0,15}\.[0-9]{1,15}[E]{0,1}[-]{0,1}[+]{0,1}[0-9]{0,15})")
                           │        │         │  │         │       │       │        └── 0 or more (max 15) occurrences of digits between 0-9
                           │        │         │  │         │       │       └── 0 or 1 occurrence of "+"
                           │        │         │  │         │       └── 0 or 1 occurrence of "-"
                           │        │         │  │         └── 0 or 1 occurrence of "E"
                           │        │         │  └── 0 or more (max 15) occurrences of digits between 0-9
                           │        │         └── 1 occurence of "."
                           │        └── 0 or more (max 15) occurrences of digits between 0-9
                           └── 0 or 1 occurrence of "-"
  """

    re_value = re.compile(
        r"([-]{0,1}[0-9]{0,15}\.[0-9]{1,15}[E]{0,1}[-]{0,1}[+]{0,1}[0-9]{0,15})")
    #
    # The regex below will allow us to parse out integers
    #
    if parse_integer:
        re_value = re.compile("([-]{0,1}[0-9]+)")
    for line in file_handle:
        if parse_case_sensitive:
            re_component = re.compile(regex_string)
        else:
            re_component = re.compile(regex_string, re.IGNORECASE)
        result_line = re_component.search(line)
        if result_line is not None:
            result_line = result_line.group()

            if parse_multiline:
                value = re_value.findall(result_line)
                array = []
                while len(value) > 0:
                    for x in value:
                        array.append(x)
                    next_line = next(file_handle)
                    value = re_value.findall(next_line)
                component.append(array)

                instanceCount = instanceCount + 1
                if instanceCount == parse_instance:
                    if parse_value_index is not None:
                        # Return an array element
                        return component[-1][parse_value_index]
                    else:
                        # Return the entire array
                        return component[-1]

            else:
                desired_line = line
                for i in range(0, parse_line_offset):
                    desired_line = next(file_handle)
                value = re_value.findall(desired_line)
                if value is not None:
                    try:
                        component.append(value[parse_value_index])
                        instanceCount = instanceCount + 1
                        if instanceCount == parse_instance:
                            return component[-1]
                    except BaseException:
                        pass

    # Special case
    if parse_instance < 0:
        try:
            if parse_multiline:
                if parse_value_index is not None:
                    # Return an array element
                    return component[parse_instance][parse_value_index]
                else:
                    # Return an array
                    return component[parse_instance]
            else:
                return component[parse_instance]
        except BaseException:
            return
