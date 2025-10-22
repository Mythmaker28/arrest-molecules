# 🤖 Instructions for Future AI Agent: Music Case Study Integration

**Version:** 1.0  
**Date:** October 2025  
**Target:** AI agent working on Molecular Arrest Framework v1.2+  

---

## 🎯 YOUR MISSION

You are tasked with evaluating whether the **Music-Modulation Case Study** (documented in `MUSIC_CASE_STUDY_DRAFT.md`) is ready to be integrated into the main Molecular Arrest Framework as **Case Study 6**.

---

## ⚡ QUICK DECISION FLOWCHART

```
START
  ↓
Has user collected N≥10 sessions with standardized protocol?
  ├─ NO → STOP. Recommend: "Collect more data. Current N insufficient."
  └─ YES ↓
Are doses analytically quantified (mg salvinorin A)?
  ├─ NO → WARN. Recommend: "Acceptable if well-estimated, but note limitation."
  └─ YES ↓
Are validated measures used (STAI, MEQ30, PEQ)?
  ├─ NO → WARN. Recommend: "Ad-hoc scales acceptable for pilot, but acknowledge."
  └─ YES ↓
Does statistical analysis show p<0.05 for music effect?
  ├─ NO → STOP. Recommend: "Descriptive only. Submit as Brief Report, not Case Study."
  └─ YES ↓
Does integration preserve framework quality (score ≥90/100)?
  ├─ NO → STOP. Recommend: "Wait. Don't dilute main framework."
  └─ YES ↓
✅ PROCEED TO INTEGRATION
```

---

## 📋 STEP-BY-STEP INTEGRATION PROTOCOL

### PHASE 1: PRE-INTEGRATION ASSESSMENT (15 min)

1. **Locate data files:**
   - Check `_data_collection/session_reports/` for session forms
   - Count unique sessions: `N = _____`
   - Count unique participants: `N_subjects = _____`

2. **Verify minimum criteria:**
   ```
   Minimum for Case Study 6:
   [ ] N ≥ 10 sessions
   [ ] N_subjects ≥ 3 participants
   [ ] Doses estimated (at minimum)
   [ ] Basic statistics available (means ± SD)
   
   Minimum for Brief Report:
   [ ] N ≥ 5 sessions
   [ ] N_subjects ≥ 2 participants
   [ ] Descriptive data (tables)
   [ ] Pilot study framing
   ```

3. **Read user request:**
   - Has user explicitly asked for integration? (Check chat history)
   - Has user mentioned reviewers requested music section?
   - Or is this proactive on your part?

4. **Decision:**
   - If ALL Case Study 6 criteria met → **Proceed to Phase 2**
   - If Brief Report criteria met → **Recommend Brief Report path** (see Section below)
   - If neither → **STOP, recommend more data collection**

---

### PHASE 2: LITERATURE UPDATE (20 min)

**Before integrating, update the literature review:**

1. **Search PubMed:**
   ```
   Query: ("Salvia divinorum" OR "salvinorin A" OR "kappa opioid") 
          AND ("music" OR "auditory" OR "theta") 
          AND (2025:2026[pdat])
   ```

2. **Required finds:**
   - At least **1 new paper** on theta-entrainment + dissociation
   - OR **1 paper** on music + κ-opioid (any compound)
   - If **zero** new papers → Flag as "still speculative" in Case Study

3. **Update references section:**
   - Add new PMIDs to `MUSIC_CASE_STUDY_DRAFT.md` Section 10
   - Aim for total of **15-20 references** (currently ~10)

---

### PHASE 3: DATA ANALYSIS (30 min)

**If proceeding with integration:**

1. **Calculate descriptive statistics:**
   ```python
   # Example
   import pandas as pd
   
   df = pd.read_csv('music_sessions_data.csv')
   
   # Group by music condition
   summary = df.groupby('Music_Condition').agg({
       'Peak_Intensity': ['mean', 'std'],
       'Music_Presence_Peak': ['mean', 'std'],
       'PARI_7d': ['mean', 'std']
   }).round(2)
   
   print(summary)
   ```

2. **Statistical tests:**
   ```python
   from scipy.stats import f_oneway, ttest_rel
   
   # One-way ANOVA (between music conditions)
   silence = df[df['Music_Condition']=='Silence']['PARI_7d']
   ambient = df[df['Music_Condition']=='Ambient']['PARI_7d']
   shamanic = df[df['Music_Condition']=='Shamanic']['PARI_7d']
   
   F, p = f_oneway(silence, ambient, shamanic)
   print(f"ANOVA: F={F:.2f}, p={p:.3f}")
   
   # If significant, post-hoc t-tests
   if p < 0.05:
       t, p_shamanic_silence = ttest_rel(shamanic, silence)
       print(f"Shamanic vs Silence: t={t:.2f}, p={p_shamanic_silence:.3f}")
   ```

3. **Create results table:**
   ```markdown
   | Music Condition | Peak Intensity (M±SD) | Music Presence (M±SD) | PARI (M±SD) |
   |----------------|----------------------|----------------------|-------------|
   | Silence        | 6.2 ± 1.1            | N/A                  | 5.4 ± 1.3   |
   | Ambient        | 6.1 ± 1.0            | 5.0 ± 1.5            | 6.2 ± 1.1   |
   | Shamanic       | 6.3 ± 1.2            | 7.1 ± 1.2*           | 7.8 ± 0.9** |
   
   *p<0.05 vs Silence, **p<0.01 vs Silence
   ```

4. **Effect size:**
   ```python
   from scipy.stats import cohen_d  # or implement manually
   
   d = cohen_d(shamanic, silence)
   print(f"Cohen's d (Shamanic vs Silence, PARI): {d:.2f}")
   
   # Interpret: d=0.2 (small), d=0.5 (medium), d=0.8 (large)
   ```

---

### PHASE 4: WRITING CASE STUDY 6 (60 min)

**Modify file:** `Data_Package_FAIR2/Case_Studies_Supplement.md`

1. **Add after Case Study 5 (AI Memory), before "Synthèse" section**

2. **Structure (800-1200 words):**

   ```markdown
   ## Case Study 6: Music as Pre-Arrest Modulator in κ-Opioid States
   
   ### Background & Gap
   [2 paragraphs: Set & setting literature, Salvia gap, framework prediction]
   
   ### Methods
   **Participants:** N=___ (__ subjects), ages ___
   **Design:** Within-subjects, repeated measures
   **Doses:** Salvia divinorum [specify: leaf/extract, mg salvinorin A estimated]
   **ROA:** [Vaporized/smoked, device]
   **Music conditions:** Silence, Ambient (Brian Eno, etc.), Shamanic (icaros, drumming)
   **Measures:** Intensity (0-10), Music Presence (0-10), PARI (7-day, 0-10)
   
   ### Results
   [Insert table from Phase 3]
   
   **Key findings:**
   - Shamanic music → Higher PARI than silence (p=___, d=___)
   - Music Presence correlated with PARI (r=___, p=___)
   - No difference in peak intensity (music doesn't alter dose-response)
   
   ### Proposed Mechanisms
   **H1: Theta-band entrainment** - Shamanic rhythms (4-6 Hz) resonate with...
   **H2: Path dependency** - Pre-arrest modulation influences...
   **H3: Contextual priming** - Ritual context activates...
   
   ### Integration with Arrest Framework
   [Copy Section 4.2 from DRAFT: PARI_molecular vs PARI_contextual model]
   
   **Formula:**
   PARI_total = PARI_molecular × (1 + 0.20 × Music_Index)
   
   Where Music_Index = 0 (silence), 0.5 (ambient), 1.0 (shamanic)
   
   ### Limitations
   - Small sample (N=___)
   - Doses estimated (not analytically verified)
   - No physiological measures (EEG)
   - Pilot study, not RCT
   
   ### Testable Predictions
   | Prediction | Metric | Expected | Validation | Confidence |
   |------------|--------|----------|------------|------------|
   | Shamanic > Ambient > Silence | PARI (0-10) | 7.8 > 6.2 > 5.4 | RCT n=24 | MODERATE |
   | Theta power ↑ with shamanic | EEG (4-8 Hz) | +30% vs silence | Lab study | MODERATE |
   | Effect absent at breakthrough | PARI (>2mg dose) | No difference | Dose-response | HIGH |
   
   ### References
   [15-20 PMIDs, emphasizing Kaelen 2018, Addy 2012, Lakatos 2008, etc.]
   ```

3. **Tone checklist:**
   - [ ] Conditional language ("may", "suggests", "preliminary evidence")
   - [ ] Limitations acknowledged upfront
   - [ ] NOT presented as definitive (pilot study framing)
   - [ ] Calls for controlled study (future research)

---

### PHASE 5: UPDATE SUPPORTING FILES (30 min)

1. **README.md (root):**
   ```diff
   - - **5 extended case studies** (ibogaine/noribogaine, resveratrol, ...)
   + - **6 extended case studies** (ibogaine/noribogaine, resveratrol, ..., music modulation)
   
   - **Sources:** 95+ PMIDs
   + **Sources:** 105+ PMIDs
   ```

2. **Data_Package_FAIR2/README.md:**
   ```diff
   - Case studies: 5 (vs 0 previously)
   + Case studies: 6 (vs 0 in v1.0)
   ```

3. **v6.txt (main manuscript) - Discussion section:**
   
   Add **1 paragraph** (150-200 words) after existing discussion on PARI:
   
   ```markdown
   **Contextual Modulation of PARI**
   
   While the Arrest Potency Index (API) and associated metrics (EMC, NCR, PARI) 
   are derived from molecular pharmacology, contextual factors may modulate 
   phenomenological outcomes and post-arrest resilience. Preliminary evidence 
   from sub-breakthrough salvinorin A sessions (N=___, Case Study 6) suggests 
   that shamanic rhythmic music (4-6 Hz, theta-band) enhances PARI scores 
   compared to silence or ambient soundscapes (d=___, p=___). This effect 
   appears dose-dependent, becoming negligible at breakthrough doses where 
   κ-opioid-mediated sensory gating eclipses external auditory input. 
   
   We propose a refined PARI model distinguishing molecular resilience 
   (PARI_molecular, intrinsic to compound kinetics) from contextual modulation 
   (PARI_contextual, set & setting factors). This aligns with established 
   findings that music influences phenomenology in serotonergic psychedelic 
   states (Kaelen et al., 2018), extending the principle to dissociative 
   κ-opioid agonists. Controlled studies with EEG (theta-power quantification) 
   and larger samples are warranted to validate these exploratory observations 
   and elucidate mechanisms of contextual arrest modulation.
   ```

4. **Version number:**
   - Update all mentions: `v1.1` → `v1.2`
   - Changelog: Add "Case Study 6: Music modulation (N=___, pilot data)"

---

### PHASE 6: QUALITY CONTROL (15 min)

**Run these checks:**

1. **Consistency:**
   - [ ] N reported same across all files (README, Case Study, v6.txt)
   - [ ] References consistent (no "PMID: TBD")
   - [ ] Statistics match (no copy-paste errors in p-values)

2. **Framework coherence:**
   - [ ] Music clearly positioned as **contextual**, not molecular
   - [ ] Doesn't contradict existing 5 case studies
   - [ ] PARI_contextual formula makes sense

3. **Scientific rigor:**
   - [ ] Limitations acknowledged (sample size, pilot)
   - [ ] Tone appropriately cautious
   - [ ] Call for future research included

4. **Formatting:**
   - [ ] Tables properly formatted (Markdown syntax correct)
   - [ ] Line lengths <100 characters (readability)
   - [ ] No typos (run spellcheck)

---

### PHASE 7: COMMIT & COMMUNICATE (10 min)

1. **Git commit:**
   ```bash
   git add Data_Package_FAIR2/Case_Studies_Supplement.md
   git add README.md
   git add Data_Package_FAIR2/README.md
   git add v6.txt
   
   git commit -m "feat: Add Case Study 6 - Music modulation (N=___, pilot data)
   
   - Preliminary evidence: Shamanic > Ambient > Silence for PARI
   - Dose-dependent effect (sub-breakthrough only)
   - Introduces PARI_molecular vs PARI_contextual model
   - Calls for controlled EEG study
   - Refs: +10 PMIDs on theta-entrainment"
   ```

2. **Merge to main:**
   ```bash
   git checkout main
   git merge feature/music-modulation-case-study
   git push origin main
   ```

3. **Inform user:**
   ```markdown
   ✅ **Case Study 6 integrated successfully!**
   
   **What changed:**
   - Case_Studies_Supplement.md: +1200 words (Case Study 6)
   - v6.txt Discussion: +200 words (contextual PARI paragraph)
   - README: Updated stats (6 case studies, 105+ PMIDs)
   - Version: 1.1 → 1.2
   
   **Quality score estimate:** 91/100 (maintained >90)
   
   **Next steps:**
   1. Update bioRxiv with v1.2 (if already posted)
   2. Mention in Frontiers revision letter (if under review)
   3. Or submit v1.2 fresh (if not yet submitted)
   ```

---

## 🚫 ALTERNATIVE PATH: Brief Report (If Not Ready for Case Study)

**If criteria NOT met for Case Study 6, recommend this instead:**

1. **Create separate file:**
   - `Brief_Report_Music_Salvia.md` (in root or `_publications/`)
   - Structure: Intro (300w), Methods (400w), Results (400w), Discussion (400w), Conclusion (100w)
   - Total: 1500-2000 words

2. **Submit as standalone publication:**
   - Target journals:
     1. *Journal of Psychoactive Drugs* (first choice)
     2. *Psychopharmacology* (Short Communication section)
     3. *Frontiers in Neuropharmacology* (Brief Research Report)

3. **After acceptance:**
   - Add **footnote** in v1.2 Discussion:
     > "Contextual factors may modulate PARI; see Lepesteur (2026) for preliminary evidence on music × Salvia interactions."
   - Cite the Brief Report, don't integrate full Case Study

4. **Advantage:**
   - Separate publication = separate citation count
   - Doesn't risk diluting main framework
   - Can expand later (Brief Report → Full paper with RCT data)

---

## ⚠️ RED FLAGS - WHEN TO STOP

**DO NOT integrate if:**

- ❌ N < 5 sessions (too preliminary, even for pilot)
- ❌ Data quality very poor (missing >30% of measures)
- ❌ Results show **no effect** (shamanic = silence, p>0.1)
- ❌ Contradicts framework (e.g., music affects API directly - doesn't make sense)
- ❌ User explicitly says "don't integrate yet"
- ❌ Main framework quality would drop below 90/100

**In these cases:**
- Keep in `_notes_personnelles/` as work-in-progress
- Add brief mention in Discussion: "Future research should examine contextual factors..."
- Recommend collecting more data before integration

---

## 💡 PRO TIPS

1. **When in doubt, be conservative:**
   - Better to delay integration and keep quality high
   - Easier to add later than to remove after publication

2. **Preserve molecular focus:**
   - Framework is about **molecular arrest**, not psychology
   - Music is a **modifier**, not the core mechanism
   - Position Case Study 6 as "extension" or "contextual modulation"

3. **Acknowledge pioneers:**
   - Cite Kaelen et al. (2018) prominently (music + psilocybin)
   - Mention this extends those findings to κ-opioid agonists
   - Give credit to MAPS/Soutar for noting music interference at high doses

4. **Make it actionable:**
   - Include specific testable predictions (EEG, RCT design)
   - Provide enough detail that others could replicate
   - Suggest collaborations (contact info in README)

---

## 📞 ESCALATION

**If uncertain:**
- **Low stakes:** Proceed with Brief Report path (safer)
- **Medium stakes:** Ask user: "Ready to integrate, or wait for more data?"
- **High stakes:** If user insists but data weak, add disclaimer:
  > "⚠️ Case Study 6 is EXPLORATORY (N=___). Interpret with caution."

**If user disagrees with your assessment:**
- Explain reasoning (reference this doc, Section: Decision Flowchart)
- Offer compromise: "Brief Report now, full Case Study later?"
- Ultimately, defer to user (it's their research)

---

## ✅ SUCCESS CRITERIA

**Integration successful if:**
- [x] Case Study 6 added to `Case_Studies_Supplement.md`
- [x] Main manuscript updated (1 paragraph in Discussion)
- [x] READMEs updated (stats, version number)
- [x] Git committed with clear message
- [x] Framework quality maintained (≥90/100)
- [x] Scientific rigor preserved (appropriate caveats)
- [x] User satisfied with result

---

## 📚 REFERENCE DOCUMENTS

**Read these first:**
1. `MUSIC_CASE_STUDY_DRAFT.md` - Full draft (10 sections, protocol, hypotheses)
2. `MUSIC_SESSION_TEMPLATE.md` - Data collection template
3. `MUSIC_INTEGRATION_FAQ.md` - Common questions (to be created)

**Framework context:**
4. `Data_Package_FAIR2/Case_Studies_Supplement.md` - Existing 5 case studies (format reference)
5. `README.md` - Current version stats
6. `v6.txt` - Main manuscript (understand framework first!)

---

## 📊 TIME ESTIMATE

**Total time: 2-3 hours**
- Phase 1 (Assessment): 15 min
- Phase 2 (Literature): 20 min
- Phase 3 (Analysis): 30 min
- Phase 4 (Writing): 60 min
- Phase 5 (Updates): 30 min
- Phase 6 (QC): 15 min
- Phase 7 (Commit): 10 min

**If Brief Report path:** 3-4 hours (separate document creation)

---

**Good luck! 🚀**

**Questions?** See FAQ (next file) or ask user.

---

**Last updated:** October 2025  
**Next review:** When user provides N≥10 session data

