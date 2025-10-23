# Checklist Pré-Release v1.1.0
## Vérification Finale Avant Publication GitHub/Zenodo

**Date :** 22 octobre 2025  
**Version :** v1.1.0  
**Projet :** Molecular Arrest Framework

---

## 🔒 SÉCURITÉ ET CONFORMITÉ

### Fichiers Sensibles
- [x] ✅ **Aucun fichier .env** détecté
- [x] ✅ **Aucune clé API** ou token présent
- [x] ✅ **Aucun mot de passe** dans le code
- [x] ✅ **`.gitignore` configuré** (notes personnelles exclues)
- [x] ✅ **Protocoles sensibles** documentés avec accès contrôlé

### Conformité Légale
- [x] ✅ **Licences claires** - MIT (code) + CC-BY 4.0 (data)
- [x] ✅ **Fichier LICENSE** créé avec dual license
- [x] ✅ **Headers de licence** dans code Python/R
- [x] ✅ **Avertissement dual-use** documenté (Section 4.4.5 manuscrit)
- [x] ✅ **Pas de données personnelles** ou protégées

---

## 📁 FICHIERS ESSENTIELS

### Documentation Principale
- [x] ✅ **README.md** - Complet avec badge DOI préparé
- [x] ✅ **LICENSE** - Dual MIT + CC-BY 4.0
- [x] ✅ **CITATION.cff** - Métadonnées citation GitHub
- [x] ✅ **CONTRIBUTING.md** - Guide de contribution
- [x] ✅ **CODE_OF_CONDUCT.md** - Standards communauté
- [x] ✅ **.gitignore** - Exclusions appropriées

### Fichiers Release Spécifiques
- [x] ✅ **RELEASE_NOTES_v1.1.0.md** - Notes complètes (prêtes à copier)
- [x] ✅ **.zenodo.json** - Configuration Zenodo automatique
- [x] ✅ **GUIDE_RELEASE_GITHUB_ZENODO.md** - Instructions étape par étape
- [x] ✅ **PRE_RELEASE_CHECKLIST.md** - Ce fichier

### Manuscrit
- [x] ✅ **v6.txt** - Version texte complète (1,943 lignes)
- [x] ✅ **molecular_arrest_manuscript.docx** - Version Word

### Data Package FAIR²
- [x] ✅ **Compound_Properties_Database.csv** - 10 composés × 36 paramètres
- [x] ✅ **Confidence_Grading_Matrix.csv** - 44 prédictions
- [x] ✅ **API_Calculations_Full.xlsx** - Calculs détaillés
- [x] ✅ **Experimental_Protocols_Summary.csv** - 3 expériences
- [x] ✅ **Case_Studies_Supplement.md** - 5 études de cas
- [x] ✅ **Data_Dictionary.md** - Dictionnaire complet
- [x] ✅ **Literature_Search_Strategy.md** - Stratégie PRISMA
- [x] ✅ **Data_Package_FAIR2/README.md** - Documentation package

### Code & Scripts
- [x] ✅ **Python_Code_API_Monte_Carlo.py** - Script principal (v1.1)
- [x] ✅ **test_api_calculations.py** - Tests unitaires
- [x] ✅ **R_Code_Figures_S2.R** - Visualisations
- [x] ✅ **requirements.txt** - Dépendances Python (v1.1.0)

### Suppléments
- [x] ✅ **Figures_Supplementaires.txt** - Spécifications figures
- [x] ✅ **figures/** - Drafts figures S1-S3 (PNG + TIFF)

---

## ✅ COHÉRENCE DES DONNÉES

### Nombres et Versions
- [x] ✅ **44 prédictions** partout (harmonisé)
- [x] ✅ **10 composés** partout (harmonisé)
- [x] ✅ **Version v1.1 / v1.1.0** cohérente
- [x] ✅ **95+ sources** littéraires documentées
- [x] ✅ **Dates cohérentes** (2025-10-21/22)

### URLs et Contacts
- [x] ✅ **URL unique GitHub** : `Mythmaker28/arrest-molecules`
- [x] ✅ **Email unique** : `tommy.lepesteur@hotmail.fr`
- [x] ✅ **ORCID** : `0009-0009-0577-9563` (à confirmer avant Zenodo)

### Métadonnées
- [x] ✅ **Auteur principal** : Tommy Lepesteur
- [x] ✅ **Contributrice** : Dr. Marie Legrand (Data Curator)
- [x] ✅ **Affiliation** : Independent Researcher, Rennes, France
- [x] ✅ **Keywords** : 15 mots-clés dans .zenodo.json

---

## 🔬 QUALITÉ SCIENTIFIQUE

### Reproductibilité
- [x] ✅ **Seed fixe** : seed=42 dans code Python (documenté)
- [x] ✅ **Versions logiciels** : Python 3.8+, R 4.0+
- [x] ✅ **Versions packages** : numpy 1.24.3, pandas 2.0.3, etc.
- [x] ✅ **Databases externes** : ChEMBL v31, DrugBank 5.1.10 (versionnées)

### Traçabilité
- [x] ✅ **PMIDs présents** pour tous les paramètres pharmacologiques
- [x] ✅ **Sources documentées** dans CSV (colonne K_i_Source_PMID, etc.)
- [x] ✅ **Méthodes explicites** : Monte Carlo 10,000 iterations
- [x] ✅ **Contrôle qualité** : τ = 1/k_off ±5% documenté

### Prédictions
- [x] ✅ **44 prédictions stratifiées** : High (41%), Moderate (30%), Low (30%)
- [x] ✅ **Critères validation** clairs pour chaque prédiction
- [x] ✅ **Intervalles confiance** 95% pour tous les APIs

---

## 📊 VÉRIFICATIONS TECHNIQUES

### Git
```bash
# À exécuter avant release
cd "C:\Users\tommy\Desktop\arrest molecules"
git status                    # Devrait montrer fichiers à commiter
git branch                    # Devrait être sur 'main'
git remote -v                 # Devrait montrer origin = Mythmaker28/arrest-molecules
```

### Fichiers à Commiter (Premier Commit)
- [x] Tous les fichiers du projet (sauf _notes_personnelles/ exclus par .gitignore)
- [x] .zenodo.json
- [x] CITATION.cff
- [x] LICENSE
- [x] RELEASE_NOTES_v1.1.0.md
- [x] GUIDE_RELEASE_GITHUB_ZENODO.md
- [x] PRE_RELEASE_CHECKLIST.md
- [x] README.md (avec badge DOI)

### Taille du Repo
```bash
# Vérifier la taille totale
du -sh "C:\Users\tommy\Desktop\arrest molecules"
# Si > 100 MB, vérifier qu'il n'y a pas de binaires inutiles
```

**Attendu :** < 50 MB (principalement texte, CSV, code)

---

## 🎯 ACTIONS AVANT RELEASE

### 1. Initialiser Git (si pas encore fait)
```bash
cd "C:\Users\tommy\Desktop\arrest molecules"
git init
git branch -M main
```

### 2. Premier Commit
```bash
git add .
git status  # Vérifier
git commit -m "feat: initial release v1.1.0 - Molecular Arrest Framework

- 10 paradigmatic compounds with full pharmacological data
- 44 testable predictions with confidence grading
- Monte Carlo uncertainty quantification (seed=42)
- FAIR² compliant data package
- 95+ literature sources (PubMed traceable)
- Complete documentation and reproducible code"
```

### 3. Créer Repo GitHub
1. Aller sur https://github.com/new
2. **Repository name:** `arrest-molecules`
3. **Description:** `Molecular Arrest Framework - Unifying theory for dampening compounds in biological regulation`
4. **Public** (obligatoire pour Zenodo gratuit)
5. **NE PAS** initialiser avec README/LICENSE/gitignore (on a déjà tout)
6. Créer

### 4. Connecter et Pousser
```bash
git remote add origin https://github.com/Mythmaker28/arrest-molecules.git
git push -u origin main
```

### 5. Activer Zenodo
1. https://zenodo.org/ → Login
2. Nom utilisateur → GitHub
3. Sync now
4. Trouver `arrest-molecules` → Activer toggle

### 6. Créer Release GitHub
1. https://github.com/Mythmaker28/arrest-molecules/releases
2. "Draft a new release"
3. **Tag:** `v1.1.0` (créer nouveau tag)
4. **Target:** `main`
5. **Title:** `Molecular Arrest Framework v1.1.0`
6. **Description:** Copier tout RELEASE_NOTES_v1.1.0.md
7. **NE PAS cocher** "pre-release"
8. **Publish release**

### 7. Finaliser Zenodo (attendre 5 min)
1. https://zenodo.org/account/settings/github/
2. Cliquer sur le repo → Edit
3. Vérifier métadonnées (déjà remplies via .zenodo.json)
4. **Publish** pour obtenir DOI

### 8. Mettre à Jour avec DOI
```bash
# Modifier README.md et CITATION.cff avec DOI réel
# Exemple: remplacer XXXXXXX par le concept DOI (ex: 1234566)

git add README.md CITATION.cff
git commit -m "docs: add Zenodo DOI badges and citation info"
git push origin main
```

---

## ✅ CRITÈRES DE RÉUSSITE

### GitHub
- [ ] Release v1.1.0 visible
- [ ] Code source téléchargeable (zip + tar.gz)
- [ ] Release notes formatées correctement
- [ ] Badge release dans README

### Zenodo
- [ ] 2 DOI créés (version + concept)
- [ ] Enregistrement publié
- [ ] Métadonnées complètes
- [ ] Licence CC-BY 4.0
- [ ] Type: Dataset

### Documentation
- [ ] Badge DOI en haut du README
- [ ] Section "How to Cite" avec BibTeX
- [ ] CITATION.cff avec DOI
- [ ] GitHub affiche "Cite this repository"

---

## 🚦 ÉTAT FINAL

**PRÊT POUR RELEASE :** ✅ OUI

- ✅ Tous les fichiers essentiels présents
- ✅ Aucun secret ou donnée sensible
- ✅ Documentation complète et cohérente
- ✅ Métadonnées Zenodo préparées
- ✅ Notes de release rédigées
- ✅ Guide étape par étape créé

**ACTIONS MANUELLES REQUISES :**
1. Initialiser/connecter Git repo
2. Créer repo GitHub
3. Pousser le code
4. Activer Zenodo
5. Créer release GitHub
6. Publier sur Zenodo
7. Mettre à jour README avec DOI

**TEMPS ESTIMÉ :** 20-30 minutes (en suivant GUIDE_RELEASE_GITHUB_ZENODO.md)

---

**Checklist vérifiée le :** 22 octobre 2025  
**Projet :** Molecular Arrest Framework v1.1.0  
**Status :** 🚀 **PRÊT POUR LANCEMENT**

