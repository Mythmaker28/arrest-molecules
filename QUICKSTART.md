# ⚡ Quickstart - 60 secondes

## Installation & Exécution

### Option A : Depuis la Dernière Release (Recommandé)

```bash
# Télécharger directement les assets de la dernière release
wget https://github.com/Mythmaker28/arrest-molecules/releases/latest/download/arrest-molecules-latest.zip
unzip arrest-molecules-latest.zip
cd arrest-molecules
pip install -r Data_Package_FAIR2/requirements.txt
```

### Option B : Cloner le Repo Complet

```bash
git clone https://github.com/Mythmaker28/arrest-molecules.git
cd arrest-molecules
pip install -r Data_Package_FAIR2/requirements.txt
```

### 2. Installer les dépendances
```bash
pip install -r Data_Package_FAIR2/requirements.txt
```

### 3. Exécuter le calcul API
```bash
cd Data_Package_FAIR2
python Python_Code_API_Monte_Carlo.py --all
```

**Résultat attendu :** Calcul API pour les 10 composés avec intervalles de confiance 95%

---

## Reproduire une Figure

```bash
# Générer la figure S2 (oscillatory advantage)
cd Data_Package_FAIR2
Rscript R_Code_Figures_S2.R
```

**Output :** `figures/Figure_S2_Oscillatory_Advantage.png`

---

## Explorer les Données

```python
import pandas as pd

# Charger la base de composés
df = pd.read_csv('Data_Package_FAIR2/Compound_Properties_Database.csv')
print(f"{len(df)} composés caractérisés")
print(df[['Compound_Name', 'API_relative', 'Confidence_Grade']])

# Charger la matrice de prédictions
pred = pd.read_csv('Data_Package_FAIR2/Confidence_Grading_Matrix.csv')
print(f"\n{len(pred)} prédictions testables")
print(pred['Confidence_Level'].value_counts())
```

---

## Tests

```bash
cd Data_Package_FAIR2
python -m pytest test_api_calculations.py -v
```

---

## Citation

```bibtex
@dataset{lepesteur2025molecular,
  author    = {Lepesteur, Tommy},
  title     = {Molecular Arrest Framework Research Data Package},
  year      = 2025,
  publisher = {Zenodo},
  version   = {v1.1.0},
  doi       = {10.5281/zenodo.17420685}
}
```

**DOI :** https://doi.org/10.5281/zenodo.17420685

---

**Temps total :** < 3 minutes sur poste standard  
**Prérequis :** Python 3.8+, R 4.0+ (optionnel pour figures)

