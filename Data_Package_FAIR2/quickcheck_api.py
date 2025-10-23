#!/usr/bin/env python3
"""
Quick Check - API Calculations Validation
Vérifie que les valeurs API correspondent aux valeurs attendues
"""

import pandas as pd
import sys

def quickcheck_api():
    """Vérifie les valeurs API calculées contre les valeurs attendues"""
    
    print("="*60)
    print("QUICK CHECK - API Validation")
    print("="*60)
    
    # Trouver le CSV (depuis n'importe quel répertoire)
    import os
    from pathlib import Path
    
    script_dir = Path(__file__).parent
    csv_path = script_dir / 'Compound_Properties_Database.csv'
    
    # Charger la base de données
    try:
        df = pd.read_csv(csv_path)
        print(f"\n[OK] {len(df)} compos\u00e9s charg\u00e9s\n")
    except FileNotFoundError:
        print(f"[ERREUR] CSV non trouv\u00e9: {csv_path}")
        return False
    
    # Valeurs attendues (depuis la littérature et nos calculs)
    expected_values = {
        'Salvinorin A': {
            'API_relative': 1.00,
            'CI_lower': 0.85,
            'CI_upper': 1.15,
            'tolerance': 0.05
        },
        'Rapamycin': {
            'API_relative': 0.12,
            'CI_lower': 0.08,
            'CI_upper': 0.16,
            'tolerance': 0.02
        },
        'Tetrodotoxin': {
            'API_relative': 4.0,
            'CI_lower': 3.2,
            'CI_upper': 4.8,
            'tolerance': 0.3
        },
        'Psilocybin': {
            'API_relative': -0.89,  # Négatif car oscillation
            'CI_lower': -1.05,
            'CI_upper': -0.73,
            'tolerance': 0.1
        }
    }
    
    all_pass = True
    
    for compound, expected in expected_values.items():
        row = df[df['Compound_Name'] == compound]
        
        if row.empty:
            print(f"[ERREUR] {compound} non trouvé dans la base")
            all_pass = False
            continue
        
        api_value = row['API_relative'].values[0]
        ci_lower = row['API_CI_lower'].values[0]
        ci_upper = row['API_CI_upper'].values[0]
        
        # Vérifier API
        api_diff = abs(api_value - expected['API_relative'])
        api_ok = api_diff <= expected['tolerance']
        
        # Vérifier CI
        ci_lower_ok = abs(ci_lower - expected['CI_lower']) <= expected['tolerance']
        ci_upper_ok = abs(ci_upper - expected['CI_upper']) <= expected['tolerance']
        
        status = "[OK]" if (api_ok and ci_lower_ok and ci_upper_ok) else "[FAIL]"
        
        print(f"{status} {compound}")
        print(f"  API: {api_value:.3f} (attendu {expected['API_relative']:.3f}, diff {api_diff:.3f})")
        print(f"  CI:  [{ci_lower:.3f}, {ci_upper:.3f}]")
        print(f"       (attendu [{expected['CI_lower']:.3f}, {expected['CI_upper']:.3f}])")
        
        if not (api_ok and ci_lower_ok and ci_upper_ok):
            all_pass = False
        
        print()
    
    # Statistiques globales
    print("="*60)
    print("STATISTIQUES GLOBALES")
    print("="*60)
    print(f"Composés totaux : {len(df)}")
    print(f"Arrest agents : {len(df[df['Arrest_Level'].str.contains('Level', na=False)])}")
    print(f"Oscillateurs : {len(df[df['Arrest_Level'].str.contains('Oscillation', na=False)])}")
    print(f"\nRépartition API :")
    print(f"  API > 1.0 : {len(df[df['API_relative'] > 1.0])}")
    print(f"  0.1 < API < 1.0 : {len(df[(df['API_relative'] > 0.1) & (df['API_relative'] < 1.0)])}")
    print(f"  API < 0.1 : {len(df[df['API_relative'] < 0.1])}")
    print(f"  API < 0 (oscillation) : {len(df[df['API_relative'] < 0])}")
    
    print("\n" + "="*60)
    if all_pass:
        print("[SUCCÈS] Tous les tests de validation réussis !")
        print("="*60)
        return True
    else:
        print("[ÉCHEC] Certaines valeurs ne correspondent pas")
        print("="*60)
        return False

if __name__ == '__main__':
    success = quickcheck_api()
    sys.exit(0 if success else 1)

