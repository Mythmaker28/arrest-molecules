#!/usr/bin/env python
"""
Arrest Molecules - Reproducibility entrypoint.

Usage (from repository root):

    python -m venv .venv
    # Windows:
    #   .venv\\Scripts\\activate
    # Linux / Mac:
    #   source .venv/bin/activate
    pip install -r requirements.txt
    python run_arrest_pipeline.py

This script:
- verifies the presence of key data files in Data_Package_FAIR2,
- creates an `outputs/` directory if needed,
- runs these steps in order (scripts from Data_Package_FAIR2):
    1. dataset_status.py         row counts, placeholders and documented tiers
    2. data_validation.py        core dataset and predictions matrix checks
    3. validate_extended_csv.py  extended dataset schema and placeholders
    4. quickcheck_api.py         API recomputed from the core dataset
    5. python -m unittest        unit tests of the data package
    6. Python_Code_API_Monte_Carlo.py --all
       Monte Carlo API for all compounds (default seed and iterations);
       API_Comparison_All_Compounds.csv and .png are written to `outputs/`,
- stops at the first step that fails and exits with that step's exit code.
It does NOT modify or fabricate any scientific data.
"""

from pathlib import Path
import os
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parent
DATA_DIR = REPO_ROOT / "Data_Package_FAIR2"
OUTPUTS_DIR = REPO_ROOT / "outputs"

REQUIRED_FILES = [
    DATA_DIR / "API_Calculations_Full.xlsx",
    DATA_DIR / "Experimental_Protocols_Summary.csv",
    DATA_DIR / "Confidence_Grading_Matrix.csv",
    DATA_DIR / "Compound_Properties_Database.csv",
    DATA_DIR / "Compound_Properties_Experimental_Extended.csv",
]

# (description, arguments passed to the Python interpreter, working directory)
STEPS = [
    ("Dataset status", [DATA_DIR / "dataset_status.py"], DATA_DIR),
    ("Core dataset validation", [DATA_DIR / "data_validation.py"], DATA_DIR),
    ("Extended dataset validation", [DATA_DIR / "validate_extended_csv.py"], DATA_DIR),
    ("API quick check", [DATA_DIR / "quickcheck_api.py"], DATA_DIR),
    ("Unit tests", ["-m", "unittest", "-q"], DATA_DIR),
    ("Monte Carlo API for all compounds",
     [DATA_DIR / "Python_Code_API_Monte_Carlo.py", "--all"], OUTPUTS_DIR),
]


def check_required_files() -> None:
    missing = [p for p in REQUIRED_FILES if not p.exists()]
    if missing:
        print("[ERROR] Missing required input files:")
        for m in missing:
            print(f"  - {m}")
        print("Please ensure all data files are present in Data_Package_FAIR2.")
        sys.exit(1)

def run_steps(steps) -> None:
    env = dict(os.environ)
    # Figures are only saved to files, so no interactive backend is needed.
    env.setdefault("MPLBACKEND", "Agg")
    for number, (description, args, cwd) in enumerate(steps, start=1):
        # Flush so the header precedes the step's own output when stdout is a pipe.
        print(f"\n[STEP {number}/{len(steps)}] {description}", flush=True)
        try:
            subprocess.run([sys.executable] + [str(a) for a in args], cwd=str(cwd), env=env,
                           check=True)
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Step {number} ({description}) failed with exit code {e.returncode}")
            sys.exit(e.returncode)

def main() -> None:
    print(f"[INFO] Running Arrest Molecules pipeline from: {REPO_ROOT}")

    check_required_files()

    OUTPUTS_DIR.mkdir(exist_ok=True)
    print(f"[INFO] Outputs directory: {OUTPUTS_DIR}")

    run_steps(STEPS)

    print("\n[INFO] Pipeline completed successfully.")

if __name__ == "__main__":
    main()
