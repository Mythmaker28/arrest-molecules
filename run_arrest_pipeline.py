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
- delegates execution to an existing analysis script if found.
It does NOT modify or fabricate any scientific data.
"""

from pathlib import Path
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parent
DATA_DIR = REPO_ROOT / "Data_Package_FAIR2"

REQUIRED_FILES = [
    DATA_DIR / "API_Calculations_Full.xlsx",
    DATA_DIR / "Experimental_Protocols_Summary.csv",
    DATA_DIR / "Confidence_Grading_Matrix.csv",
]

SCRIPT_CANDIDATES = [
    REPO_ROOT / "test_api_calculations.py",
    REPO_ROOT / "Python_Code_API_Monte_Carlo.py",
    REPO_ROOT / "Data_Package_FAIR2" / "test_api_calculations.py",
    REPO_ROOT / "Data_Package_FAIR2" / "Python_Code_API_Monte_Carlo.py",
]


def check_required_files() -> None:
    missing = [p for p in REQUIRED_FILES if not p.exists()]
    if missing:
        print("[ERROR] Missing required input files:")
        for m in missing:
            print(f"  - {m}")
        print("Please ensure all data files are present in Data_Package_FAIR2.")
        sys.exit(1)

def find_analysis_script() -> Path | None:
    for script in SCRIPT_CANDIDATES:
        if script.exists():
            return script
    return None

def main() -> None:
    print(f"[INFO] Running Arrest Molecules pipeline from: {REPO_ROOT}")

    check_required_files()

    outputs = REPO_ROOT / "outputs"
    outputs.mkdir(exist_ok=True)
    print(f"[INFO] Outputs directory: {outputs}")

    script = find_analysis_script()
    if script is None:
        print(
            "[WARN] No main analysis script found "
            "(expected one of: test_api_calculations.py, Python_Code_API_Monte_Carlo.py)."
        )
        print("       Data files are present. Run your preferred analysis script manually.")
        sys.exit(0)

    print(f"[INFO] Delegating to: {script.name}")
    try:
        subprocess.run([sys.executable, str(script)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {script.name} failed with exit code {e.returncode}")
        sys.exit(e.returncode)

    print("[INFO] Pipeline completed successfully.")

if __name__ == "__main__":
    main()
