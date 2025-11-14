# Molecular Arrest in Biological Regulation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17420685.svg)](https://doi.org/10.5281/zenodo.17420685)
[![Latest Release](https://img.shields.io/github/v/release/Mythmaker28/arrest-molecules?label=Latest%20Release&color=success)](https://github.com/Mythmaker28/arrest-molecules/releases/latest)
[![GitHub Release Date](https://img.shields.io/github/release-date/Mythmaker28/arrest-molecules)](https://github.com/Mythmaker28/arrest-molecules/releases)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
[![CI Tests](https://img.shields.io/github/actions/workflow/status/Mythmaker28/arrest-molecules/python-test.yml?branch=main&label=tests)](https://github.com/Mythmaker28/arrest-molecules/actions)

**Hypothèse exploratoire et framework pilote pour l'étude des composés à effets d'amortissement biologique**

> 📢 **Version actuelle : v1.1.1** | [📥 Télécharger la dernière release](https://github.com/Mythmaker28/arrest-molecules/releases/latest) | [📖 Notes de version](https://github.com/Mythmaker28/arrest-molecules/releases/tag/v1.1.1)

---

<!--VERSION-START-->
**Version actuelle (latest):** v1.1.1 ⭐  
**Date de release :** 23 October 2025  
**DOI Zenodo :** 10.5281/zenodo.17420685  
<!--VERSION-END-->

**Author:** Tommy Lepesteur  
**ORCID:** 0009-0009-0577-9563  
**License:** CC-BY 4.0 (data), MIT License (code)  
**Repository:** https://github.com/Mythmaker28/arrest-molecules

> ℹ️ **Cette page pointe toujours vers les assets de la dernière release.** Les liens ci-dessous se mettent à jour automatiquement.  

---

## ⚠️ Avertissement Méthodologique

**Ce projet présente une hypothèse de travail exploratoire, non un cadre établi.**

- ✅ **Points forts:** Transparence des données, code reproductible, prédictions falsifiables, classement par confiance
- ⚠️ **Limitations critiques:**
  - Seulement 10 composés (échantillon pilote)
  - Aucune donnée expérimentale nouvelle générée
  - Métriques proposées (API, EMC, NCR, etc.) **ne sont pas encore validées empiriquement**
  - 59% des prédictions sont de confiance modérée ou faible
  - Classifications basées sur des seuils arbitraires nécessitant validation

**Ce travail vise à stimuler la recherche, pas à fournir des conclusions définitives.**

---

## Description

This data package accompanies the manuscript "Molecular Arrest in Biological Regulation: A Working Hypothesis for Natural Compounds with Dampening Effects" submitted to *Frontiers in Pharmacology*.

**⚠️ IMPORTANT: This is a pilot hypothesis-generating framework, not an established paradigm.** The work proposes testable concepts requiring prospective experimental validation.

The package contains:
- Curated molecular properties for **10 exemplar compounds**: 8 arrest agents (salvinorin A, paclitaxel, rapamycin, capsaicin, tetrodotoxin, resveratrol, ibogaine, noribogaine) + 2 oscillatory controls (psilocybin, LSD) for boundary comparison
- **Proposed** pharmacological metrics (API, EMC, NCR, AKR, PARI) — *indices requiring empirical validation*
- Uncertainty quantification via Monte Carlo simulation
- Confidence grading for 44 quantitative predictions (41% high confidence, 30% moderate, 30% low)
- Executable code for reproducing all calculations
- **5 extended case studies** (ibogaine/noribogaine, resveratrol, fasting/breathing, psilocybin/LSD, AI memory)
- Data dictionary and usage protocols

**⚠️ LIMITATIONS:**
- **No new experimental data were generated.** All values are literature-derived (95+ sources).
- **Small dataset:** Only 10 compounds; conclusions remain tentative.
- **Metrics are proposed, not validated:** API, EMC, NCR, AKR, PARI require prospective testing.
- **Many predictions are low-to-moderate confidence:** See `Confidence_Grading_Matrix.csv` for details.

---

## Files Included

### Core Data Tables

**1. Compound_Properties_Database.csv** (10 rows × 36 columns)
- Molecular properties: formula, MW, logP, rotatable bonds, SMILES, InChI
- Binding parameters: K_i, K_d, EC₅₀, k_off
- Pharmacokinetics: t₁/₂, C_max, AUC, V_d, clearance, protein binding
- **New compounds:** Ibogaine, Noribogaine, Psilocybin, LSD (arrest-oscillation continuum)
- Literature sources: PubMed IDs for each parameter

**2. API_Calculations_Full.xlsx** (multi-sheet workbook)
- Sheet 1: Input parameters with literature sources
- Sheet 2: Step-by-step API calculations (absolute → relative)
- Sheet 3: Monte Carlo simulation results (10,000 iterations per compound)
- Sheet 4: 95% confidence intervals
- Sheet 5: Sensitivity analysis (varying parameters ±30%)

**3. Confidence_Grading_Matrix.csv** (44 rows × 6 columns)
- All quantitative predictions from manuscript
- Evidence type (direct/indirect/extrapolated)
- Confidence level (high/moderate/low)
- Validation requirements

**4. Experimental_Protocols_Summary.csv** (3 rows × 12 columns)
- Design parameters for Experiments 1-3
- Sample sizes with power calculations
- Primary/secondary outcomes
- Success/falsification criteria
- Estimated costs and timelines

### Code and Scripts

**5. Python_Code_API_Monte_Carlo.py**
- Fully commented Python 3.8+ script
- Calculates API with uncertainty propagation
- Requires: numpy, pandas, matplotlib
- Runtime: <10 seconds on standard laptop
- Outputs: API values with 95% CI, diagnostic plots

**6. R_Code_Figures_S2.R**
- Generates 3-panel oscillatory advantage figure
- Requires: ggplot2, dplyr, survival, patchwork
- Customizable parameters (colors, font sizes)
- Exports 300 dpi TIFF files

### Documentation

**7. Data_Dictionary.md**
- Complete variable definitions
- Units and measurement methods
- Abbreviations and ontology terms
- Quality control procedures

**8. Literature_Search_Strategy.md**
- PubMed search terms and filters
- PRISMA-style flowchart (1,247 abstracts screened → 95 retained)
- Inclusion/exclusion criteria
- Data extraction protocol

**9. Case_Studies_Supplement.md** ⭐ NEW
- Extended Case Study 1: Ibogaine & Noribogaine (hybrid arrest, addiction reset)
- Extended Case Study 2: Resveratrol & SIRT1 (minimal arrest, negative control)
- Extended Case Study 3: Fasting & Breathing (natural oscillators)
- Extended Case Study 4: Psilocybin & LSD (high-entropy oscillation, DMN dissolution)
- Extended Case Study 5: AI Memory (computational extension of arrest principles)

---

## ⚡ Quick Start (60 seconds)

```bash
# 1. Clone & install
git clone https://github.com/Mythmaker28/arrest-molecules.git
cd arrest-molecules
python -m venv .venv

# 2. Activate environment
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run reproducibility pipeline
python run_arrest_pipeline.py
```

**Output:** Validates data files, creates `outputs/` directory, and runs analysis scripts if available.

📖 **Detailed guide:** See [`QUICKSTART.md`](QUICKSTART.md) and [`DOCS/REPRO_STATUS.md`](DOCS/REPRO_STATUS.md)

---

## Quick Start Guide

### For users wanting to verify API calculations:

1. Open `Compound_Properties_Database.csv`
2. Identify compound of interest (e.g., Rapamycin)
3. Note parameters: K_d = 0.1 nM, τ_residence = 120 min, t_onset = 1440 min, EC₅₀ = 1 nM
4. Run Python script:
   ```python
   python Python_Code_API_Monte_Carlo.py --compound Rapamycin
   ```
5. Output: API = 0.12 [95% CI: 0.08-0.16], Confidence: MODERATE

### For users wanting to test the framework with new compounds:

1. Gather required parameters from literature (K_d, k_off or duration, t_onset, EC₅₀)
2. Add row to `Compound_Properties_Database.csv`
3. Run Python script with `--new_compound` flag
4. Compare API to reference standards (Table 1 in manuscript)
5. **Critically evaluate** whether arrest classification criteria (EMC/NCR/PARI) apply

**Caution:** The classification system is a working hypothesis. Empirical validation against experimental outcomes is essential before drawing conclusions.

### For users wanting to reproduce figures:

1. Ensure R packages installed: `install.packages(c("ggplot2", "dplyr", "patchwork"))`
2. Run: `Rscript R_Code_Figures_S2.R`
3. Figures saved to `./output/` directory as TIFF (300 dpi)

---

## Data Dictionary (Abbreviated)

### Compound_Properties_Database.csv

| Column Name | Description | Units | Data Type | Example |
|-------------|-------------|-------|-----------|---------|
| Compound_Name | Chemical name | — | String | Salvinorin A |
| CAS_Number | Chemical Abstracts Service registry | — | String | 83729-01-5 |
| SMILES | Simplified molecular-input line-entry system | — | String | COC(=O)[C@]12[C@@]3... |
| InChI | International Chemical Identifier | — | String | InChI=1S/C23H28O8... |
| Molecular_Formula | Elemental composition | — | String | C23H28O8 |
| Molecular_Weight | Molecular mass | g/mol | Numeric | 432.47 |
| LogP | Octanol-water partition coefficient | — | Numeric | 2.73 |
| Rotatable_Bonds | Count of freely rotatable bonds | — | Integer | 3 |
| Primary_Target | Main molecular target | — | String | Kappa-opioid receptor |
| Target_Gene | Gene symbol | — | String | OPRK1 |
| K_i | Inhibition constant | nM | Numeric | 1.8 |
| K_i_Source_PMID | PubMed ID for K_i value | — | Integer | 12202542 |
| K_d | Dissociation constant | nM | Numeric | 1.8 |
| k_off | Dissociation rate constant | min⁻¹ | Numeric | 0.04 |
| tau_residence | Residence time (1/k_off) | min | Numeric | 25 |
| t_onset | Time to 50% effect | min | Numeric | 1 |
| EC50 | Half-maximal effective conc. | nM | Numeric | 2 |
| EC50_Assay | Functional assay type | — | String | GIRK activation |
| t_half_plasma | Plasma half-life | h | Numeric | 0.15 |
| Cmax | Peak plasma concentration | ng/mL | Numeric | 2.4 |
| AUC | Area under curve | ng·h/mL | Numeric | 15 |
| Vd | Volume of distribution | L/kg | Numeric | 3.2 |
| Clearance | Systemic clearance | L/h/kg | Numeric | 12.5 |
| Protein_Binding | Plasma protein binding | % | Numeric | 89 |
| API_absolute | Arrest Potency Index (absolute) | nM⁻² | Numeric | 6.95 |
| API_relative | API normalized to salvinorin A | — | Numeric | 1.00 |
| API_CI_lower | 95% CI lower bound | — | Numeric | 0.85 |
| API_CI_upper | 95% CI upper bound | — | Numeric | 1.15 |
| AKR | Arrest Kinetics Ratio | — | Numeric | 1.5 |
| EMC | Entropy Modulation Coefficient | — | Numeric | -0.4 |
| NCR | Network Connectivity Reduction | % | Numeric | 50 |
| PARI | Post-Arrest Resilience Index | — | Numeric | 0.3 |
| Arrest_Level | Classification (1/2/3) | — | String | Level 3 |
| Confidence_Grade | Overall data quality | — | String | MODERATE |

### Missing Data Encoding
- **NA:** Not applicable (e.g., EMC for non-neural compounds)
- **ND:** Not determined (measurement not yet performed)
- **NR:** Not reported in literature
- **EST:** Estimated value (not directly measured)

---

## Usage Notes

### Target Audience
- Pharmacologists interested in testing the framework's predictions
- Medicinal chemists exploring potential dampening agent design principles
- Systems biologists studying network dynamics and oscillatory processes
- Researchers evaluating chronopharmacology hypotheses
- Educators seeking quantitative pharmacology case studies

**Note:** This framework is exploratory. Users should critically evaluate claims and contribute to validation efforts.

### How to Cite This Work

**For the dataset:**
> Lepesteur T. (2025). Molecular Arrest Framework Research Data Package (v1.1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.17420685

**For the manuscript:**
> Lepesteur T. Molecular Arrest in Biological Regulation: A Unifying Framework for Natural Compounds with Dampening Effects. *Manuscript in preparation* (2025)

**For the code:**
> Lepesteur T. (2025). molecular-arrest-framework: API calculation tools (v1.1.0). GitHub. https://github.com/Mythmaker28/arrest-molecules

**BibTeX:**
```bibtex
@dataset{lepesteur2025molecular,
  author       = {Lepesteur, Tommy},
  title        = {Molecular Arrest Framework Research Data Package},
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v1.1.0},
  doi          = {10.5281/zenodo.17420685},
  url          = {https://doi.org/10.5281/zenodo.17420685}
}
```

**Note:** This DOI is the **concept DOI** that always points to the latest version. For citing a specific version, use the version-specific DOI from the Zenodo record.

---

## Version History

**v1.1.1 (October 2025):** ⭐ CURRENT (Reproducibility Patch)
- ✅ Quick check script for instant validation (< 1s)
- ✅ Full CI/CD reproducibility workflow
- ✅ Automated artifact verification
- ✅ SHA256 checksums for all assets
- ✅ DOI Zenodo integrated everywhere
- ✅ 1-click reproducibility guaranteed (< 3 min)

**v1.1.0 (October 2025):**
- **Extended dataset:** 6 → 10 compounds (+67%)
- **New compounds:** Ibogaine, Noribogaine (hybrid arrest), Psilocybin, LSD (oscillation)
- **Case studies supplement:** 5 detailed case studies spanning arrest-oscillation continuum
- **requirements.txt:** Explicit Python dependencies with versions
- Updated predictions: 42 → 44 with refined confidence grading
- Enhanced documentation: 95+ literature sources

**v1.0 (October 2025):**
- Initial release accompanying manuscript submission
- 6 core arrest compounds characterized
- 44 predictions with confidence grading
- Monte Carlo uncertainty quantification implemented

**Planned updates (contingent on validation):**
- **v1.2:** Add salvinorin A analogs (8 compounds) from Supplementary Table S2 — *if SAR patterns hold*
- **v2.0:** Incorporate Experiment 1 results (salvinorin fMRI data) — *if predictions confirmed*
- **v2.1:** Incorporate Experiment 2 results (oscillatory cellular lifespan) — *if oscillatory advantage validated*
- **v3.0:** Clinical validation from Experiment 3 (TRD trial) — *if safety/efficacy demonstrated*

**Note:** Future versions depend on prospective experimental validation. If key predictions fail, the framework will require substantial revision or abandonment.

---


## Contact and Support

**Questions:** tommy.lepesteur@hotmail.fr  
**Issue tracking:** https://github.com/Mythmaker28/arrest-molecules/issues  
**Contributions:** Pull requests welcome for novel compound additions (requires literature sources)  

**Controlled access requests** (for synthesis protocols):
Email corresponding author with:
1. Institutional email (no personal addresses)
2. IRB approval documentation (PDF)
3. Research protocol summary (1 page)
4. Statement of intended use (therapeutic research only)

Response within 7 business days.

---

## License and Reuse

**Data:** Creative Commons Attribution 4.0 International (CC-BY 4.0)
- ✓ Share and adapt freely
- ✓ Provide attribution
- ✓ Indicate if changes made

**Code:** MIT License
- ✓ Use commercially or non-commercially
- ✓ Modify and distribute
- ✓ Include original license notice

**Restrictions:** Synthesis protocols for high-potency analogs subject to controlled access (see Data Availability Statement in manuscript Section "Data Availability Statement").

---

## Acknowledgments

Data compilation supported by independent literature review with quality verification by an external consultant. Database access via freely available public resources (DrugBank, PubChem, ChEMBL).

---

## Changelog & Release Notes

### v1.1 (2025-10-21) - Extended Dataset & Case Studies ⭐

**Dataset expansion (+67%) :**
- **4 nouveaux composés ajoutés** : Ibogaine, Noribogaine, Psilocybin, LSD
- Dataset : 6 → 10 composés couvrant tout le continuum arrest-oscillation
- Ibogaine/Noribogaine : Arrest hybride DAT/SERT/κ-opioid, mécanisme addiction reset
- Psilocybin/LSD : Oscillation haute entropie (EMC positif), dissolution DMN

**Nouveau supplément : Case_Studies_Supplement.md (5 études détaillées) :**
1. Ibogaine & Noribogaine : Hybrid arrest, GDNF neuroplasticity, addiction reset
2. Resveratrol & SIRT1 : Minimal arrest (témoin négatif), échec seuil
3. Fasting & Breathing : Natural oscillators, physiological arrest principles
4. Psilocybin & LSD : High-entropy oscillation, DMN connectivity, TRD applications
5. AI Memory Extension : Dropout/consolidation parallels, computational arrest

**Documentation améliorée :**
- `requirements.txt` créé avec versions exactes (numpy 1.24.3, pandas 2.0.3, etc.)
- Références bibliographiques : 85 → 95+ sources
- Prédictions : 42 → 44 (ajout métabolites psychédéliques)

**Statistiques mises à jour dans README :**
- Compound_Properties_Database.csv : 10 lignes, 36 colonnes
- Literature sources : 95+ PMIDs
- Case studies : 5 (vs 0 précédemment)

---

### v1.0.1 (2025-10-21) - Corrections Post-Rapport

**Harmonisation prédictions (42→44) :**
- Nombre de prédictions corrigé dans v6.txt pour correspondre au CSV
- Statistiques de confiance recalculées : High 18/44 (41%), Moderate 13/44 (30%), Low 13/44 (30%)

**Fichiers manquants créés (5) :**
- `Experimental_Protocols_Summary.csv`, `R_Code_Figures_S2.R`, `Data_Dictionary.md`
- `Literature_Search_Strategy.md`, `API_Calculations_Full.xlsx`

**Figures brouillons créés (3) :**
- `Figure_S1_Molecular_Structures_draft.png`, `Figure_S2_Oscillatory_Advantage_draft.png/tiff`
- `Figure_S3_API_Flowchart_draft.png`

**Améliorations code :**
- Option `--random-seed` ajoutée au script Python (défaut 42 reproductible)

---

### v1.0 (2025-10-21) - Initial Release

**2025-10-21:** Dataset created, v1.0 submitted with manuscript

