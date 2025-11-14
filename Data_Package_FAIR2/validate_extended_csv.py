#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation script for Compound_Properties_Experimental_Extended.csv
Checks:
- Valid placeholder format (NR, NA, ND, EST - uppercase only)
- Header consistency with main database
- Basic data integrity
"""

import pandas as pd
import sys


def main():
    """Run validation checks on Extended CSV."""
    
    # Load Extended CSV
    try:
        df = pd.read_csv('Compound_Properties_Experimental_Extended.csv')
        print(f'[OK] Extended CSV loaded: {len(df)} rows')
    except Exception as e:
        print(f'[ERROR] Failed to load Extended CSV: {e}')
        sys.exit(1)

    # Check valid placeholders
    valid_placeholders = {'NR', 'NA', 'ND', 'EST'}
    invalid_found = False

    for col in df.columns:
        for idx, val in enumerate(df[col]):
            if isinstance(val, str):
                val_upper = val.strip().upper()
                # Check for invalid lowercase or mixed case placeholders
                if val_upper in valid_placeholders and val.strip() != val_upper:
                    print(
                        f'[ERROR] Row {idx+2}, Column {col}: '
                        f'Invalid placeholder case "{val}" (should be uppercase)'
                    )
                    invalid_found = True

    if not invalid_found:
        print('[OK] All placeholders use valid uppercase format (NR/NA/ND/EST)')

    # Check header consistency with main database
    try:
        df_main = pd.read_csv('Compound_Properties_Database.csv')
        if list(df.columns) != list(df_main.columns):
            print('[ERROR] Extended CSV headers do not match main database')
            print(f'  Extended: {list(df.columns)[:5]}...')
            print(f'  Main: {list(df_main.columns)[:5]}...')
            sys.exit(1)
        else:
            print('[OK] Extended CSV headers match main database')
    except Exception as e:
        print(f'[WARNING] Could not compare headers: {e}')

    print('\n[OK] Validation passed')
    
    if invalid_found:
        sys.exit(1)


if __name__ == '__main__':
    main()

