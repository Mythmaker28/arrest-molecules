# Molecular Arrest Framework - Research Data Package

**Version:** 1.0  
**Date:** October 2025  
**Author:** Tommy Lepesteur (tommy.lepesteur@hotmail.fr)  
**ORCID:** 0009-0009-0577-9563  
**License:** CC-BY 4.0 (data), MIT License (code)  
**DOI:** [To be assigned by Zenodo upon publication]  

---

## Description

This data package accompanies the manuscript "Molecular Arrest in Biological Regulation: A Unifying Framework for Natural Compounds with Dampening Effects" submitted to *Frontiers in Pharmacology*.

The package contains:
- Curated molecular properties for 6 paradigmatic arrest compounds
- Calculated pharmacological metrics (API, EMC, NCR, AKR, PARI)
- Uncertainty quantification via Monte Carlo simulation
- Confidence grading for 42 quantitative predictions
- Executable code for reproducing all calculations
- Data dictionary and usage protocols

**No new experimental data were generated.** All values are derived from published literature (85 primary sources cited in main manuscript).

---

## Files Included

### Core Data Tables

**1. Compound_Properties_Database.csv** (6 rows × 24 columns)
- Molecular properties: formula, MW, logP, rotatable bonds, SMILES, InChI
- Binding parameters: K_i, K_d, EC₅₀, k_off
- Pharmacokinetics: t₁/₂, C_max, AUC, V_d, clearance, protein binding
- Literature sources: PubMed IDs for each parameter

**2. API_Calculations_Full.xlsx** (multi-sheet workbook)
- Sheet 1: Input parameters with literature sources
- Sheet 2: Step-by-step API calculations (absolute → relative)
- Sheet 3: Monte Carlo simulation results (10,000 iterations per compound)
- Sheet 4: 95% confidence intervals
- Sheet 5: Sensitivity analysis (varying parameters ±30%)

**3. Confidence_Grading_Matrix.csv** (42 rows × 6 columns)
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

**7. Data_Dictionary.pdf**
- Complete variable definitions
- Units and measurement methods
- Abbreviations and ontology terms
- Quality control procedures

**8. Literature_Search_Strategy.pdf**
- PubMed search terms and filters
- PRISMA-style flowchart (1,247 abstracts screened → 85 retained)
- Inclusion/exclusion criteria
- Data extraction protocol

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

### For users wanting to extend framework to new compounds:

1. Gather required parameters (K_d, k_off or duration, t_onset, EC₅₀)
2. Add row to `Compound_Properties_Database.csv`
3. Run Python script with `--new_compound` flag
4. Compare API to reference standards (Table 1 in manuscript)
5. Assign arrest level based on EMC/NCR/PARI criteria

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
- Pharmacologists validating framework predictions
- Medicinal chemists designing novel arrest agents
- Systems biologists studying network dynamics
- Clinicians exploring chronopharmacology applications
- Educators teaching quantitative pharmacology

### Recommended Citations

**For the dataset:**
> Mythmaker T. Molecular Arrest Framework Research Data Package (Version 1.0) [Data set]. Zenodo. https://doi.org/[DOI-to-be-assigned] (2025)

**For the manuscript:**
> Mythmaker T. Molecular Arrest in Biological Regulation: A Unifying Framework for Natural Compounds with Dampening Effects. *Front Pharmacol* [in review] (2025)

**For the code:**
> Mythmaker T. molecular-arrest-framework: API calculation tools (v1.0). GitHub. https://github.com/molecular-arrest-framework (2025)

---

## Version History

**v1.0 (October 2025):**
- Initial release accompanying manuscript submission
- 6 compounds characterized
- 42 predictions with confidence grading
- Monte Carlo uncertainty quantification implemented

**Planned updates:**
- **v1.1:** Add salvinorin A analogs (8 compounds) from Supplementary Table S2
- **v2.0:** Incorporate Experiment 1 results (salvinorin fMRI data) when available
- **v2.1:** Incorporate Experiment 2 results (oscillatory cellular lifespan)
- **v3.0:** Clinical validation from Experiment 3 (TRD trial)

---

## Contact and Support

**Questions:** tommy.lepesteur@hotmail.fr  
**Issue tracking:** https://github.com/molecular-arrest-framework/issues  
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

## Changelog

**2025-10-21:** Dataset created, v1.0 submitted with manuscript

