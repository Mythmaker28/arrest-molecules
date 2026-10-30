# Reproducibility Status – Phase 1

This document summarizes the minimal steps required to reproduce the core
analyses of the **arrest-molecules** project.

## Relevant structure

- `Data_Package_FAIR2/` – curated input data package.
- `Data_Package_FAIR2/Python_Code_API_Monte_Carlo.py` / `Data_Package_FAIR2/test_api_calculations.py` – main analysis script and its unit tests.
- `requirements.txt` (root) – minimal Python environment.
- `run_arrest_pipeline.py` – single entrypoint wrapper.
- `outputs/` – created automatically to store generated results (ignored by git):
  `API_Comparison_All_Compounds.csv` and `API_Comparison_All_Compounds.png`.

## Minimal reproduction protocol

From the repository root:

1. `python -m venv .venv`
2. Activate:
   - Windows: `.venv\\Scripts\\activate`
   - Linux/Mac: `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python run_arrest_pipeline.py`

If required data files are missing, the script will stop and list them.
Otherwise it runs these steps in order (scripts from `Data_Package_FAIR2/`):

1. `dataset_status.py` – row counts, placeholders and documented tiers
2. `data_validation.py` – core dataset and predictions matrix
3. `validate_extended_csv.py` – extended dataset
4. `quickcheck_api.py` – API recomputed from the core dataset
5. `python -m unittest` – unit tests of the data package
6. `Python_Code_API_Monte_Carlo.py --all` – Monte Carlo API for all compounds
   (default seed and iteration count), written to `outputs/`

It stops at the first step that fails and exits with that step's exit code.

## Notes

- No scientific values are changed by this pipeline.
- Detailed figure-level mapping and CI can be added in a later phase.
  No GitHub Actions workflow runs `run_arrest_pipeline.py` yet; the workflows
  run the individual scripts.
- The earlier single-script version of the pipeline was tested on the
  maintainer's machine with Python 3.13 and the root requirements.txt.
- Checked on 2026-10-30 (Linux): the six steps complete with Python 3.9.25 and
  3.11.17 and the pinned `Data_Package_FAIR2/requirements.txt` (the versions
  installed by CI), and the `outputs/` files are byte-identical between those
  runs. They also complete with Python 3.11.17 and the root `requirements.txt`,
  whose newer package versions change the last digits of the CSV values
  (relative difference ≤ 1.4e-15) and the bytes of the figure, so compare
  outputs from unpinned environments with a tolerance rather than checksums.

