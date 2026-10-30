# Cosmological Parameter Estimation Framework

*Latest update : October 30,2026*
A general-purpose computational framework for cosmological parameter estimation, MCMC analysis, and observational constraint studies.

The framework incorporates observational datasets and likelihoods from **Planck, ACT, DESI and BAO**, using established scientific computing tools.

## Tech Stack

| Technology    | Purpose                                   |
| ------------- | ----------------------------------------- |
| Python        | Core programming                          |
| Cobaya        | Bayesian inference and MCMC sampling      |
| CLASS         | Cosmological Boltzmann solver             |
| GetDist       | MCMC analysis and posterior visualization |
| NumPy / SciPy | Numerical computation                     |
| Matplotlib    | Scientific visualization                  |
| Pandas        | Data processing                           |
| YAML          | Analysis configuration                    |
| Git / GitHub  | Version control                           |

## Installation

**1. Clone the repository**

```bash
git clone <repository-url>
cd <repository-name>
```

**2. Create a virtual environment**

```powershell
python -m venv .venv
```

**3. Activate the environment (Windows)**

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux:

```bash
source .venv/bin/activate
```

**4. Install dependencies**

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Ensure Cobaya, CLASS and their required external dependencies are installed and configured.

**Always activate the virtual environment before running any scripts.**

## Observational Datasets

The framework supports:

* **Planck:** CMB observations.
* **ACT:** CMB observations.
* **DESI:** Large-scale structure observations.
* **BAO:** Baryon Acoustic Oscillation constraints.

Individual and combined dataset configurations can be used depending on the analysis requirements.

Required likelihood packages and external data paths must be configured before execution.

## Running an Analysis

Test a configuration:

```bash
cobaya-run yamls/configuration.yaml --test
```

Run the analysis:

```bash
cobaya-run yamls/configuration.yaml
```

Replace `configuration.yaml` with the relevant YAML configuration file.

## Repository Contents

* Computational scripts and supporting Python modules.
* MCMC chains and associated data.
* Analysis configuration files.
* Data-processing and visualization utilities.

## Reproducibility

The `.venv` directory and temporary computational outputs are excluded from version control. Dependencies are specified in `requirements.txt` to facilitate environment reconstruction.

## Documentation

* [Cobaya](https://cobaya.readthedocs.io/)
* [CLASS](https://class-code.net/)
* [GetDist](https://getdist.readthedocs.io/)
* [Planck Legacy Archive](https://pla.esac.esa.int/)
* [ACT](https://act.princeton.edu/)
* [DESI](https://www.desi.lbl.gov/)

---

**Scope:** This repository provides a model-independent computational infrastructure. The framework is not restricted to any particular theoretical inflationary model.
