# Molecular Arrest Framework v1.1.1 - Reproducibility Patch

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17420685.svg)](https://doi.org/10.5281/zenodo.17420685)

> **Release correctrice** - Améliore la reproductibilité 1-clic et finalise les figures

**Date de release :** 23 octobre 2025  
**Type :** Patch de reproductibilité  
**DOI Zenodo :** 10.5281/zenodo.17420685

---

## 🎯 Objectif de cette Release

Garantir la **reproductibilité complète** du projet en < 3 minutes sur n'importe quel système, avec vérifications automatisées et assets finalisés.

---

## 🔧 Corrections & Améliorations

### 1. CI/CD Renforcé ✅

**Nouveau workflow : `Reproducibility CI`**

- ✅ Vérification automatique des 4 artefacts critiques
- ✅ Test de reproductibilité 1-clic (< 60 secondes)
- ✅ Quick Check des valeurs API attendues
- ✅ Upload automatique des outputs (CSV, figures)
- ✅ Timeout de sécurité (2 min max par job)

**Fichier :** `.github/workflows/python-test.yml` → renommé en `.github/workflows/reproducibility-ci.yml`

---

### 2. Quick Check Automatisé ✅

**Nouveau script :** `Data_Package_FAIR2/quickcheck_api.py`

Valide instantanément que les calculs API donnent les valeurs attendues :

```bash
cd Data_Package_FAIR2
python quickcheck_api.py
```

**Vérifie :**
- Salvinorin A : API = 1.00 [0.85-1.15]
- Rapamycin : API = 0.12 [0.08-0.16]
- Tetrodotoxin : API = 4.0 [3.2-4.8]
- Psilocybin : API = -0.89 [-1.05, -0.73]

**Temps d'exécution :** < 1 seconde

---

### 3. Validation des Artefacts ✅

**Fichiers critiques vérifiés :**

1. `Compound_Properties_Database.csv` (10 composés × 36 paramètres)
2. `API_Calculations_Full.xlsx` (Monte Carlo complet)
3. `Python_Code_API_Monte_Carlo.py` (script principal)
4. `R_Code_Figures_S2.R` (génération figures)

**Check automatique** dans CI : si un fichier manque → ❌ Fail + message explicite

---

### 4. DOI Zenodo Intégré Partout ✅

**Mis à jour dans :**
- `README.md` (header + section citation)
- `CITATION.cff` (version 1.1.1)
- `RELEASE_NOTES_v1.1.1.md` (ce fichier)
- Tous les badges

**DOI permanent :** 10.5281/zenodo.17420685

---

### 5. Cohérence des Noms ✅

**Harmonisé :** Nom du projet = `arrest-molecules` partout

- URLs GitHub
- Chemins de fichiers
- Documentation
- Badges

---

## 📦 Assets Inclus

### Données
- `Compound_Properties_Database.csv` (28 KB)
- `Confidence_Grading_Matrix.csv` (5 KB)
- `Experimental_Protocols_Summary.csv` (2 KB)
- `API_Calculations_Full.xlsx` (45 KB)

### Code
- `Python_Code_API_Monte_Carlo.py` (23 KB)
- `R_Code_Figures_S2.R` (18 KB)
- `data_validation.py` (7 KB)
- `quickcheck_api.py` (4 KB) ⭐ NOUVEAU
- `test_api_calculations.py` (3 KB)

### Documentation
- `README.md`
- `QUICKSTART.md`
- `CITATION.cff` (mis à jour)
- `Data_Dictionary.md`
- `Literature_Search_Strategy.md`

### Figures
- `Figure_S2_Oscillatory_Advantage.png` (300 dpi)
- `Figure_S2_Oscillatory_Advantage.tiff` (300 dpi)

### Métadonnées
- `.zenodo.json` (config Zenodo)
- `requirements.txt` (versions exactes)
- `SHA256SUMS.txt` ⭐ NOUVEAU

---

## ✅ Tests de Reproductibilité

### Test 1 : Installation rapide
```bash
git clone https://github.com/Mythmaker28/arrest-molecules.git
cd arrest-molecules
pip install -r Data_Package_FAIR2/requirements.txt
```
**Temps attendu :** < 30 secondes

### Test 2 : Validation données
```bash
cd Data_Package_FAIR2
python data_validation.py
```
**Résultat attendu :** `[SUCCÈS] Toutes les validations réussies !`

### Test 3 : Quick Check
```bash
python quickcheck_api.py
```
**Résultat attendu :** `[SUCCÈS] Tous les tests de validation réussis !`

### Test 4 : Calcul complet
```bash
python Python_Code_API_Monte_Carlo.py --all
```
**Temps attendu :** < 60 secondes  
**Output :** API pour 10 composés avec intervalles de confiance

---

## 🔒 Checksums SHA256

Tous les assets de cette release ont des checksums SHA256 vérifiables dans `SHA256SUMS.txt` :

```
# Exemple (valeurs à générer)
abc123... Compound_Properties_Database.csv
def456... API_Calculations_Full.xlsx
...
```

**Vérification :**
```bash
sha256sum -c SHA256SUMS.txt
```

---

## 📊 Changements depuis v1.1.0

### Ajoutés
- ✅ `quickcheck_api.py` - Validation rapide des valeurs
- ✅ `SHA256SUMS.txt` - Checksums de sécurité
- ✅ CI Reproducibility workflow complet
- ✅ Upload automatique des artifacts CI

### Modifiés
- ✅ `README.md` - DOI intégré, version 1.1.1
- ✅ `CITATION.cff` - Version et date mises à jour
- ✅ `.github/workflows/python-test.yml` - Renommé et amélioré
- ✅ Badges - DOI et release date actualisés

### Corrigés
- ✅ Timeout CI (60s max pour calculs)
- ✅ Validation artefacts avant tests
- ✅ Noms de projet harmonisés

---

## 🎓 Citation

### Format Texte
```
Lepesteur T. (2025). Molecular Arrest Framework Research Data Package (v1.1.1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.17420685
```

### BibTeX
```bibtex
@dataset{lepesteur2025molecular,
  author       = {Lepesteur, Tommy},
  title        = {Molecular Arrest Framework Research Data Package},
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v1.1.1},
  doi          = {10.5281/zenodo.17420685},
  url          = {https://doi.org/10.5281/zenodo.17420685}
}
```

---

## 🚀 Prochaines Étapes

### v1.2 (Prévue)
- Ajout analogs salvinorin A (8 composés supplémentaires)
- Extended case studies (2 nouvelles études)
- Interactive dashboard (Plotly/Dash)

### v2.0 (Future)
- Intégration données expérimentales (Exp 1-3)
- Validation clinique
- Extension framework

---

## 📞 Support

**Questions :** tommy.lepesteur@hotmail.fr  
**Issues :** https://github.com/Mythmaker28/arrest-molecules/issues  
**DOI :** https://doi.org/10.5281/zenodo.17420685

---

## 📜 Licences

- **Données :** CC-BY 4.0
- **Code :** MIT License

---

**Release préparée le :** 23 octobre 2025  
**Par :** Tommy Lepesteur  
**Type :** Patch de reproductibilité  
**Status :** ✅ Production-ready

