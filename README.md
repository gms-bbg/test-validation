# test-validation
A generic logfile validation written in Python 3 (~ 1 GB repo)

## Wiki: https://github.com/gms-bbg/test-validation/wiki

```
usage: checkgms.py [-h] [--dryrun] [--file FILE_SUBSTRING] [--folder FOLDER_SUBSTRING]
                   [-a] [-d] [-e] [-g] [-p] [-v]

GAMESS Test Validation

optional arguments:
  -h, --help                show this help message and exit
  --dryrun                  cycles through filelist without parsing
  --file FILE_SUBSTRING     process file(s) containing substring
  --folder FOLDER_SUBSTRING process folder(s) containing substring
  -a, --array               print out array values
  -d, --debug               debug print control
  -e, --exit_on_fail        exit on first failed validation
  -g, --group               print group header for values
  -p, --verbose_parsing     verbose printing during parsing
  -v, --verbose_validation  verbose printing during validation
  --skip_file               skip file(s) containing substring
  --skip_folder             skip folder(s) containing substring
  --skip_json_create        skip creation of new JSON validation files
```

## Usage:

1.  Run `./checkgms.py` the to create validation files (*.json) from existing log files.
2.  Run `./checkgms.py` again to validate (*.log) files.

## To perform validation on only the standard test folder:
```
./checkgms.py --folder=standard
```

## To perform validation on only exam27 in the standard test folder:
```
./checkgms.py --folder=standard --file=exam27
```
## For a very verbose parsing:
```
./checkgms.py -p -g -a
```

## For a very verbose validation:
```
./checkgms.py -p -v -g -a
```



