#!/usr/bin/env python3
"""
Détection des fichiers dupliqués dans le projet
Utile pour nettoyer et éviter la redondance
"""

import hashlib
import json
from pathlib import Path
from collections import defaultdict

def compute_sha1(filepath):
    """Calcule le hash SHA1 d'un fichier"""
    sha1 = hashlib.sha1()
    with open(filepath, 'rb') as f:
        while True:
            data = f.read(65536)  # 64kb chunks
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def find_duplicates(root_dir='.', exclude_dirs=None):
    """
    Trouve tous les fichiers dupliqués (même contenu)
    
    Args:
        root_dir: Répertoire racine à scanner
        exclude_dirs: Liste de répertoires à exclure
    
    Returns:
        dict: {sha1: [list of file paths]}
    """
    if exclude_dirs is None:
        exclude_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'venv'}
    
    file_hashes = defaultdict(list)
    root_path = Path(root_dir).resolve()
    
    print(f"[SCAN] Scan des fichiers dans {root_path}...")
    
    for filepath in root_path.rglob('*'):
        # Skip directories et fichiers exclus
        if filepath.is_dir():
            continue
        
        # Skip si dans un répertoire exclu
        if any(excluded in filepath.parts for excluded in exclude_dirs):
            continue
        
        # Skip fichiers trop gros (>50MB)
        try:
            if filepath.stat().st_size > 50 * 1024 * 1024:
                print(f"[SKIP] Fichier >50MB: {filepath.relative_to(root_path)}")
                continue
        except:
            continue
        
        # Calculer hash
        try:
            sha1 = compute_sha1(filepath)
            rel_path = str(filepath.relative_to(root_path))
            file_hashes[sha1].append(rel_path)
        except Exception as e:
            print(f"[ERREUR] Lecture {filepath}: {e}")
    
    return file_hashes

def generate_report(file_hashes, output_file='REPORT_DUPLICATES.md'):
    """Génère un rapport Markdown des doublons trouvés"""
    
    # Filtrer pour ne garder que les vrais doublons (>1 fichier)
    duplicates = {sha1: files for sha1, files in file_hashes.items() if len(files) > 1}
    
    if not duplicates:
        print("[OK] Aucun doublon detecte !")
        return
    
    total_duplicates = sum(len(files) - 1 for files in duplicates.values())
    total_groups = len(duplicates)
    
    print(f"\n[RESULTAT] {total_duplicates} fichiers dupliques trouves dans {total_groups} groupes\n")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Rapport des Fichiers Dupliqués\n\n")
        f.write(f"**Date :** {Path.cwd()}\n\n")
        f.write(f"**Résumé :** {total_duplicates} doublons dans {total_groups} groupes\n\n")
        f.write("---\n\n")
        
        for i, (sha1, files) in enumerate(sorted(duplicates.items(), key=lambda x: -len(x[1])), 1):
            files_sorted = sorted(files)
            
            f.write(f"## Groupe {i} - {len(files)} copies\n\n")
            f.write(f"**SHA1:** `{sha1}`\n\n")
            f.write(f"**Fichier canonique suggéré:** `{files_sorted[0]}`\n\n")
            f.write("**Copies à supprimer:**\n")
            for filepath in files_sorted[1:]:
                f.write(f"- `{filepath}`\n")
            f.write("\n")
            
            # Calculer taille économisée
            try:
                size = Path(files_sorted[0]).stat().st_size
                saved = size * (len(files) - 1)
                if saved > 1024*1024:
                    f.write(f"**Économie potentielle:** {saved / (1024*1024):.2f} MB\n\n")
                elif saved > 1024:
                    f.write(f"**Économie potentielle:** {saved / 1024:.2f} KB\n\n")
                else:
                    f.write(f"**Économie potentielle:** {saved} bytes\n\n")
            except:
                pass
            
            f.write("---\n\n")
    
    print(f"[OK] Rapport genere : {output_file}")
    
    # Aussi générer JSON pour traitement automatique
    json_output = output_file.replace('.md', '.json')
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(duplicates, f, indent=2)
    print(f"[OK] JSON genere : {json_output}")

if __name__ == '__main__':
    import sys
    import io
    # Fix pour Windows encoding
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("=" * 60)
    print("Detection des fichiers dupliques")
    print("=" * 60)
    
    file_hashes = find_duplicates()
    generate_report(file_hashes)
    
    print("\nScan termine")

