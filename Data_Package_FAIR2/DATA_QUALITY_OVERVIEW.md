# Data Quality Overview - Molecular Arrest Framework

**Version:** 1.2.0-experimental  
**Date:** November 14, 2025  
**Purpose:** Transparent assessment of data completeness and quality for all compounds

---

## Summary Statistics

- **Total compounds:** 19 (10 core + 9 extended)
- **Tier A (Core, high completeness):** 7 compounds (70% of core)
- **Tier B (Core/Extended, moderate completeness):** 5 compounds (3 core + 2 extended)
- **Tier C (Extended, partial/exploratory):** 5 compounds
- **Tier D (Negative controls, minimal data):** 2 compounds

---

## Data Quality Tiers

### Tier A – Core, High Completeness (≥90% key parameters, strong literature)

#### 1. Salvinorin A [CORE]
**Confidence:** VERY HIGH  
**Completeness:** 95%+  
**Justification:** Complete binding (Ki/Kd + PMID 12202542), kinetics (k_off), full PK (t_half, Cmax, AUC, Vd, Clearance), EC50 with assay type, EMC/NCR/PARI from literature. Reference standard for API calculations (relative = 1.00).

#### 2. Paclitaxel [CORE]
**Confidence:** HIGH  
**Completeness:** 95%+  
**Justification:** Complete binding with PMID (8428871), measured k_off (0.00139), comprehensive PK including Cmax/AUC/Vd/Clearance, mitotic arrest well-characterized. Long residence time (720 min) validated.

#### 3. Tetrodotoxin [CORE]
**Confidence:** HIGH  
**Completeness:** 90%+  
**Justification:** Strong binding data (PMID 5419956), literature-derived k_off/residence time (360 min), excellent PK characterization, Na channel block mechanism well-established. Minimal Cmax due to toxicity.

#### 4. Noribogaine [CORE]
**Confidence:** HIGH  
**Completeness:** 95%+  
**Justification:** Complete dataset including measured kinetics (PMID 22230299), extensive PK (long t_half = 38h, full AUC/Vd/Clearance), long residence (2340 min). Active metabolite of ibogaine with clinical data.

#### 5. Psilocybin [CORE]
**Confidence:** HIGH  
**Completeness:** 90%+  
**Justification:** Well-characterized binding (PMID 28012622), measured 5-HT2A kinetics, complete PK, oscillatory metrics (EMC +0.52, NCR -28%) from neuroimaging studies. FDA Breakthrough designation provides clinical validation.

#### 6. Diazepam [EXTENDED]
**Confidence:** HIGH  
**Completeness:** 90%  
**Justification:** Excellent binding data (Ki=18 nM, PMID 6253801), comprehensive PK (t_half 43h, Cmax 390 ng/mL, complete AUC/Vd/Clearance), extensive clinical use. **Missing:** Direct EMC/NCR neuroimaging (estimated -0.3/35%).

#### 7. LSD [CORE]
**Confidence:** MODERATE-HIGH  
**Completeness:** 90%  
**Justification:** Strong binding/kinetics (PMID 28380168), long residence (303 min), good PK, oscillatory metrics from literature. Lower than psilocybin due to less recent clinical data but still robust.

---

### Tier B – Moderate Completeness (50–90%, some gaps but solid foundation)

#### 8. Rapamycin [CORE]
**Confidence:** MODERATE  
**Completeness:** 85%  
**Justification:** Complete binding (PMID 1909400), estimated k_off from signaling duration, good PK. **Weakness:** Very long t_onset (1440 min = 24h) is functional autophagy, not molecular binding onset. Still, mTOR paradigm is well-validated.

#### 9. Capsaicin [CORE]
**Confidence:** MODERATE-HIGH  
**Completeness:** 75%  
**Justification:** Good binding data (PMID 9389475), estimated kinetics from desensitization, partial PK (t_half NA, Cmax/AUC limited). TRPV1 mechanism well-understood but human PK incomplete.

#### 10. Ibogaine [CORE]
**Confidence:** MODERATE  
**Completeness:** 80%  
**Justification:** Solid binding data (PMID 15707643), estimated kinetics, good PK coverage. **Limitation:** Multiple targets (DAT/SERT/κ-opioid) make mechanistic interpretation complex. Phase II clinical data available.

#### 11. Everolimus [EXTENDED]
**Confidence:** MODERATE-HIGH  
**Completeness:** 70%  
**Justification:** FDA-approved rapalog with good PK (Cmax 14.4, AUC 634, full distribution data). **Gap:** Ki/Kd estimated from rapamycin SAR, not direct measurement. k_off calculated (0.0069). Clinical use validates mechanism.

#### 12. Propofol [EXTENDED]
**Confidence:** MODERATE-HIGH  
**Completeness:** 80%  
**Justification:** Good binding (PMID 8502498), extensive clinical PK, strong EMC/NCR/PARI from anesthesia literature. **Gap:** k_off estimated (0.2), not measured from GABA_A kinetics. Extreme arrest example with excellent recovery (PARI 0.6).

---

### Tier C – Partial/Exploratory (Significant NR/EST, strong rationale but incomplete)

#### 13. Nalfurafine [EXTENDED]
**Confidence:** MODERATE  
**Completeness:** 60%  
**Justification:** Strong binding (Ki 0.075 nM, PMID 15707643), good EC50, t_half measured. **Major gaps:** Cmax, AUC, Vd, Clearance all NR. k_off estimated. Clinical use in Japan validates mechanism. **Ready for promotion** once Japanese PK data found.

#### 14. Temsirolimus [EXTENDED]
**Confidence:** MODERATE  
**Completeness:** 65%  
**Justification:** FDA-approved rapalog with complete PK (Cmax 295, AUC 2212, Vd 172, Clearance 10.6). **Gap:** Ki/Kd estimated (0.8), k_off calculated (0.0058). Clinical efficacy supports mechanism.

#### 15. Muscimol [EXTENDED]
**Confidence:** MODERATE  
**Completeness:** 55%  
**Justification:** Good binding (Kd 0.3 nM, PMID 6144558), rapid kinetics (k_off 0.5), strong EMC/NCR. **Major limitation:** PK mostly rodent-derived. Cmax/AUC NR for humans. Research toxin, not clinical. High EMC (-0.65) supports arrest concept.

#### 16. Adenosine [EXTENDED]
**Confidence:** MODERATE  
**Completeness:** 60%  
**Justification:** Good binding (Kd 70 nM, PMID 8987793), measured kinetics, FDA-approved IV use. **Gap:** Ultra-short t_half (0.003h = 11 seconds) makes sustained arrest quantification difficult. Cmax/AUC NR. Endogenous signal validates mechanism.

#### 17. Resveratrol [CORE]
**Confidence:** LOW  
**Completeness:** 70%  
**Justification:** Complete parameter set but **weak affinity** (Kd 50 µM). Rapid dissociation (k_off=1). Very slow onset (720 min). **Tier C because:** Scientifically complete but represents "minimal arrest" boundary, not strong exemplar. Useful as negative comparator.

---

### Tier D – Negative Controls / Minimal Data (Weak affinity, conceptual role)

#### 18. Curcumin [EXTENDED]
**Confidence:** LOW  
**Completeness:** 50%  
**Justification:** Very weak affinity (Kd 50 µM, PMID 14570043), rapid dissociation, very long onset (1440 min). Many EST/NR fields. **Role:** Negative control to define "Level 0-1" minimal arrest threshold. Scientifically valuable as boundary case.

#### 19. Quercetin [EXTENDED]
**Confidence:** LOW  
**Completeness:** 50%  
**Justification:** Very weak affinity (Kd 80 µM, PMID 24931768), rapid dissociation, slow onset. Similar to curcumin. **Role:** Second negative control to validate that weak polyphenols show minimal API/arrest signatures.

---

## Quality Distribution Summary

| Tier | Count | % of Total | Core | Extended | Avg Completeness |
|------|-------|------------|------|----------|------------------|
| **A** | 7 | 37% | 6 | 1 | 93% |
| **B** | 5 | 26% | 3 | 2 | 78% |
| **C** | 5 | 26% | 1 | 4 | 62% |
| **D** | 2 | 11% | 0 | 2 | 50% |
| **Total** | 19 | 100% | 10 | 9 | 78% |

---

## Key Observations

### Strengths
1. **Core dataset is robust:** 90% of core compounds in Tier A or B (9/10)
2. **High PMIDs coverage:** 16/19 compounds (84%) have at least one PMID for binding data
3. **PK completeness:** 13/19 (68%) have t_half; 11/19 (58%) have Cmax
4. **Mechanistic diversity:** 8 distinct pharmacological classes represented

### Gaps (Extended Dataset)
1. **PK incompleteness:** 4/9 extended compounds missing Cmax/AUC/Vd/Clearance
2. **Estimated kinetics:** 5/9 have k_off marked as EST (needs direct measurement)
3. **Human vs animal data:** Muscimol PK is rodent-only, needs human validation
4. **Neuroimaging metrics:** Diazepam EMC/NCR are estimated, not measured

### Candidates Closest to Core Promotion
1. **Diazepam (Tier A):** Already 90% complete; needs EMC/NCR neuroimaging → **1 study away**
2. **Nalfurafine (Tier C):** Strong binding; needs Japanese clinical PK → **1 publication away**
3. **Propofol (Tier B):** Excellent data; needs direct k_off measurement → **1 kinetic study away**

---

## Recommendations for Future Data Acquisition

### HIGH PRIORITY (Core promotion candidates)
1. **Diazepam EMC/NCR:** Search "diazepam AND (fMRI OR EEG) AND (entropy OR connectivity)"
2. **Nalfurafine PK:** Search "(nalfurafine OR TRK-820) AND pharmacokinetics"
3. **Propofol k_off:** Search "propofol AND GABA-A AND (dissociation OR kinetics)"

### MODERATE PRIORITY (Validation of estimates)
4. **Everolimus/Temsirolimus Ki/Kd:** Direct mTOR binding assays (not cellular IC50)
5. **Muscimol human PK:** Case reports of *Amanita muscaria* poisoning with blood levels

### LOW PRIORITY (SAR expansion)
6. **Additional KOR agonists:** U69,593, Enadoline for structure-activity relationships
7. **Additional rapalogs:** Zotarolimus, Biolimus A9 for mTOR SAR validation
8. **Additional GABAergic:** Midazolam, Etomidate, Thiopental for arrest spectrum
9. **Adenosine analogs:** CPA, CCPA for A1/A2A selectivity studies
10. **Additional polyphenols:** EGCG as another weak comparator

---

## Validation Status

**Scripts executed:** November 14, 2025

```bash
python data_validation.py    → ✅ PASS (core 10 compounds)
python quickcheck_api.py      → ✅ PASS (API calculations correct)
```

**Conclusion:** Core dataset integrity maintained. Extended dataset acknowledged as exploratory with documented gaps.

---

## Usage Guidelines

**For researchers using this dataset:**

- **Tier A compounds:** Suitable for quantitative modeling, publication-quality analyses
- **Tier B compounds:** Suitable for exploratory analyses with caveats about specific gaps
- **Tier C compounds:** Use for hypothesis generation, SAR trends; require validation before definitive claims
- **Tier D compounds:** Conceptual/boundary cases; do not use for quantitative predictions

**For citation:**
> Lepesteur T. Molecular Arrest Framework - Data Quality Overview v1.2.0-experimental. 
> GitHub: Mythmaker28/arrest-molecules. November 2025.

---

**Document status:** ✅ CURRENT (synchronized with v1.2.0-experimental release)

