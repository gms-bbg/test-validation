from basis_6311g import *
from basis_sto import *
from basis_631g import *

import fileinput
import sys

'''
Place GAMESS coordinates in coords.xyz 
python append_basis.py 
'''

file = sys.argv[1]
basis = sys.argv[2]

if basis == "sto":
  for line in fileinput.FileInput(file, inplace=1):
    if "H     1.0" in line:
      line = line.replace(line,line+hydrogen_sto_basis)
    print(line, end='')

  for line in fileinput.FileInput(file,inplace=1):
    if "C     6.0" in line:
      line = line.replace(line,line+carbon_sto_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "N     7.0" in line:
      line = line.replace(line,line+nitrogen_sto_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "O     8.0" in line:
      line = line.replace(line,line+oxygen_sto_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "P    15.0" in line:
      line = line.replace(line,line+phosphorus_sto_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "S    16.0" in line:
      line = line.replace(line,line+sulfur_sto_basis)
    print(line, end='')
elif basis == "631g":
  for line in fileinput.FileInput(file, inplace=1):
    if "H     1.0" in line:
      line = line.replace(line,line+hydrogen_631g_basis)
    print(line, end='')

  for line in fileinput.FileInput(file,inplace=1):
    if "C     6.0" in line:
      line = line.replace(line,line+carbon_631g_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "N     7.0" in line:
      line = line.replace(line,line+nitrogen_631g_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "O     8.0" in line:
      line = line.replace(line,line+oxygen_631g_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "P    15.0" in line:
      line = line.replace(line,line+phosphorus_631g_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "S    16.0" in line:
      line = line.replace(line,line+sulfur_631g_basis)
    print(line, end='')
elif basis == "6311g":
  for line in fileinput.FileInput(file, inplace=1):
    if "H     1.0" in line:
      line = line.replace(line,line+hydrogen_6311g_basis)
    print(line, end='')

  for line in fileinput.FileInput(file,inplace=1):
    if "C     6.0" in line:
      line = line.replace(line,line+carbon_6311g_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "N     7.0" in line:
      line = line.replace(line,line+nitrogen_6311g_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "O     8.0" in line:
      line = line.replace(line,line+oxygen_6311g_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "P    15.0" in line:
      line = line.replace(line,line+phosphorus_6311g_basis)
    print(line, end='')

  for line in fileinput.FileInput(file, inplace=1):
    if "S    16.0" in line:
      line = line.replace(line,line+sulfur_6311g_basis)
    print(line, end='')
else:
  "basis set not supported"
