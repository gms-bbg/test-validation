# Test-Validation
A generic logfile validation written in Python 3

## Wiki: https://github.com/gms-bbg/test-validation/wiki

# Directory structure
```
test-validation/
├── R-7gradient/          Effective Fragment Potential Method (EFP) R**-7 Gradient
├── cc/                   Coupled-Cluster methods
├── ci/                   Configuration-Interaction (CI) methods
├── cim/                  Cluster-In-Molecule Framework
├── comp/                 Composite methods
├── dft/                  Density Functional Theory (DFT)
├── dftb/                 DFT Tight-Binding
├── ecp/                  Effective Core Potentials
├── eda/                  Energy Decomposition Analysis
├── efmo/                 Effective Fragment Molecular Orbital Method
├── efp-ci/               Effective Fragment Potential Method - CI
├── excitations/          Excited-State methods
|   └── tddft_os/         Time-Dependent Density Functional Theory (TDDFT)
├── exotic/               "exotic" runs
├── exrep/                EFP Exchange-Repulsion
├── globop/               Global optimization methods (e.g. Monte-Carlo, Genetic Algorithm)
├── gvb/                  General Valence (Van-Vleck) Bond Theory
├── libcchem/             LIBCCHEM runs
|   ├── cc/               CC
|   ├── mp2/              Second-Order Pertubation Theory methods
|   ├── paper/            Benchmark inputs for LIBCCHEM
|   ├── ri/               Resolution of the Identity (RI)
|   ├── scf/              Self-Consistent Field (SCF)
|   └── zapt/             Z-Average Perturbation Theory (ZAPT)
├── mcp/                  Model Core Potentials
├── mcscf/                Multi-configurational Self-Consistent Field methods
|   ├── diabat/           Diabatic state generation
|   ├── freq/             Hessian
|   ├── mrpt/             Multi-reference Perturbation Theory (MRPT)
|   ├── nacme/            Non-adiabatic Coupling Matrix Elements (NACME)
|   ├── psi/              
|   └── xing/             Inter-system crossings/Conical intersections 
├── mp2/                  MP2
├── numdiff/              Numerical Differentiation
├── openmp/               Threaded methods (e.g. SCF Fock build)
├── pes/                  Potential Energy Surface
├── qmefpea/              QM-EFP Energy Analysis
├── quanpol/              Quantum Chemistry Polarizable Force Field Program (QUANPOL)
├── relwfn/               Relativistic wavefunction methods
├── rhf/                  Restricted Hartree-Fock (RHF) for closed-shell
├── rohf/                 Restricted Open-shell Hartree-Fock (ROHF)
├── semi-emperical/       Semi-empirical methods
├── solvent/              Solvent methods
|   ├── efp-ctcut/        EFP Charge-Transfer (CT) Cutoff
|   ├── efp1/             Effective Fragment Potential 1 Method
|   ├── efp2/             Generalized Effective Fragment Potential Method
|   ├── mnsol/            University of Minnesota Solvation Models
|   ├── pcm/              Polarizable Continuum Model (PCM)
|   ├── reorg/            Solvent Reorganization Energy
|   ├── scrf/             Self-Consistent Reaction Field (SCRF)
|   └── svpe/             Surface and Volume Polarization for Electrostatics (SVPE)
├── spectra/              Spectra runs
├── standard/             Standard GAMESS test set (not validated in this test suite)
├── svd/                  Single-Value Decomposition (SVD)
├── tddft/                TDDFT
├── travis-ci/            Standard GAMESS test set (validated in this test suite)
├── trf/                  Integral transformation runs
├── uhf/                  Un-restricted Hartree-Fock (UHF) for open-shell
├── _parsegroups_/        contains .parsegroup files that define the parsing for a particular parse group
└── checkgms.py           Main script to run test validation of *.log files or generate validation files from *.log files
└── checkgms_parsers.py   Defines log file parsing
└── checkgms_stable.py    Defines flow for parsing and validation
└── checkgms_utils.py     Defines utility functions
└── queuetest.py          Script to submit jobs to a queuing system
└── runtest.py            Script to run calculations directly
└── parse.inp             Defines the order of the parse groups
└── LICENSE
└── README.md
└── TIMINGS.md            Contains run timings on BOLT and test input categorization
```

# checkgms.py Usage

Must be called within the test-validation folder.

```
./checkgms.py --help

usage: checkgms.py [-h] [--dryrun] [--file FILE] [--folder FOLDER]
                   [--json_create] [-a] [-d] [-e] [-g] [-p] [-v]
                   [--skip_file SKIP_FILE] [--skip_folder SKIP_FOLDER]
                   [--skip_json_create]

GAMESS Test Validation

optional arguments:
  -h, --help                 show this help message and exit
  --dryrun                   cycles through filelist without parsing
  --file FILE                process file(s) containing substring
  --folder FOLDER            process folder(s) containing substring
  --json_create              force the creation of JSON validation files
  -a, --array                print out array values
  -d, --debug                debug print control
  -e, --exit_on_fail         exit on first failed validation
  -g, --group                print group header for values
  -p, --verbose_parsing      verbose printing during parsing
  -v, --verbose_validation   verbose printing during validation
  --skip_file SKIP_FILE      skip file(s) containing substring
  --skip_folder SKIP_FOLDER  skip folder(s) containing substring
  --skip_json_create         skip creation of new JSON validation files
  --test_type TEST_TYPE      test input type: small, medium, large
```

# queuetest.py / runtest.py Usage

Must be called one directory-level **above** the test-validation folder.

```
./queuetest.py --help

usage: queuetest.py / runtest.py
                    [-h] [--file FILE] [--folder FOLDER] [-n NCPUS]
                    [--output_extension OUTPUT_EXTENSION]
                    [--skip_file SKIP_FILE] [--skip_folder SKIP_FOLDER]

GAMESS Test Submission / Launch

optional arguments:
  -h, --help                     show this help message and exit
  --file FILE                    process file(s) containing substring
  --folder FOLDER                process folder(s) containing substring
  -n NCPUS, --ncpus NCPUS        number of GAMESS compute processes
  --output_extension EXTENSION   extension to use for output files default(".log")
  --skip_file SKIP_FILE          skip file(s) containing substring
  --skip_folder SKIP_FOLDER      skip folder(s) containing substring
  --test_type TEST_TYPE          test input type: small, medium, large
```

# Example Usage

-  Validate all existing log files with minimal verbosity:

   ```./checkgms.py```

-  Validate all existing log files with minimal verbosity BUT exit on the first failure:

   ```./checkgms.py -e```

-  Validate all existing log files and show each validation made:

   ```./checkgms.py -v```

-  Validate all existing log files and show each validation made along with parse group headers:

   ```./checkgms.py -v -g```

-  Validate all folders containing the sub-string 'parallel':

   ```./checkgms.py --folder=parallel```

-  Validate all folders containing the sub-string 'parallel' but SKIP all folders containing the sub-string 'libcchem':

   ```./checkgms.py --folder=parallel --skip_folder=libcchem```

-  Validate all folders containing the sub-string 'parallel' AND all files containing sub-string 'mp2' but SKIP all folders containing the sub-string 'libcchem':

   ```./checkgms.py --folder=parallel --skip_folder=libcchem --file=mp2```

-  Validate all folders containing the sub-string 'parallel' AND all files containing sub-string 'mp2' but SKIP all folders containing the sub-string 'libcchem' AND SKIP all files containing the substring 'zapt':

   ```./checkgms.py --folder=parallel --skip_folder=libcchem --file=mp2 --skip_file=zapt```

-  Validate all existing log files with minimal verbosity BUT do not create NEW validation files (*.json) if they do not already exist:

   ```./checkgms.py --skip_json_create```

-  To see what files get picked up by the ```--folder, --skip_folder, --file, skip_file``` flags just add the ```--dryrun``` flag to the command.  This will not perform the validation.

