# Molecular Arrest Framework v1.1.0

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17420685.svg)](https://doi.org/10.5281/zenodo.17420685)

> **First public release** of the Molecular Arrest Framework - A unifying theoretical framework for natural compounds with dampening effects on biological regulation.

---

## 📦 What's in this Release

### Core Scientific Content
- **Manuscript (v6)** - Complete theoretical framework with IMRAD structure (1,943 lines)
- **Structured data package** - FAIR² compliant research data
- **10 paradigmatic compounds** - Spanning arrest-oscillation continuum
  - 6 core arrest agents (Salvinorin A, Paclitaxel, Rapamycin, Capsaicin, Tetrodotoxin, Resveratrol)
  - 4 continuum compounds (Ibogaine, Noribogaine, Psilocybin, LSD)

### Metrics & Calculations
- **API (Arrest Potency Index)** - Quantitative framework for arrest potency
- **EMC (Entropy Modulation Coefficient)** - Neural complexity metric
- **NCR (Network Connectivity Reduction)** - Brain network impact
- **PARI (Post-Arrest Resilience Index)** - Hormetic benefit quantification
- **Monte Carlo uncertainty quantification** - Full Python implementation with reproducible seed

### Data Package (FAIR² Compliant)
- `Compound_Properties_Database.csv` - 10 compounds × 36 parameters with PubMed sources
- `Confidence_Grading_Matrix.csv` - 44 quantitative predictions stratified by evidence level
- `API_Calculations_Full.xlsx` - Step-by-step calculations with Monte Carlo simulations
- `Experimental_Protocols_Summary.csv` - 3 validation experiments with power calculations
- `Case_Studies_Supplement.md` - 5 extended case studies

### Code & Reproducibility
- **Python_Code_API_Monte_Carlo.py** - Fully documented script (MIT License)
  - Fixed seed=42 by default for reproducibility
  - Option for independence tests with variable seeds
  - 10,000 Monte Carlo iterations per compound
- **R_Code_Figures_S2.R** - Publication-quality figure generation
- **requirements.txt** - Explicit Python dependencies with versions
- **test_api_calculations.py** - Unit tests for API calculations

### Documentation
- **Data_Dictionary.md** - Complete variable definitions, units, quality control
- **Literature_Search_Strategy.md** - PRISMA-compliant search protocol (95+ sources)
- **README.md** - Comprehensive usage guide with quick start
- **CONTRIBUTING.md** - Contribution guidelines
- **CODE_OF_CONDUCT.md** - Community standards

### Supplementary Materials
- **Figures_Supplementaires.txt** - Specifications for Figures S1-S3
- **v6.txt** - Full manuscript in structured text format
- Figure drafts (S1: Molecular Structures, S2: Oscillatory Advantage, S3: API Flowchart)

---

## 🔬 Scientific Highlights

### Novel Framework
- **First unifying theory** for molecular arrest across biological scales
- **Explicit falsifiability** - 44 testable predictions with confidence grading
- **Quantitative metrics** for dampening vs. oscillatory effects
- **3 proposed validation experiments** with full protocols

### Data Quality
- **95+ primary sources** from peer-reviewed literature
- **All parameters traceable** to PubMed IDs
- **Confidence stratification** - High (41%), Moderate (30%), Low (30%)
- **Monte Carlo uncertainty** - 95% confidence intervals for all APIs

### Reproducibility
- ✅ Fixed random seed (seed=42) for exact replication
- ✅ Explicit software versions (Python 3.8+, R 4.0+)
- ✅ Public databases only (DrugBank 5.1.10, ChEMBL v31, PubChem)
- ✅ Step-by-step calculation documentation

---

## 📊 Key Statistics

| Metric | Value |
|--------|-------|
| Compounds characterized | 10 |
| Molecular parameters | 36 per compound |
| Quantitative predictions | 44 |
| Literature sources | 95+ (PubMed) |
| Code lines (Python) | 562 |
| Monte Carlo iterations | 10,000 per compound |
| Confidence intervals | 95% for all metrics |

---

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/Mythmaker28/arrest-molecules.git
cd arrest-molecules
pip install -r Data_Package_FAIR2/requirements.txt
```

### Run API Calculations
```bash
cd Data_Package_FAIR2
python Python_Code_API_Monte_Carlo.py --all
# Outputs: API values with 95% CI for all compounds
```

### Verify Predictions
```bash
python test_api_calculations.py
# Tests: API formula, Monte Carlo convergence, data integrity
```

---

## 📖 How to Cite

### For the Dataset
> Lepesteur T. (2025). Molecular Arrest Framework Research Data Package (v1.1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.17420685

### For the Framework
> Lepesteur T. (2025). Molecular Arrest in Biological Regulation: A Unifying Framework for Natural Compounds with Dampening Effects. *Manuscript in preparation*.

### For the Code
> Lepesteur T. (2025). molecular-arrest-framework: API calculation tools (v1.1.0). GitHub. https://github.com/Mythmaker28/arrest-molecules

---

## 📜 License

- **Data & Documentation:** CC-BY 4.0 (free to share and adapt with attribution)
- **Code:** MIT License (free to use commercially and non-commercially)
- **Synthesis protocols:** Controlled access (requires IRB approval, see README)

---

## 🔮 Known Items & Future Work

### Pending for Next Release
- [ ] ORCID registration confirmed (currently provisional)
- [ ] Publication-quality figures finalized (post-journal acceptance)
- [ ] Experimental validation data (Experiments 1-3 proposed)

### Planned Updates
- **v1.2:** Add salvinorin A analogs (8 compounds from literature)
- **v2.0:** Integrate Experiment 1 results (fMRI entropy validation)
- **v2.1:** Integrate Experiment 2 results (oscillatory cellular lifespan)
- **v3.0:** Clinical validation from Experiment 3 (TRD trial)

---

## 🤝 Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for guidelines.

**Accepted contributions:**
- Novel compound additions (requires literature PMIDs)
- Bug fixes with tests
- Documentation improvements
- Experimental validation data

**Major changes require discussion** - Open an issue before submitting PRs for:
- Metric modifications (API, EMC, NCR, PARI)
- Threshold changes (Level 1/2/3 criteria)
- New dependencies

---

## 📞 Contact & Support

- **Questions:** tommy.lepesteur@hotmail.fr
- **Issues:** https://github.com/Mythmaker28/arrest-molecules/issues
- **Contributions:** Pull requests welcome

**Response time:** 7 business days

---

## 🙏 Acknowledgments

- **Independent data verification:** Dr. Marie Legrand, PharmD (Université de Rennes)
- **Database access:** DrugBank, PubChem, ChEMBL (public versions)
- **Community:** Open science advocates and reviewers

---

## ⚠️ Responsible Research Notice

This framework includes discussion of:
- Schedule I controlled substances (research context only)
- Dual-use compounds (synthesis protocols under controlled access)
- Experimental protocols requiring IRB/DEA approval

**All use must comply with local regulations.** See Section 4.4.5 of manuscript for dual-use considerations and mitigation strategies.

---

## 📋 Changelog (v1.1.0)

### Added
- 4 new compounds (Ibogaine, Noribogaine, Psilocybin, LSD)
- Case Studies Supplement (5 detailed studies)
- Extended predictions (42 → 44 total)
- requirements.txt with explicit versions
- Harmonized documentation (95+ sources)

### Changed
- Dataset: 6 → 10 compounds (+67%)
- Version numbering harmonized to v1.1.0
- GitHub URLs canonicalized (Mythmaker28/arrest-molecules)
- Enhanced literature search strategy

### Fixed
- Prediction count consistency (now 44 everywhere)
- Compound count consistency (now 10 everywhere)
- Version consistency across all files
- Contact information harmonized

---

**Release Date:** October 22, 2025  
**Maintainer:** Tommy Lepesteur  
**License:** CC-BY 4.0 (data) + MIT (code)  
**Zenodo Archive:** Automatic upon release publication

