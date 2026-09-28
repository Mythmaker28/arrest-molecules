# Roadmap

This roadmap turns the current v1.1.2 research package into a clearer, more
testable, and independently reproducible project. It is based on the repository
state at commit [`e4adae4`](https://github.com/Mythmaker28/arrest-molecules/commit/e4adae4fa31d03e1fd8eed663e374a35f656d6ce),
including the [README](README.md), the
[critical review](CRITICAL_REVIEW_FINAL.md), the
[data-quality overview](Data_Package_FAIR2/DATA_QUALITY_OVERVIEW.md), and the
[candidate backlog](Data_Package_FAIR2/CANDIDATE_MOLECULES_TODO.md).

## Guardrails

- Treat the framework as exploratory until prospective validation supports it.
- Never replace missing measurements with invented values. Keep `NR`, `EST`,
  and `NA` explicit and source every promoted value.
- Keep the locked core dataset unchanged unless validation passes and the
  evidence for the change is documented.
- Separate arrest candidates from oscillatory comparators in data, analyses,
  and claims.

## Milestones

### 1. Establish one authoritative project status

Reconcile the current compound counts, version labels, quality tiers, and
release status across [README.md](README.md), [VERSION](VERSION),
[Data_Dictionary.md](Data_Package_FAIR2/Data_Dictionary.md),
[DATA_QUALITY_OVERVIEW.md](Data_Package_FAIR2/DATA_QUALITY_OVERVIEW.md),
[CANDIDATE_MOLECULES_TODO.md](Data_Package_FAIR2/CANDIDATE_MOLECULES_TODO.md),
and the two CSV datasets.

**Done when:** one documented command reports the core and extended row counts,
tier distribution, and missing-value totals; all documents that describe the
current release agree with that output.

### 2. Make validation cover every published field

Extend [data_validation.py](Data_Package_FAIR2/data_validation.py),
[validate_extended_csv.py](Data_Package_FAIR2/validate_extended_csv.py), and
[test_api_calculations.py](Data_Package_FAIR2/test_api_calculations.py) to check
schema, unique compound identifiers, allowed missing-value markers, source
identifiers, derived-value coherence, and the EMC/NCR fields highlighted as
under-tested by the critical review.

**Done when:** corrupted fixtures fail for each rule, the unmodified datasets
pass, and the full validation/test commands are recorded in CI.

### 3. Consolidate the reproducibility path

Make [run_arrest_pipeline.py](run_arrest_pipeline.py) the documented entry
point, align the root and data-package requirements, and remove contradictory
test coverage between [ci.yml](.github/workflows/ci.yml),
[python-ci.yml](.github/workflows/python-ci.yml),
[python-test.yml](.github/workflows/python-test.yml), and
[REPRO_STATUS.md](DOCS/REPRO_STATUS.md).

**Done when:** a clean Python 3.11 environment can install dependencies, run the
pipeline, validations, API calculation, and unit tests through one documented
sequence; the exact sequence is green in a pull request.

### 4. Close the highest-value evidence gaps

Work through the source-backed priorities already identified in
[CANDIDATE_MOLECULES_TODO.md](Data_Package_FAIR2/CANDIDATE_MOLECULES_TODO.md):
nalfurafine clinical PK, diazepam neuroimaging, propofol dissociation kinetics,
and direct everolimus/temsirolimus binding. Record unsuccessful searches as
negative results rather than estimates.

**Done when:** each target has either primary-source measurements with stable
identifiers and extraction notes, or a dated search log explaining why it
remains missing; no scientific value is promoted automatically.

### 5. Define and test promotion from extended to core

Turn the checklist in
[DATA_CONSOLIDATION_REPORT_NOV2025.md](DATA_CONSOLIDATION_REPORT_NOV2025.md)
into an auditable promotion procedure covering completeness, independent
sources, direct versus estimated measurements, validation, and review.

**Done when:** the procedure can evaluate a candidate without editing either
CSV, produces a human-reviewable report, and no row reaches the locked core
dataset without an explicit reviewed decision.

### 6. Prove independent reproducibility

Have a fresh environment or independent reviewer follow
[QUICKSTART.md](QUICKSTART.md) and [REPRO_STATUS.md](DOCS/REPRO_STATUS.md).
Capture runtime, dependency versions, generated artifacts, checksums, and any
manual steps. Resolve discrepancies before changing scientific conclusions.

**Done when:** a second run from a clean checkout reproduces the documented
artifacts and checksums, or every non-deterministic difference is bounded and
explained.

### 7. Validate the science before strengthening claims

Follow the priority order in
[CRITICAL_REVIEW_FINAL.md](CRITICAL_REVIEW_FINAL.md): external review by domain
experts, empirical validation of at least one proposed metric, then the
prospective experiments. Keep null or contradictory outcomes visible and revise
or abandon the framework if its key predictions fail.

**Done when:** preregistered acceptance/falsification criteria exist before new
experiments, external feedback is tracked, and manuscript claims cite the
resulting evidence rather than roadmap intent.

## Release gate

A new release is ready only when milestones included in that release have green
CI, synchronized documentation and metadata
([CITATION.cff](CITATION.cff), [.zenodo.json](.zenodo.json), release notes, and
checksums), and an explicit statement of unresolved evidence gaps.
