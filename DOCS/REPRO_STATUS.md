# Reproducibility Status – Phase 1

This document summarizes the minimal steps required to reproduce the core
analyses of the **arrest-molecules** project.

## Relevant structure

- `Data_Package_FAIR2/` – curated input data package.
- `test_api_calculations.py` / `Python_Code_API_Monte_Carlo.py` – main analysis scripts.
- `requirements.txt` (root) – minimal Python environment.
- `run_arrest_pipeline.py` – single entrypoint wrapper.
- `outputs/` – created automatically to store generated results (ignored by git).

## Minimal reproduction protocol

From the repository root:

1. `python -m venv .venv`
2. Activate:
   - Windows: `.venv\\Scripts\\activate`
   - Linux/Mac: `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python run_arrest_pipeline.py`

If required data files are missing, the script will stop and list them.

## Notes

- No scientific values are changed by this pipeline.
- Detailed figure-level mapping and CI can be added in a later phase.
- Tested on the maintainer's machine with Python 3.13 and the root requirements.txt.

