# Guide Complet : Release GitHub → Zenodo
## Molecular Arrest Framework v1.1.0

**Date :** 22 octobre 2025  
**Objectif :** Publier une release GitHub propre qui génère automatiquement les DOI Zenodo

---

## ✅ ÉTAT ACTUEL DU PROJET

### Vérifications de Sécurité ✅
- [x] **Aucun fichier secret** détecté (pas de .env, clés API, tokens)
- [x] **`.gitignore` configuré** - Notes personnelles exclues automatiquement
- [x] **Données sensibles** - Protocoles de synthèse sous contrôle d'accès (documenté)

### Fichiers Essentiels Présents ✅
- [x] **Manuscrit** - `v6.txt` (1,943 lignes) + `molecular_arrest_manuscript.docx`
- [x] **Données** - 10 composés, 44 prédictions, 95+ sources
- [x] **Code** - Python (Monte Carlo) + R (figures) + tests
- [x] **README.md** - Complet avec badge DOI (placé)
- [x] **LICENSE** - MIT + CC-BY 4.0 (dual license créée)
- [x] **CITATION.cff** - Métadonnées de citation GitHub
- [x] **`.zenodo.json`** - Configuration automatique Zenodo
- [x] **CONTRIBUTING.md** + **CODE_OF_CONDUCT.md**

### Fichiers Créés pour la Release ✅
1. ✅ `RELEASE_NOTES_v1.1.0.md` - Notes complètes pour GitHub
2. ✅ `LICENSE` - Dual license MIT + CC-BY 4.0
3. ✅ `CITATION.cff` - Format standard pour citations
4. ✅ `.zenodo.json` - Métadonnées Zenodo automatiques
5. ✅ `README.md` modifié - Badge DOI + section citation améliorée

---

## 📋 ÉTAPES POUR PUBLIER LA RELEASE

### ÉTAPE 1 : Préparer le Dépôt Git

#### 1.1 Vérifier le statut et la branche
```bash
cd "C:\Users\tommy\Desktop\arrest molecules"
git status
git branch
```

**Actions nécessaires :**
- Si pas sur `main` : `git checkout -b main` (créer branche main)
- Si des fichiers non trackés : voir étape 1.2

#### 1.2 Ajouter et committer les fichiers
```bash
# Ajouter TOUS les fichiers du projet (sauf ceux dans .gitignore)
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

#### 1.3 Connecter au repo GitHub distant
```bash
# Si le repo GitHub n'existe pas encore, créez-le d'abord sur github.com
# Nom: arrest-molecules
# Description: Molecular Arrest Framework - Unifying theory for dampening compounds
# Public
# NE PAS initialiser avec README (on a déjà tout)

# Ajouter le remote
git remote add origin https://github.com/Mythmaker28/arrest-molecules.git

# Vérifier
git remote -v

# Pousser le code
git push -u origin main
```

**⚠️ ATTENTION :** Si le repo existe déjà et a des commits, utilisez :
```bash
git pull origin main --allow-unrelated-histories
# Résolvez les conflits si nécessaire
git push origin main
```

---

### ÉTAPE 2 : Connecter GitHub à Zenodo

#### 2.1 Activer l'intégration Zenodo
1. Allez sur **https://zenodo.org/** et connectez-vous (ou créez un compte)
2. Cliquez sur votre nom en haut à droite → **GitHub**
3. Cliquez sur le bouton **"Sync now"** pour synchroniser vos repos
4. Cherchez **`arrest-molecules`** dans la liste
5. **Activez le toggle** à droite du repo

**Capture d'écran attendue :**
```
✓ arrest-molecules          [ON]  (toggle vert)
  Mythmaker28/arrest-molecules
```

#### 2.2 Vérifier la configuration
- Le fichier `.zenodo.json` à la racine sera automatiquement lu par Zenodo
- Vérifiez qu'il contient bien vos informations (déjà fait ✅)

---

### ÉTAPE 3 : Créer la Release GitHub

#### 3.1 Via l'interface GitHub
1. Allez sur **https://github.com/Mythmaker28/arrest-molecules**
2. Cliquez sur **"Releases"** (dans la colonne de droite)
3. Cliquez sur **"Draft a new release"**

#### 3.2 Remplir le formulaire de release

**Tag version:**
```
v1.1.0
```
- Cliquez sur **"Create new tag: v1.1.0 on publish"**

**Target:**
```
main
```

**Release title:**
```
Molecular Arrest Framework v1.1.0
```

**Release notes:**
Copiez-collez le contenu COMPLET de `RELEASE_NOTES_v1.1.0.md` (déjà préparé)

**Options :**
- [ ] ❌ **NE PAS cocher** "Set as a pre-release"
- [x] ✅ **Cocher** "Set as the latest release"

**Assets (fichiers attachés) :**
- **NE PAS ATTACHER** de fichiers manuellement
- Zenodo archive automatiquement tout le repo au tag `v1.1.0`

#### 3.3 Publier
Cliquez sur **"Publish release"**

✅ **La release est maintenant visible** sur GitHub !

---

### ÉTAPE 4 : Récupérer les DOI Zenodo

#### 4.1 Attendre la création (1-5 minutes)
1. Allez sur **https://zenodo.org/account/settings/github/**
2. Vous devriez voir votre release en cours de traitement
3. Après quelques minutes, cliquez sur le repo → vous serez redirigé vers l'enregistrement Zenodo

#### 4.2 Finaliser l'enregistrement Zenodo

**Vérifications avant publication :**

1. **Titre** ✅ (déjà rempli via `.zenodo.json`)
   ```
   Molecular Arrest Framework - Research Data Package v1.1.0
   ```

2. **Auteurs** ✅ (déjà rempli)
   - Tommy Lepesteur (ORCID: 0009-0009-0577-9563)
   - Marie Legrand (contributor, Data Curator)

3. **Description** ✅ (déjà remplie avec HTML formaté)

4. **Mots-clés** ✅ (déjà 15 keywords)

5. **Licence** ✅
   - Vérifiez : **CC-BY 4.0** (pour les données)

6. **Type d'upload** ✅
   - Vérifiez : **Dataset**

7. **Date de publication** ✅
   - 2025-10-22

**Si tout est correct, cliquez sur "Publish"**

#### 4.3 Récupérer les 2 DOI

Après publication, Zenodo affiche :

**1. DOI de VERSION (spécifique à v1.1.0) :**
```
10.5281/zenodo.1234567  (exemple)
```

**2. DOI de CONCEPT (pointe toujours vers la dernière version) :**
```
10.5281/zenodo.1234566  (exemple - toujours -1 du DOI de version)
```

**Badge DOI :**
Zenodo fournit aussi un badge :
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234566.svg)](https://doi.org/10.5281/zenodo.1234566)
```

---

### ÉTAPE 5 : Mettre à Jour GitHub avec les DOI

#### 5.1 Modifier le README.md

Remplacez `XXXXXXX` par le **concept DOI** (pas le DOI de version) :

**Ligne 3 du README.md :**
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```
→
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234566.svg)](https://doi.org/10.5281/zenodo.1234566)
```

**Section "How to Cite This Work" (ligne ~195) :**
```
https://doi.org/10.5281/zenodo.XXXXXXX
```
→
```
https://doi.org/10.5281/zenodo.1234566
```

**BibTeX :**
```bibtex
doi = {10.5281/zenodo.XXXXXXX}
```
→
```bibtex
doi = {10.5281/zenodo.1234566}
```

#### 5.2 Modifier CITATION.cff

Remplacez dans `CITATION.cff` (ligne 29 et 51) :
```yaml
value: "10.5281/zenodo.XXXXXXX"
```
→
```yaml
value: "10.5281/zenodo.1234566"
```

#### 5.3 Committer et pousser
```bash
git add README.md CITATION.cff
git commit -m "docs: add Zenodo DOI badges and citation info"
git push origin main
```

---

### ÉTAPE 6 : Modifier la Release GitHub (Optionnel)

Si vous voulez ajouter le badge DOI dans les notes de release :

1. Allez sur **https://github.com/Mythmaker28/arrest-molecules/releases**
2. Cliquez sur **"Edit"** pour la release v1.1.0
3. Modifiez la première ligne :
   ```markdown
   [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
   ```
   →
   ```markdown
   [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234566.svg)](https://doi.org/10.5281/zenodo.1234566)
   ```
4. Cliquez sur **"Update release"**

---

## ✅ CRITÈRES DE RÉUSSITE

### 1. GitHub ✅
- [ ] Release **v1.1.0** visible sur https://github.com/Mythmaker28/arrest-molecules/releases
- [ ] Titre : "Molecular Arrest Framework v1.1.0"
- [ ] Notes de release complètes et formatées
- [ ] Tag `v1.1.0` créé
- [ ] Code source téléchargeable (.zip et .tar.gz)

### 2. Zenodo ✅
- [ ] Enregistrement publié : https://zenodo.org/record/XXXXXXX
- [ ] **2 DOI visibles :**
  - DOI de version (10.5281/zenodo.XXXXXXX)
  - Concept DOI (10.5281/zenodo.XXXXXX)
- [ ] Métadonnées complètes (titre, auteur, ORCID, licence, keywords)
- [ ] Licence : **CC-BY 4.0**
- [ ] Type : **Dataset**

### 3. README ✅
- [ ] Badge DOI en haut (avec concept DOI)
- [ ] Section "How to Cite This Work" avec DOI
- [ ] BibTeX avec DOI
- [ ] Instructions claires sur concept DOI vs version DOI

### 4. Citation ✅
- [ ] `CITATION.cff` avec DOI Zenodo
- [ ] GitHub affiche automatiquement "Cite this repository" (bouton dans sidebar)

---

## 📊 APRÈS LA RELEASE

### Monitoring
- **GitHub Insights** : Clones, visits, stars
- **Zenodo Stats** : Downloads, views, citations
- **DOI résolution** : Tester que le DOI redirige bien vers Zenodo

### Communication
- Partager le DOI sur :
  - Twitter/X scientifique
  - ResearchGate
  - LinkedIn
  - Communautés pharmacologie/psychédéliques
  
### Mises à jour futures
Pour v1.2, v2.0, etc. :
1. Faire les modifications
2. Commit + push
3. Créer nouvelle release (v1.2.0, v2.0.0...)
4. Zenodo crée automatiquement un **nouveau DOI de version**
5. Le **concept DOI reste le même** (pointe vers latest)

---

## 🆘 DÉPANNAGE

### Problème : Zenodo ne détecte pas la release
**Solution :**
1. Vérifiez que le toggle est bien activé sur https://zenodo.org/account/settings/github/
2. Cliquez sur "Sync now"
3. Attendez 5-10 minutes
4. Si toujours rien, créez une nouvelle release (v1.1.1)

### Problème : .zenodo.json non pris en compte
**Solution :**
1. Vérifiez la syntaxe JSON (pas de virgule finale, guillemets corrects)
2. Le fichier DOIT être à la racine du repo
3. Recréez la release si le fichier était absent au moment de la release

### Problème : DOI ne s'affiche pas sur GitHub
**Solution :**
- Le badge s'affiche seulement après commit + push du README modifié
- Vérifiez l'URL du badge (doit être le concept DOI, pas version)
- Rafraîchissez le cache du navigateur (Ctrl+F5)

### Problème : CITATION.cff non reconnu
**Solution :**
- Vérifiez la syntaxe YAML (indentation = 2 espaces, pas de tabs)
- Le bouton "Cite this repository" apparaît après quelques minutes
- Pushez une modification mineure pour forcer la mise à jour GitHub

---

## 📞 AIDE SUPPLÉMENTAIRE

- **Documentation Zenodo-GitHub** : https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
- **Zenodo Support** : https://zenodo.org/support
- **CITATION.cff Validator** : https://citation-file-format.github.io/cff-initializer-javascript/

---

## ✅ CHECKLIST FINALE

Avant de considérer la tâche terminée :

- [ ] Release GitHub publiée et visible
- [ ] Zenodo enregistrement publié avec 2 DOI
- [ ] README.md contient badge DOI (concept)
- [ ] CITATION.cff contient DOI
- [ ] Section "How to Cite" complète avec BibTeX
- [ ] Test : Le DOI redirige bien vers Zenodo
- [ ] Test : Le badge DOI s'affiche correctement
- [ ] Test : GitHub affiche "Cite this repository"
- [ ] Optionnel : Notes de release modifiées avec DOI

---

**Guide créé le :** 22 octobre 2025  
**Projet :** Molecular Arrest Framework v1.1.0  
**Mainteneur :** Tommy Lepesteur  
**Prêt pour publication !** 🚀

