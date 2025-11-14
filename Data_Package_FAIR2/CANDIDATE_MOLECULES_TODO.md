# Candidate Molecules for Dataset Expansion

**Date:** November 2025  
**Status:** TODO - Awaiting literature review and parameter extraction  
**Purpose:** Expand dataset beyond current 10 compounds to strengthen framework validation

---

## Priority 1: High-Confidence Arrest Candidates

### 1. Muscimol (GABA_A agonist)
**Rationale:** Prototypical neural arrest agent, extensively characterized  
**Expected properties:**
- High GABA_A affinity (K_i ~1-5 nM)
- Rapid onset (minutes)
- Clear entropy reduction (EMC < -0.3)
- **TODO:** Extract K_d, k_off, EC50, t_onset from literature (PMIDs needed)
- **Classification (predicted):** Level 2-3

### 2. Adenosine (A1 receptor agonist)
**Rationale:** Endogenous arrest signal, metabolic dampening  
**Expected properties:**
- Moderate affinity (K_d ~10-50 nM)
- Rapid kinetics
- Metabolic arrest via glycolysis inhibition
- **TODO:** Extract pharmacological parameters
- **Classification (predicted):** Level 2

### 3. Diazepam/Midazolam (Benzodiazepines)
**Rationale:** Synthetic arrest agents, clinical validation  
**Expected properties:**
- GABA_A positive allosteric modulation
- Well-characterized PK/PD
- Clear NCR in neuroimaging studies
- **TODO:** Extract binding and functional parameters
- **Classification (predicted):** Level 2

### 4. Propofol (General anesthetic)
**Rationale:** Extreme arrest example, dose-dependent consciousness modulation  
**Expected properties:**
- GABA_A activation
- EMC ~-0.6 to -0.8 (established from anesthesia literature)
- NCR > 70%
- **TODO:** Extract quantitative parameters
- **Classification (predicted):** Level 3 (with post-anesthetic resilience)

---

## Priority 2: mTOR/Metabolic Modulators

### 5. Everolimus (mTOR inhibitor)
**Rationale:** FDA-approved rapalog, similar mechanism to rapamycin  
**Expected properties:**
- High mTOR affinity (K_i ~0.1-1 nM)
- Slower onset than rapamycin
- Similar PARI profile
- **TODO:** Compare API to rapamycin
- **Classification (predicted):** Level 3

### 6. Temsirolimus (mTOR inhibitor)
**Rationale:** Another rapalog for SAR validation  
**Expected properties:**
- Similar to everolimus/rapamycin
- **TODO:** Extract parameters for rapalog class comparison

---

## Priority 3: Additional KOR Agonists (SAR expansion)

### 7. Nalfurafine
**Rationale:** Clinically approved KOR agonist (Japan), less dysphoric  
**Expected properties:**
- K_i ~0.4 nM at KOR
- High selectivity vs MOR/DOR
- Clinical safety data available
- **TODO:** Extract full pharmacological profile
- **Classification (predicted):** Level 2-3

### 8. Mesyl Salvinorin B
**Rationale:** Salvinorin A analog with improved selectivity  
**Expected properties:**
- K_i ~0.6 nM
- 11,000× KOR selectivity
- Mentioned in manuscript SAR section
- **TODO:** Extract complete dataset for inclusion

---

## Priority 4: Negative Controls (Minimal Arrest)

### 9. Curcumin
**Rationale:** Popular "nutraceutical" with weak effects  
**Expected properties:**
- Multiple targets, low affinity (~μM range)
- Poor bioavailability
- Minimal arrest signatures
- **TODO:** Extract parameters to serve as Level 0-1 comparator
- **Classification (predicted):** Level 0-1 (sub-arrest threshold)

### 10. Quercetin
**Rationale:** Another polyphenol with weak multi-target effects  
**Expected properties:**
- Similar to curcumin, resveratrol
- Weak SIRT1 activation
- **TODO:** Extract parameters
- **Classification (predicted):** Level 1

---

## Data Requirements for Each Candidate

For inclusion in `Compound_Properties_Database.csv`, extract:

**Mandatory:**
- [ ] Compound_Name, CAS_Number
- [ ] SMILES, InChI (from PubChem/ChEMBL)
- [ ] Molecular_Weight, LogP, Rotatable_Bonds
- [ ] Primary_Target, Target_Gene
- [ ] K_i_nM (with source PMID)
- [ ] K_d_nM
- [ ] k_off_per_min (or estimate from duration)
- [ ] tau_residence_min (must equal 1/k_off)
- [ ] t_onset_min
- [ ] EC50_nM (with assay type)

**Optional but valuable:**
- [ ] t_half_plasma_h
- [ ] Cmax, AUC, Vd, Clearance
- [ ] Protein_Binding_percent
- [ ] Clinical_Status

**Calculated (after data entry):**
- [ ] API_absolute, API_relative
- [ ] API_CI_lower, API_CI_upper (via Monte Carlo)
- [ ] EMC, NCR, AKR, PARI (from literature)
- [ ] Arrest_Level classification
- [ ] Confidence_Grade

---

## Literature Search Strategy

For each candidate molecule:

1. **PubMed search:** "[Compound name] AND (binding OR affinity OR Ki OR Kd)"
2. **Focus on:** Radioligand binding assays, functional assays (EC50), PK studies
3. **Prioritize:** Meta-analyses, high-impact journals, multiple independent labs
4. **Extract:** Mean ± SD for each parameter, number of studies (for uncertainty)
5. **Document:** All PMIDs in Compound_Properties_Database.csv

---

## Expected Impact

Adding these 10 compounds would:
- Expand dataset from 10 → 20 compounds (+100%)
- Strengthen SAR patterns (e.g., KOR agonist series)
- Validate rapalog class predictions
- Provide better negative controls (curcumin, quercetin)
- Enable more robust statistical correlations (N=20 vs N=10)

**Caution:** Do NOT fabricate precise values. All entries must be literature-supported with PMIDs.

---

## Status: PENDING LITERATURE REVIEW

**Assigned to:** [Researcher with database access]  
**Timeline:** Requires ~2-4 weeks for thorough literature extraction  
**Next step:** Systematic PubMed/DrugBank/ChEMBL queries for each candidate


