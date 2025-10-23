# 🚀 Actions à Faire MAINTENANT : Release v1.1.0
## Guide Ultra-Rapide (20 minutes)

**Projet :** Molecular Arrest Framework v1.1.0  
**Date :** 22 octobre 2025  
**Statut :** ✅ Tout est préparé, suivez ces étapes dans l'ordre

---

## ⚡ ÉTAPE 1 : Git Initial Setup (5 min)

Ouvrez PowerShell et exécutez :

```powershell
cd "C:\Users\tommy\Desktop\arrest molecules"

# Ajouter tous les fichiers
git add .

# Vérifier ce qui sera commité
git status

# Premier commit
git commit -m "feat: initial release v1.1.0 - Molecular Arrest Framework

- 10 paradigmatic compounds with full pharmacological data
- 44 testable predictions with confidence grading
- Monte Carlo uncertainty quantification (seed=42)
- FAIR² compliant data package
- 95+ literature sources (PubMed traceable)
- Complete documentation and reproducible code"
```

---

## ⚡ ÉTAPE 2 : Créer Repo GitHub (3 min)

### 2.1 Sur github.com
1. Allez sur https://github.com/new
2. Remplissez :
   - **Repository name:** `arrest-molecules`
   - **Description:** `Molecular Arrest Framework - Unifying theory for dampening compounds in biological regulation`
   - **Visibility:** ✅ **Public** (obligatoire pour Zenodo gratuit)
   - ❌ **NE PAS cocher** "Add a README", "Add .gitignore", "Choose a license"
3. Cliquez **"Create repository"**

### 2.2 Dans PowerShell
```powershell
# Connecter au repo distant
git remote add origin https://github.com/Mythmaker28/arrest-molecules.git

# Pousser le code
git push -u origin main
```

**✅ Vérifiez :** Votre code est maintenant visible sur https://github.com/Mythmaker28/arrest-molecules

---

## ⚡ ÉTAPE 3 : Activer Zenodo (2 min)

1. Allez sur **https://zenodo.org/**
2. Cliquez **"Log in"** → **"Log in with GitHub"**
3. En haut à droite, cliquez sur votre nom → **"GitHub"**
4. Cliquez sur **"Sync now"** (bouton vert)
5. Cherchez **`arrest-molecules`** dans la liste
6. **Activez le toggle** à droite du nom (doit devenir vert/ON)

**✅ Vérifiez :** Le toggle est vert avec mention "ON"

---

## ⚡ ÉTAPE 4 : Créer Release GitHub (5 min)

### 4.1 Sur github.com
1. Allez sur **https://github.com/Mythmaker28/arrest-molecules**
2. Cliquez sur **"Releases"** (colonne de droite sous "About")
3. Cliquez sur **"Draft a new release"**

### 4.2 Remplir le formulaire

**Tag version:**
```
v1.1.0
```
- GitHub va proposer "Create new tag: v1.1.0 on publish" → Cliquez dessus

**Target:**
```
main
```

**Release title:**
```
Molecular Arrest Framework v1.1.0
```

**Release notes:**
- Ouvrez le fichier `RELEASE_NOTES_v1.1.0.md` de votre projet
- **Copiez TOUT le contenu** (Ctrl+A, Ctrl+C)
- **Collez** dans le champ "Describe this release"

**Options en bas :**
- ❌ **NE PAS cocher** "Set as a pre-release"
- ✅ **Cocher** "Set as the latest release"

### 4.3 Publier
Cliquez sur **"Publish release"** (bouton vert)

**✅ Vérifiez :** Vous voyez la release sur https://github.com/Mythmaker28/arrest-molecules/releases/tag/v1.1.0

---

## ⚡ ÉTAPE 5 : Publier sur Zenodo (5 min)

### 5.1 Attendre la création (2-5 min)
1. Attendez quelques minutes (Zenodo traite automatiquement)
2. Allez sur **https://zenodo.org/account/settings/github/**
3. Vous devriez voir votre release en traitement ou prête

### 5.2 Finaliser l'enregistrement
1. Cliquez sur **`arrest-molecules`** → Redirige vers l'enregistrement Zenodo
2. **Vérifiez les métadonnées** (normalement déjà remplies via .zenodo.json) :
   - ✅ Titre correct
   - ✅ Auteur : Tommy Lepesteur
   - ✅ ORCID : 0009-0009-0577-9563
   - ✅ Licence : CC-BY 4.0
   - ✅ Type : Dataset
   - ✅ Keywords présents
3. Cliquez sur **"Publish"** (bouton bleu en haut à droite)

### 5.3 Récupérer les DOI
Après publication, Zenodo affiche :

**DOI de VERSION (spécifique à v1.1.0) :**
```
10.5281/zenodo.XXXXXXX  (exemple)
```

**Concept DOI (pointe toujours vers latest) :**
```
10.5281/zenodo.XXXXXX  (exemple - 1 chiffre de moins)
```

**⚠️ IMPORTANT :** Notez le **CONCEPT DOI** (pas celui de version)

**Badge fourni par Zenodo :**
Zenodo affiche aussi un badge Markdown/HTML → Copiez le **Markdown**

---

## ⚡ ÉTAPE 6 : Mettre à Jour avec DOI (5 min)

### 6.1 Modifier README.md

Ouvrez `README.md` et remplacez :

**Ligne 3 :**
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```
→ Remplacez `XXXXXXX` par votre **CONCEPT DOI**

**Ligne ~199 (section "For the dataset:") :**
```
https://doi.org/10.5281/zenodo.XXXXXXX
```
→ Remplacez `XXXXXXX` par votre **CONCEPT DOI**

**Lignes ~215-216 (BibTeX) :**
```bibtex
doi = {10.5281/zenodo.XXXXXXX},
url = {https://doi.org/10.5281/zenodo.XXXXXXX}
```
→ Remplacez `XXXXXXX` par votre **CONCEPT DOI**

### 6.2 Modifier CITATION.cff

Ouvrez `CITATION.cff` et remplacez :

**Ligne ~29 :**
```yaml
value: "10.5281/zenodo.XXXXXXX"
```
→ Remplacez `XXXXXXX` par votre **CONCEPT DOI**

**Ligne ~51 :**
```yaml
doi: "10.5281/zenodo.XXXXXXX"
```
→ Remplacez `XXXXXXX` par votre **CONCEPT DOI**

### 6.3 Commiter et Pousser

Dans PowerShell :
```powershell
git add README.md CITATION.cff
git commit -m "docs: add Zenodo DOI badges and citation info"
git push origin main
```

**✅ Vérifiez :** Le badge DOI s'affiche correctement sur GitHub

---

## ✅ CRITÈRES DE RÉUSSITE

### GitHub ✅
- [ ] Release v1.1.0 visible : https://github.com/Mythmaker28/arrest-molecules/releases/tag/v1.1.0
- [ ] Code source téléchargeable (ZIP + tar.gz automatiques)
- [ ] Notes de release formatées et complètes
- [ ] Badge "Latest release" visible dans sidebar

### Zenodo ✅
- [ ] Enregistrement publié : https://zenodo.org/record/XXXXXXX
- [ ] 2 DOI affichés (version + concept)
- [ ] Métadonnées complètes (titre, auteur, ORCID, licence, keywords)
- [ ] Badge DOI disponible

### README ✅
- [ ] Badge DOI s'affiche en haut (cliquable → redirige vers Zenodo)
- [ ] Section "How to Cite This Work" avec DOI réel
- [ ] BibTeX avec DOI réel
- [ ] Badge "Latest release" s'affiche

### Citation ✅
- [ ] CITATION.cff contient DOI réel
- [ ] GitHub affiche bouton **"Cite this repository"** (sidebar droite)

---

## 🎉 C'EST FINI !

**Votre projet est maintenant publié avec DOI Zenodo !**

### Partager
```
🎉 Molecular Arrest Framework v1.1.0 is now published!

📊 Dataset: 10 compounds, 44 predictions, 95+ sources
🔬 Fully reproducible (seed=42, explicit versions)
📖 Open access: CC-BY 4.0 (data) + MIT (code)

🔗 GitHub: https://github.com/Mythmaker28/arrest-molecules
📚 DOI: https://doi.org/10.5281/zenodo.[VOTRE_CONCEPT_DOI]

#OpenScience #FAIR #Pharmacology #Reproducibility
```

---

## 📞 EN CAS DE PROBLÈME

**Zenodo ne crée pas l'enregistrement :**
→ Attendez 10 min, Sync now, recréez la release si besoin

**Badge DOI ne s'affiche pas :**
→ Vérifiez l'URL (concept DOI, pas version), rafraîchissez (Ctrl+F5)

**Bouton "Cite this repository" absent :**
→ Vérifiez syntaxe CITATION.cff, attendez quelques minutes

**Autres problèmes :**
→ Consultez **GUIDE_RELEASE_GITHUB_ZENODO.md** (section Dépannage complète)

---

## 📚 FICHIERS DE RÉFÉRENCE

| Fichier | Usage |
|---------|-------|
| **ACTIONS_RELEASE_v1.1.0.md** | Ce guide (actions rapides) ⭐ |
| **GUIDE_RELEASE_GITHUB_ZENODO.md** | Guide détaillé complet |
| **RELEASE_NOTES_v1.1.0.md** | À copier dans GitHub release |
| **PRE_RELEASE_CHECKLIST.md** | Checklist de vérification |

---

**Guide créé le :** 22 octobre 2025  
**Temps total estimé :** 20-30 minutes  
**Difficulté :** ⭐ Facile (étapes claires)  
**Résultat :** 🎯 DOI Zenodo + Release GitHub professionnelle

