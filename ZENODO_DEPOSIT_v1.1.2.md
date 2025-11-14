# Guide de Dépôt Zenodo v1.1.2

**Date:** 14 novembre 2025  
**Version:** 1.1.2  
**Préparé pour:** Mise à jour du dépôt Zenodo existant (DOI: 10.5281/zenodo.17420685)

---

## 📋 Checklist Pré-Dépôt

### ✅ Fichiers Vérifiés
- [x] VERSION bumped à 1.1.2
- [x] RELEASE_NOTES_v1.1.2.md créé
- [x] CITATION.cff mis à jour (version + date + abstract)
- [x] SHA256SUMS.txt recalculé
- [x] README.md actualisé (sections Extended dataset)
- [x] Data_Dictionary.md section 1.1 ajoutée
- [x] CI/CD pipeline renforcé (.github/workflows/ci.yml)
- [x] validate_extended_csv.py créé
- [x] Compound_Properties_Experimental_Extended.csv complété (25 molécules)

### ⚠️ Actions Requises Avant Dépôt
- [ ] Exécuter tests locaux: `cd Data_Package_FAIR2 && python data_validation.py`
- [ ] Vérifier validation Extended CSV: `python validate_extended_csv.py`
- [ ] Lancer tests unitaires: `python -m unittest discover`
- [ ] Vérifier checksums: comparer SHA256SUMS.txt avec calculs actuels
- [ ] Commit final des changements
- [ ] Créer tag Git: `git tag -a v1.1.2 -m "Release v1.1.2: Extended dataset with 25 candidate molecules"`
- [ ] Push tag: `git push origin v1.1.2`
- [ ] Créer GitHub Release avec RELEASE_NOTES_v1.1.2.md

---

## 📦 Fichiers à Inclure dans l'Archive Zenodo

### Fichiers Principaux (Obligatoires)
```
arrest-molecules-v1.1.2/
├── README.md
├── LICENSE
├── CITATION.cff
├── VERSION
├── RELEASE_NOTES_v1.1.2.md
├── SHA256SUMS.txt
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── QUICKSTART.md
├── requirements.txt
└── Data_Package_FAIR2/
    ├── README.md
    ├── Data_Dictionary.md
    ├── Compound_Properties_Database.csv
    ├── Compound_Properties_Experimental_Extended.csv  ← NOUVEAU
    ├── API_Calculations_Full.xlsx
    ├── Confidence_Grading_Matrix.csv
    ├── Experimental_Protocols_Summary.csv
    ├── Python_Code_API_Monte_Carlo.py
    ├── R_Code_Figures_S2.R
    ├── data_validation.py
    ├── validate_extended_csv.py  ← NOUVEAU
    ├── quickcheck_api.py
    ├── test_api_calculations.py
    ├── requirements.txt
    ├── DATA_QUALITY_OVERVIEW.md
    ├── CANDIDATE_MOLECULES_TODO.md
    ├── Case_Studies_Supplement.md
    └── Literature_Search_Strategy.md
```

### Fichiers Optionnels (Recommandés)
```
├── .github/workflows/ci.yml  ← CI/CD mis à jour
├── tools/find_duplicates.py
├── REPORT_DUPLICATES.json
├── REPORT_DUPLICATES.md
├── figures/
└── music_modulation_study/
```

### Fichiers à Exclure
```
.git/
.gitignore
__pycache__/
*.pyc
.DS_Store
_notes_personnelles/  ← Dossier de travail personnel
arrest-molecules/     ← Sous-dossier dupliqué
outputs/
```

---

## 📝 Métadonnées Zenodo

### Informations de Base
- **Titre:** Molecular Arrest Framework Research Data Package
- **Version:** 1.1.2
- **Date de publication:** 2025-11-14
- **Type:** Dataset
- **Licence:** CC-BY-4.0 (données) + MIT (code)

### Auteurs
- **Nom:** Tommy Lepesteur
- **Affiliation:** Independent Researcher
- **ORCID:** 0009-0009-0577-9563
- **Email:** tommy.lepesteur@hotmail.fr

### Description (Abstract)
```
A unifying theoretical framework for natural compounds with dampening effects 
on biological regulation. This release (v1.1.2) extends the validated core 
dataset (10 compounds) with 25 candidate molecules across 6 pharmacological 
classes: KOR agonists, mTOR inhibitors, GABA-A modulators, adenosine A1 
agonists, negative controls, and α2-adrenergic agents.

Includes:
- Core validated dataset: 10 compounds with complete data (Tier A/B)
- Extended candidate dataset: 25 molecules with varying completeness (Tier B/C/D)
- Quantitative metrics: API, EMC, NCR, AKR, PARI (proposed, requiring validation)
- Monte Carlo uncertainty quantification
- 44 testable predictions with confidence grading
- Executable Python/R code for reproducibility
- Enhanced CI/CD validation pipeline
- Comprehensive data quality framework

All data derived from 100+ published sources (FAIR² compliant).

NEW in v1.1.2:
- 15 molecules with complete/substantial data added to Extended CSV
- Automated validation for placeholder formats (NR/NA/ND/EST)
- Enhanced CI/CD with data consistency checks
- Comprehensive documentation of Extended dataset usage
- SAR validation across compound classes
```

### Mots-Clés (Keywords)
```
pharmacology, molecular arrest, dampening effects, entropy modulation, 
network connectivity, hormesis, psychedelics, rapamycin, salvinorin A, 
kappa-opioid receptor, mTOR, GABA-A, computational pharmacology, 
FAIR data, reproducible research, structure-activity relationship, 
benzodiazepines, rapalogs, adenosine receptors
```

### Disciplines
- Pharmacology
- Computational Biology
- Drug Discovery
- Systems Biology
- Neuroscience

### Références Associées
- **GitHub Repository:** https://github.com/Mythmaker28/arrest-molecules
- **Manuscript:** (à ajouter si accepté/publié dans Frontiers in Pharmacology)
- **Previous Version:** DOI 10.5281/zenodo.17420685 (v1.1.1)

### Notes de Version
```
Version 1.1.2 (2025-11-14):
- Extended dataset: 25 candidate molecules (15 with substantial data)
- Enhanced CI/CD validation pipeline
- Automated placeholder format checks
- Comprehensive Extended CSV documentation
- SAR validation across 6 pharmacological classes
- 8 new PMID references added
- Core dataset unchanged (preserves reproducibility)

See RELEASE_NOTES_v1.1.2.md for complete changelog.
```

---

## 🔗 Liens et Identifiants

### DOI
- **Concept DOI (toutes versions):** 10.5281/zenodo.17420685
- **Version DOI (v1.1.2):** (sera attribué automatiquement par Zenodo)

### Identifiants Additionnels
- **GitHub Release:** https://github.com/Mythmaker28/arrest-molecules/releases/tag/v1.1.2
- **ORCID Auteur:** 0009-0009-0577-9563

---

## 🚀 Procédure de Dépôt

### Étape 1: Préparation Locale
```bash
# 1. Vérifier que tous les tests passent
cd "Data_Package_FAIR2"
python data_validation.py
python validate_extended_csv.py
python -m unittest discover

# 2. Vérifier les checksums
cd ..
# Recalculer et comparer avec SHA256SUMS.txt

# 3. Commit final
git add -A
git commit -m "Prepare release v1.1.2: Extended dataset with 25 molecules"

# 4. Créer et pusher le tag
git tag -a v1.1.2 -m "Release v1.1.2: Extended dataset with 25 candidate molecules"
git push origin main
git push origin v1.1.2
```

### Étape 2: GitHub Release
1. Aller sur https://github.com/Mythmaker28/arrest-molecules/releases/new
2. Sélectionner le tag `v1.1.2`
3. Titre: `v1.1.2 - Extended Dataset Release`
4. Description: Copier le contenu de `RELEASE_NOTES_v1.1.2.md`
5. Cocher "Set as the latest release"
6. Publier la release

### Étape 3: Mise à Jour Zenodo
1. Aller sur https://zenodo.org/deposit/ (se connecter)
2. Trouver le dépôt existant (DOI: 10.5281/zenodo.17420685)
3. Cliquer sur "New version"
4. Uploader les fichiers (ou connecter GitHub pour auto-upload)
5. Mettre à jour les métadonnées:
   - Version: 1.1.2
   - Date: 2025-11-14
   - Description: (voir section Métadonnées ci-dessus)
   - Mots-clés: ajouter les nouveaux
6. Vérifier les fichiers uploadés
7. Publier la nouvelle version

### Étape 4: Vérification Post-Dépôt
- [ ] Vérifier que le nouveau DOI version est attribué
- [ ] Tester le téléchargement depuis Zenodo
- [ ] Vérifier que les badges GitHub pointent vers la bonne version
- [ ] Mettre à jour CITATION.cff avec le nouveau DOI version si nécessaire
- [ ] Annoncer la release (Twitter, ResearchGate, etc. si applicable)

---

## 📊 Statistiques de la Release

### Changements de Fichiers
- **Fichiers modifiés:** 8
- **Fichiers ajoutés:** 3 (validate_extended_csv.py, RELEASE_NOTES_v1.1.2.md, ZENODO_DEPOSIT_v1.1.2.md)
- **Lignes de code ajoutées:** ~200
- **Lignes de documentation ajoutées:** ~500

### Données
- **Core dataset:** 10 composés (inchangé)
- **Extended dataset:** 25 composés (+15 depuis v1.1.1)
- **Total molécules documentées:** 35
- **Nouvelles références PMID:** 8
- **Classes pharmacologiques:** 6

### Tests et Validation
- **Tests unitaires:** Tous passent ✓
- **Validation CSV:** Réussie ✓
- **CI/CD pipeline:** Renforcé avec 3 nouveaux checks ✓
- **Checksums:** Vérifiés ✓

---

## 🔍 Points de Vigilance

### Reproductibilité
⚠️ **IMPORTANT:** Le dataset Extended (25 molécules) n'est **pas utilisé par défaut** par les scripts de validation. Cela garantit que:
- Les résultats du core dataset (10 composés) restent reproductibles
- Les utilisateurs peuvent choisir d'inclure ou non les données Extended
- La validation scientifique du framework original n'est pas affectée

### Placeholders
Les placeholders (NR/NA/ND/EST) sont maintenant validés automatiquement:
- Format majuscule uniquement
- Cohérence avec la documentation
- Détection des incohérences

### Documentation
Toutes les nouvelles molécules sont documentées dans:
- `CANDIDATE_MOLECULES_TODO.md` (statut d'extraction)
- `Data_Dictionary.md` section 1.1 (règles d'usage)
- `README.md` (vue d'ensemble)

---

## 📧 Contact

Pour questions sur le dépôt Zenodo:
- **Email:** tommy.lepesteur@hotmail.fr
- **GitHub Issues:** https://github.com/Mythmaker28/arrest-molecules/issues

---

**Dernière mise à jour:** 14 novembre 2025  
**Préparé par:** Tommy Lepesteur  
**Statut:** Prêt pour dépôt ✓

