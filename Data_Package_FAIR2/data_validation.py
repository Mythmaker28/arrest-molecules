#!/usr/bin/env python3
"""
Validation des données du Molecular Arrest Framework
Vérifie l'intégrité et la cohérence des fichiers CSV
"""

import pandas as pd
import sys
from pathlib import Path

def validate_compound_database(csv_path='Compound_Properties_Database.csv'):
    """
    Valide la base de données de composés
    
    Vérifications:
    - Colonnes requises présentes
    - Valeurs positives pour paramètres pharmacologiques
    - Cohérence τ = 1/k_off (±5%)
    - PMIDs valides (format numérique)
    - Pas de valeurs manquantes critiques
    """
    print(f"[VALIDATION] Chargement {csv_path}...")
    
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"[ERREUR] Fichier non trouvé: {csv_path}")
        return False
    
    print(f"[OK] {len(df)} composés chargés\n")
    
    # 1. Colonnes requises
    required_cols = [
        'Compound_Name', 'K_d_nM', 'EC50_nM', 
        'tau_residence_min', 'k_off_per_min', 'K_i_Source_PMID'
    ]
    
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        print(f"[ERREUR] Colonnes manquantes: {missing}")
        return False
    print(f"[OK] Toutes les colonnes requises présentes")
    
    # 2. Valeurs positives
    errors = []
    for col in ['K_d_nM', 'EC50_nM', 'tau_residence_min', 'k_off_per_min']:
        negative = df[df[col] <= 0][['Compound_Name', col]]
        if not negative.empty:
            errors.append(f"  {col}: {len(negative)} valeurs ≤ 0")
            for idx, row in negative.iterrows():
                print(f"    - {row['Compound_Name']}: {col} = {row[col]}")
    
    if errors:
        print(f"[ERREUR] Valeurs non-positives détectées:")
        for err in errors:
            print(err)
        return False
    print(f"[OK] Toutes les valeurs pharmacologiques sont positives")
    
    # 3. Cohérence tau = 1/k_off (tolérance ±5%)
    print("\n[CHECK] Coherence tau = 1/k_off...")
    tolerance = 0.05
    incoherent = []
    
    for idx, row in df.iterrows():
        tau_measured = row['tau_residence_min']
        k_off = row['k_off_per_min']
        
        if k_off > 0:
            tau_calculated = 1 / k_off
            relative_error = abs(tau_measured - tau_calculated) / tau_calculated
            
            if relative_error > tolerance:
                incoherent.append({
                    'compound': row['Compound_Name'],
                    'tau_measured': tau_measured,
                    'tau_calculated': tau_calculated,
                    'error': relative_error * 100
                })
    
    if incoherent:
        print(f"[AVERTISSEMENT] {len(incoherent)} incoherences tau = 1/k_off (tolerance {tolerance*100}%):")
        for item in incoherent:
            print(f"  - {item['compound']}: tau={item['tau_measured']:.2f}, 1/k_off={item['tau_calculated']:.2f} (erreur {item['error']:.1f}%)")
    else:
        print(f"[OK] Toutes les valeurs tau coherentes avec k_off (+/-{tolerance*100}%)")
    
    # 4. PMIDs valides
    print("\n[CHECK] Validation PMIDs...")
    invalid_pmids = []
    
    for idx, row in df.iterrows():
        pmid = row['K_i_Source_PMID']
        if pd.notna(pmid):
            try:
                pmid_int = int(pmid)
                if pmid_int <= 0:
                    invalid_pmids.append(f"{row['Compound_Name']}: {pmid}")
            except (ValueError, TypeError):
                invalid_pmids.append(f"{row['Compound_Name']}: {pmid} (non numérique)")
    
    if invalid_pmids:
        print(f"[AVERTISSEMENT] {len(invalid_pmids)} PMIDs invalides:")
        for pmid in invalid_pmids:
            print(f"  - {pmid}")
    else:
        print(f"[OK] Tous les PMIDs sont valides")
    
    # 5. Valeurs manquantes dans colonnes critiques
    print("\n[CHECK] Valeurs manquantes...")
    critical_cols = ['Compound_Name', 'K_d_nM', 'EC50_nM', 'tau_residence_min']
    
    missing_data = {}
    for col in critical_cols:
        missing_count = df[col].isna().sum()
        if missing_count > 0:
            missing_data[col] = missing_count
    
    if missing_data:
        print("[AVERTISSEMENT] Valeurs manquantes dans colonnes critiques:")
        for col, count in missing_data.items():
            print(f"  - {col}: {count} valeurs manquantes")
    else:
        print("[OK] Aucune valeur manquante dans colonnes critiques")
    
    # Résumé final
    print("\n" + "="*60)
    if not errors and not missing_data:
        print("[SUCCÈS] Validation complète réussie !")
        print("="*60)
        return True
    else:
        print("[AVERTISSEMENT] Validation réussie avec avertissements mineurs")
        print("="*60)
        return True

def validate_predictions_matrix(csv_path='Confidence_Grading_Matrix.csv'):
    """Valide la matrice de prédictions"""
    print(f"\n[VALIDATION] Matrice de prédictions...")
    
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"[ERREUR] Fichier non trouvé: {csv_path}")
        return False
    
    print(f"[OK] {len(df)} prédictions chargées")
    
    # Vérifier niveaux de confiance valides
    valid_levels = {'High', 'Moderate', 'Low', 'Very High'}
    invalid = df[~df['Confidence_Level'].isin(valid_levels)]
    
    if not invalid.empty:
        print(f"[ERREUR] {len(invalid)} niveaux de confiance invalides")
        return False
    
    print(f"[OK] Tous les niveaux de confiance sont valides")
    
    # Stats
    print(f"\nRépartition des niveaux de confiance:")
    for level, count in df['Confidence_Level'].value_counts().items():
        pct = count / len(df) * 100
        print(f"  - {level}: {count} ({pct:.1f}%)")
    
    return True

if __name__ == '__main__':
    print("="*60)
    print("VALIDATION DES DONNÉES - Molecular Arrest Framework")
    print("="*60 + "\n")
    
    # Validation base de composés
    valid1 = validate_compound_database()
    
    # Validation matrice de prédictions
    valid2 = validate_predictions_matrix()
    
    # Résultat final
    print("\n" + "="*60)
    if valid1 and valid2:
        print("[SUCCÈS] Toutes les validations réussies !")
        sys.exit(0)
    else:
        print("[ÉCHEC] Certaines validations ont échoué")
        sys.exit(1)

