# Release Notes v1.1.2

**Date:** 14 novembre 2025  
**Type:** Extension de données + améliorations CI/CD

---

## 🎯 Résumé

Cette release étend le dataset avec 15 nouvelles molécules candidates dans le fichier Extended CSV, renforce la validation automatisée via CI/CD, et améliore la documentation du processus d'extension des données.

---

## ✨ Nouveautés

### 1. Extension du Dataset (Compound_Properties_Experimental_Extended.csv)

**Nouvelles molécules ajoutées (25 total, dont 15 nouvelles avec données complètes ou partielles):**

#### Agonistes KOR (Kappa-Opioid Receptor)
- **Nalfurafine** - Agoniste KOR approuvé FDA (Japon), G-protein-biased
  - K_i = 0.075 nM (PMID: 15707643)
  - Classification: Level 2-3, MODERATE
- **Mesyl Salvinorin B** - Analogue de salvinorine avec sélectivité améliorée
  - K_i = 0.6 nM (PMID: 17559236)
  - Classification: Level 2-3, MODERATE
- **U50,488** - Agoniste KOR de référence pour SAR
  - K_i = 2.4 nM (PMID: 2891264)
  - Classification: Level 2, MODERATE

#### Inhibiteurs mTOR (Rapalogs)
- **Everolimus (RAD001)** - Rapalog approuvé FDA
  - K_d = 0.6 nM, t½ = 30 h
  - Classification: Level 3, MODERATE-HIGH
- **Temsirolimus (CCI-779)** - Rapalog approuvé FDA
  - K_d = 0.8 nM, t½ = 17.3 h
  - Classification: Level 3, MODERATE
- **Ridaforolimus (AP23573)** - Rapalog Phase III
  - K_d = 0.2 nM, t½ = 48 h
  - Classification: Level 3, MODERATE

#### Modulateurs GABA-A
- **Zolpidem** - Hypnotique non-benzodiazépine, α1-sélectif
  - K_i = 20 nM (PMID: 8046346)
  - Classification: Level 2, HIGH
- **Midazolam** - Benzodiazépine à action rapide
  - K_i = 15 nM (PMID: 7636873)
  - Classification: Level 2, HIGH
- **Etomidate, Thiopental** - Anesthésiques généraux (données partielles)

#### Contrôles Négatifs
- **Curcumin** - Polyphénol multi-cibles faible affinité
  - K_i ~50 μM, classification: Level 0-1, LOW
- **Quercetin** - Flavonoïde faible activité SIRT1
  - K_i ~80 μM, classification: Level 0-1, LOW
- **EGCG** - Polyphénol du thé vert (données partielles)

#### Autres Candidats (données partielles)
- U69,593, Enadoline (CI-977), Zotarolimus (ABT-578), Biolimus A9
- N6-Cyclopentyladenosine (CPA), 2-Chloro-N6-cyclopentyladenosine (CCPA)
- Dexmedetomidine (agoniste α2-adrénergique)

### 2. Améliorations CI/CD

**Nouveau script de validation:** `Data_Package_FAIR2/validate_extended_csv.py`
- Vérifie le format des placeholders (NR, NA, ND, EST en majuscules uniquement)
- Valide la cohérence des en-têtes avec le fichier principal
- Détecte les incohérences de structure

**Pipeline CI amélioré (`.github/workflows/ci.yml`):**
- Validation automatique des placeholders et cohérence des données
- Exécution de `quickcheck_api.py` pour vérifier les calculs
- Scan de doublons (non-bloquant)
- Tests unitaires renforcés

### 3. Documentation Améliorée

**Data_Dictionary.md:**
- Section 1.1 ajoutée pour documenter `Compound_Properties_Experimental_Extended.csv`
- Règles claires pour l'utilisation des placeholders
- Politique de mouvement des données (ne pas modifier le noyau de 10 composés)

**CANDIDATE_MOLECULES_TODO.md:**
- Liste complète des molécules ajoutées avec statuts
- Références PMID et stratégies de recherche documentées
- Priorités clairement établies

---

## 🔧 Améliorations Techniques

### Validation des Données
- Script dédié `validate_extended_csv.py` pour contrôle qualité
- Vérification automatisée des formats de placeholders
- Cohérence des en-têtes garantie

### Structure des Données
- Extended CSV maintient la même structure que le fichier principal
- Placeholders standardisés: `NR` (Not Reported), `NA` (Not Applicable), `ND` (Not Determined), `EST` (Estimated)
- Séparation claire entre dataset validé (10 composés) et extensions (25 composés)

---

## 📊 Statistiques

- **Molécules totales dans Extended CSV:** 25
- **Nouvelles molécules avec données complètes:** 9 (Zolpidem, Midazolam, Nalfurafine, Mesyl Salvinorin B, U50,488, Everolimus, Temsirolimus, Ridaforolimus, Curcumin, Quercetin)
- **Molécules avec données partielles:** 15
- **PMIDs ajoutés:** 8 nouvelles références
- **Classes pharmacologiques représentées:** 6 (KOR, mTOR, GABA-A, A1, α2, multi-cibles)

---

## 🔬 Implications Scientifiques

Cette extension permet:
1. **Validation croisée** du framework d'arrest moléculaire sur des classes pharmacologiques diversifiées
2. **Comparaisons SAR** au sein des familles (rapalogs, benzodiazépines, agonistes KOR)
3. **Contrôles négatifs** robustes (curcumin, quercetin) pour établir les seuils d'arrest
4. **Gradient de puissance** allant de Level 0-1 (sub-arrest) à Level 3 (arrest profond)

---

## 📝 Notes de Migration

### Pour les utilisateurs existants
- Le dataset principal (10 composés) reste **inchangé** et reproductible
- Les scripts de validation par défaut utilisent uniquement le dataset principal
- L'Extended CSV est **optionnel** et destiné aux travaux d'extension

### Pour les contributeurs
- Suivre les règles documentées dans `Data_Dictionary.md` section 1.1
- Utiliser les placeholders en majuscules uniquement
- Ne pas modifier les lignes existantes du dataset principal
- Ajouter les PMIDs dans la colonne appropriée quand disponibles

---

## 🐛 Corrections

- Résolution des conflits git dans `Data_Dictionary.md` et `CANDIDATE_MOLECULES_TODO.md`
- Normalisation des noms de cibles (ex: "GABA-A receptor" vs "GABAA receptor")
- Correction du format des placeholders (majuscules uniquement)

---

## 🔗 Compatibilité

- **Python:** 3.8+
- **Dépendances:** Aucun changement (pandas, numpy, scipy déjà requis)
- **Rétrocompatibilité:** Totale avec v1.1.1 et v1.1.0

---

## 📦 Fichiers Modifiés

### Nouveaux fichiers
- `RELEASE_NOTES_v1.1.2.md`
- `Data_Package_FAIR2/validate_extended_csv.py`

### Fichiers mis à jour
- `VERSION` (1.1.1 → 1.1.2)
- `Data_Package_FAIR2/Compound_Properties_Experimental_Extended.csv` (10 → 25 molécules)
- `Data_Package_FAIR2/Data_Dictionary.md` (ajout section 1.1)
- `Data_Package_FAIR2/CANDIDATE_MOLECULES_TODO.md` (statuts mis à jour)
- `.github/workflows/ci.yml` (validation renforcée)

---

## 🙏 Remerciements

Cette release bénéficie des données publiées dans la littérature scientifique. Voir les PMIDs dans le CSV pour les références complètes.

---

## 📅 Prochaines Étapes (v1.2.0)

- Compléter les données manquantes pour les 15 molécules partielles
- Ajouter les structures SMILES manquantes
- Calculer les métriques API/PARI/EMC pour les nouvelles molécules
- Étendre les tests unitaires pour couvrir l'Extended CSV
- Intégrer les données de neuroimaging (NCR) quand disponibles

---

**Licence:** CC-BY 4.0  
**DOI Zenodo:** (à attribuer lors du dépôt)  
**Contact:** Voir CONTRIBUTING.md pour contribuer

