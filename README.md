# Test-Validation
A generic logfile validation written in Python 3

# Wiki
https://github.com/gms-bbg/test-validation/wiki

# Directory structure
```
tests/
├── R-7gradient/          Effective Fragment Potential Method (EFP) R**-7 Gradient
├── cc/                   Coupled-Cluster methods
├── ci/                   Configuration-Interaction methods
├── cim/                  Cluster-In-Molecule Framework
├── comp/                 Composite methods
├── dft/                  Density Functional Theory (legacy)
├── dft-new/              Density Functional Theory (new)
├── dftb/                 DFT Tight-Binding
├── ecp/                  Effective Core Potentials
├── eda/                  Energy Decomposition Analysis
├── efmo/                 Effective Fragment Molecular Orbital Method
├── efp-ci/               Effective Fragment Potential Method - CI
├── efp-mpiomp/           Effective Fragment Potential Method (MPI+OpenMP)
├── excitations/          Excited-State methods
|   └── tddft_os/         Time-Dependent Density Functional Theory
├── exotic/               "exotic" runs
├── exrep/                EFP Exchange-Repulsion
├── fmo/                  Fragment Molecular Orbital Method
├── globop/               Global optimization methods (e.g. Monte-Carlo, Genetic Algorithm)
├── gvb/                  General Valence (Van-Vleck) Bond Theory
├── info-regression-baseline/ Directory for baseline performance info
├── libcchem/             LIBCCHEM runs
|   ├── ahf/              Accelerated Hartree Fock
|   ├── cc/               CC
|   ├── genfock/          Generalized Fock Build
|   ├── mp2/              Second-Order Pertubation Theory methods
|   ├── paper/            Benchmark inputs for LIBCCHEM
|   ├── ri/               Resolution of the Identity
|   ├── scf/              Self-Consistent Field
|   └── zapt/             Z-Average Perturbation Theory
├── mcp/                  Model Core Potentials
├── mcpdft/               Multi-configurational Pair Density Functional Theory
├── mcscf/                Multi-configurational Self-Consistent Field methods
|   ├── diabat/           Diabatic state generation
|   ├── freq/             Hessian
|   ├── mrpt/             Multi-reference Perturbation Theory
|   ├── nacme/            Non-adiabatic Coupling Matrix Elements (NACME)
|   ├── psi/              
|   └── xing/             Inter-system crossings/Conical intersections 
├── mp2/                  MP2
├── neb/                  Nudged Elastic Band Method
├── numdiff/              Numerical Differentiation
├── pes/                  Potential Energy Surface
├── qmefpea/              QM-EFP Energy Analysis
├── quanpol/              Quantum Chemistry Polarizable Force Field Program
├── quao-bug/             Quasi-Atomic Orbital
├── relwfn/               Relativistic wavefunction methods
├── rhf/                  Restricted Hartree-Fock (RHF) for closed-shell
├── rhf-mpiomp/           Restricted Hartree-Fock (RHF) for closed-shell (MPI+OpenMP)
├── ricc-mpiomp/          Resolution of the Identity Coupled-Cluster (MPI+OpenMP)
├── rimp2-mpiomp/         Resolution of the Identify MP2 Energy (MPI+OpenMP)
├── rimpgrd-mpiomp/       Resolution of the Identify MP2 Gradient (MPI+OpenMP)
├── rohf/                 Restricted Open-shell Hartree-Fock (ROHF)
├── semi-emperical/       Semi-empirical methods
├── sformas/              Spin-flip ORMAS
├── solvent/              Solvent methods
|   ├── cmirs/            Composite Method for Implicit Representation of Solvent
|   ├── efp-ctcut/        EFP Charge-Transfer Cutoff
|   ├── efp1/             Effective Fragment Potential 1 Method
|   ├── efp2/             Generalized Effective Fragment Potential Method
|   ├── mnsol/            University of Minnesota Solvation Models
|   ├── pcm/              Polarizable Continuum Model
|   ├── qm-efp2/          QM+EFP2
|   ├── reorg/            Solvent Reorganization Energy
|   ├── scrf/             Self-Consistent Reaction Field (SCRF)
|   ├── ssvpe/            Surface and Simulation of Volume Polarization for                           
Electrostatics
|   ├── svp/              Surface and Volume Polarization
|   └── svpe/             Surface and Volume Polarization for Electrostatics
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
└── queuetest.py          Script to submit GAMESS jobs to a queuing system
└── runtest.py            Script to run GAMESS calculations directly
└── parse.inp             Defines the order of the parse groups
└── LICENSE
└── README.md
└── TIMINGS.md            Contains run timings on BOLT and test input categorization
```

# checkgms.py Usage

Must be called within the test-validation folder.

```
usage: checkgms.py [-h] [-r] [-m {validation,regression,both}] [-a ARCH] [-s SYSTEM] [-n NCPUS] [-g NACCELERATORS] [--dryrun] [--file FILE]
                   [--folder FOLDER] [--filepath FILEPATH] [--test_path TEST_PATH] [--json_create] [--array] [-d] [-i] [-e] [--group] [-p] [-v]
                   [--skip_file SKIP_FILE] [--skip_folder SKIP_FOLDER] [--skip_json_create] [--test_type TEST_TYPE] [--fail_rename FAIL_RENAME]
                   [--no_dump]

GAMESS Test Validation

optional arguments:
  -h, --help            show this help message and exit
  -r, --regression      performance regression testing
  -m {validation,regression,both}, --mode {validation,regression,both}
                        testing mode, default: validation
  -a ARCH, --arch ARCH  architecture string used for performance regression
  -s SYSTEM, --system SYSTEM
                        HPC system string used for performance regression
  -n NCPUS, --ncpus NCPUS
                        number of GAMESS compute processes for performance regression
  -g NACCELERATORS, --naccelerators NACCELERATORS
                        number of accelerators for performance regression
  --dryrun              cycles through filelist without parsing
  --file FILE           process file(s) containing substring
  --folder FOLDER       process folder(s) containing substring
  --filepath FILEPATH   process filepath(s) containing substring
  --test_path TEST_PATH
                        process file(s) in the specified path
  --json_create         force the creation of JSON validation files
  --array               print out array values
  -d, --debug           debug print control
  -i, --print_to_stdout
                        print_to_stdout
  -e, --exit_on_fail    exit on first failed validation
  --group               print group header for values
  -p, --verbose_parsing
                        verbose printing during parsing
  -v, --verbose_validation
                        verbose printing during validation
  --skip_file SKIP_FILE
                        skip file(s) containing substring
  --skip_folder SKIP_FOLDER
                        skip folder(s) containing substring
  --skip_json_create    skip creation of new JSON validation files
  --test_type TEST_TYPE
                        test input type: small, medium, large, msucc
  --fail_rename FAIL_RENAME
                        if validation fail, replaces ".log" with arg value
  --no_dump             suppress logfile output when exiting on failure
```

# queuetest.py / runtest.py Usage

Must be called one directory-level **above** the test-validation folder.

```
usage: queuetest.py [-h] [--pre PRE] [--post POST] [--dryrun] [--no_counter] [-i] [--file FILE] [--folder FOLDER] [--filepath FILEPATH] [--path PATH]
                    [--version VERSION] [-d] [-n NCPUS] [-t THREADS] [--mpi] [--hpe-cray-ex] [--hpe-cray-cs] [--cray-xt] [--cray-xc]
                    [--output_extension OUTPUT_EXTENSION] [-q QUEUE] [--skip_file SKIP_FILE] [--skip_folder SKIP_FOLDER] [--skip_log] [--no_skip]
                    [--test_type TEST_TYPE] [--stderr] [-c] [--breakdown] [--no_accumulate] [--sourcefile SOURCEFILE] [--bwrap]

GAMESS Test Launch

optional arguments:
  -h, --help            show this help message and exit
  --pre PRE             command to run before each test
  --post POST           command to run after each test
  --dryrun              cycles through filelist without parsing
  --no_counter          suppress the file counter
  -i, --print_to_stdout
                        print_to_stdout
  --file FILE           process file(s) containing substring
  --folder FOLDER       process folder(s) containing substring
  --filepath FILEPATH   process filepath(s) containing substring
  --path PATH           Use a different GAMESS path
  --version VERSION     Use a GAMESS version
  -d, --debug           debug print control
  -n NCPUS, --ncpus NCPUS
                        number of GAMESS compute processes
  -t THREADS, --threads THREADS
                        number of parallel GAMESS computing
  --mpi                 use mpi
  --hpe-cray-ex         use hpe-cray-ex
  --hpe-cray-cs         use hpe-cray-cs
  --cray-xt             use cray-xt
  --cray-xc             use cray-xc
  --output_extension OUTPUT_EXTENSION
                        extension to use for output files default(".log")
  -q QUEUE, --queue QUEUE
                        specify SLURM queue
  --skip_file SKIP_FILE
                        skip file(s) containing substring
  --skip_folder SKIP_FOLDER
                        skip folder(s) containing substring
  --skip_log            skip file if log file exists
  --no_skip             ignore TRAVIS-CI SKIP tags during input filtering
  --test_type TEST_TYPE
                        test input type: small, medium, large, msucc
  --stderr              print to stderr
  -c, --coverage        run code coverage with GNU gcov
  --breakdown           breakdown coverage information per input
  --no_accumulate       do not accumulate coverage statistics across inputs
  --sourcefile SOURCEFILE
                        limit coverage data to source file substring, only valid with --breakdown
  --bwrap               execute tests in a bwrap sandbox to avoid leftover semaphores
```

```
usage: runtest.py [-h] [--pre PRE] [--post POST] [--dryrun] [--no_counter] [-i] [--file FILE] [--folder FOLDER] [--filepath FILEPATH] [--path PATH]
                  [--version VERSION] [-d] [-n NCPUS] [-t THREADS] [--mpi] [--hpe-cray-ex] [--hpe-cray-cs] [--cray-xt] [--cray-xc]
                  [--output_extension OUTPUT_EXTENSION] [-q QUEUE] [--skip_file SKIP_FILE] [--skip_folder SKIP_FOLDER] [--skip_log] [--no_skip]
                  [--test_type TEST_TYPE] [--stderr] [-c] [--breakdown] [--no_accumulate] [--sourcefile SOURCEFILE] [--bwrap]

GAMESS Test Launch

optional arguments:
  -h, --help            show this help message and exit
  --pre PRE             command to run before each test
  --post POST           command to run after each test
  --dryrun              cycles through filelist without parsing
  --no_counter          suppress the file counter
  -i, --print_to_stdout
                        print_to_stdout
  --file FILE           process file(s) containing substring
  --folder FOLDER       process folder(s) containing substring
  --filepath FILEPATH   process filepath(s) containing substring
  --path PATH           Use a different GAMESS path
  --version VERSION     Use a GAMESS version
  -d, --debug           debug print control
  -n NCPUS, --ncpus NCPUS
                        number of GAMESS compute processes
  -t THREADS, --threads THREADS
                        number of parallel GAMESS computing
  --mpi                 use mpi
  --hpe-cray-ex         use hpe-cray-ex
  --hpe-cray-cs         use hpe-cray-cs
  --cray-xt             use cray-xt
  --cray-xc             use cray-xc
  --output_extension OUTPUT_EXTENSION
                        extension to use for output files default(".log")
  -q QUEUE, --queue QUEUE
                        specify SLURM queue
  --skip_file SKIP_FILE
                        skip file(s) containing substring
  --skip_folder SKIP_FOLDER
                        skip folder(s) containing substring
  --skip_log            skip file if log file exists
  --no_skip             ignore TRAVIS-CI SKIP tags during input filtering
  --test_type TEST_TYPE
                        test input type: small, medium, large, msucc
  --stderr              print to stderr
  -c, --coverage        run code coverage with GNU gcov
  --breakdown           breakdown coverage information per input
  --no_accumulate       do not accumulate coverage statistics across inputs
  --sourcefile SOURCEFILE
                        limit coverage data to source file substring, only valid with --breakdown
  --bwrap               execute tests in a bwrap sandbox to avoid leftover semaphores
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

-  Validate a particular log file when the absolute full/relative path is known:

   ```./checkgms.py --filepath=travis-ci/parallel/exam01.log```

-  Validate all existing log files with minimal verbosity BUT do not create NEW validation files (*.json) if they do not already exist:

   ```./checkgms.py --skip_json_create```

-  To see what files get picked up by the ```--folder, --skip_folder, --file, skip_file``` flags just add the ```--dryrun``` flag to the command.  This will not perform the validation.

