# test-validation
A generic logfile validation written in Python 3 (~ 1 GB repo)

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
```
