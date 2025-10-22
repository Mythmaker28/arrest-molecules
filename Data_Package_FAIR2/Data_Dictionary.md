# Data Dictionary - Molecular Arrest Framework

**Version:** 1.1  
**Date:** October 2025  
**Author:** Tommy Lepesteur  
**License:** CC-BY 4.0  

---

## Overview

Ce dictionnaire de données définit toutes les variables et colonnes utilisées dans le package de données Molecular Arrest Framework. Les définitions incluent les unités, types de données, plages valides, et méthodes de mesure.

---

## 1. Compound_Properties_Database.csv

Propriétés pharmacologiques et physicochimiques pour 6 composés paradigmatiques.

| Colonne | Description | Unités | Type | Plage valide | Exemple | Méthode/Source |
|---------|-------------|--------|------|--------------|---------|----------------|
| **Compound_Name** | Nom chimique du composé | — | String | — | Salvinorin A | Nomenclature IUPAC ou nom commun |
| **CAS_Number** | Numéro d'enregistrement Chemical Abstracts Service | — | String | Format: NNNNNN-NN-N | 83729-01-5 | CAS Registry |
| **SMILES** | Simplified Molecular-Input Line-Entry System | — | String | Syntaxe SMILES valide | COC(=O)[C@]12... | ChemDraw/PubChem |
| **Molecular_Formula** | Formule moléculaire brute | — | String | Format: C_nH_nO_nN_n | C23H28O8 | Analyse élémentaire |
| **Molecular_Weight** | Masse moléculaire | g/mol | Numeric | 100–2000 | 432.47 | Somme masses atomiques |
| **LogP** | Coefficient de partition octanol-eau (log) | — | Numeric | –5 to +10 | 2.73 | Méthode shake-flask ou calculé (ChemDraw) |
| **Rotatable_Bonds** | Nombre de liaisons librement rotatives | — | Integer | 0–50 | 3 | Définition Lipinski (liaisons simples non cycliques) |
| **Primary_Target** | Cible moléculaire principale | — | String | — | Kappa-opioid receptor | Littérature pharmacologique |
| **Target_Gene** | Symbole du gène codant la cible | — | String | Nomenclature HGNC | OPRK1 | NCBI Gene Database |
| **K_i_nM** | Constante d'inhibition | nM | Numeric | 0.001–100000 | 1.8 | Essai de liaison radioligand (compétition) |
| **K_i_Source_PMID** | PubMed ID de la source K_i | — | Integer | PMID valide | 12202542 | PubMed |
| **K_d_nM** | Constante de dissociation à l'équilibre | nM | Numeric | 0.001–100000 | 1.8 | Cinétique de liaison ou équilibre thermodynamique |
| **k_off_per_min** | Constante de vitesse de dissociation | min⁻¹ | Numeric | 0.0001–10 | 0.04 | Cinétique de dissociation (surface plasmon resonance ou radioligand) |
| **tau_residence_min** | Temps de résidence sur la cible (1/k_off) | min | Numeric | 0.1–10000 | 25 | Calculé : τ = 1/k_off |
| **tau_method** | Méthode de détermination de τ | — | String | Enum: Literature k_off / Estimated from duration / Calculated | Estimated from duration | Description méthodologique |
| **t_onset_min** | Temps d'apparition de l'effet (50% max) | min | Numeric | 0.1–10000 | 1 | Pharmacodynamie : temps jusqu'à 50% E_max |
| **t_onset_method** | Méthode de détermination t_onset | — | String | — | Subjective onset | Description source (humain/cellulaire/animal) |
| **EC50_nM** | Concentration efficace médiane | nM | Numeric | 0.001–100000 | 2 | Essai fonctionnel dose-réponse (courbe sigmoïde) |
| **EC50_Assay** | Type d'essai fonctionnel pour EC50 | — | String | — | GIRK activation | Description du bioassay |
| **t_half_plasma_h** | Demi-vie plasmatique | h | Numeric | 0.01–1000 | 0.15 | Pharmacocinétique : décroissance [plasmatique] |
| **Cmax_ng_mL** | Concentration plasmatique maximale | ng/mL | Numeric | 0.1–100000 | 2.4 | PK humaine ou animale (dosage HPLC/MS) |
| **AUC_ng_h_mL** | Aire sous courbe concentration-temps | ng·h/mL | Numeric | 1–1000000 | 15 | Intégration courbe PK |
| **Vd_L_kg** | Volume de distribution | L/kg | Numeric | 0.01–100 | 3.2 | Calculé : dose/C0 ou modèle PK compartimental |
| **Clearance_L_h_kg** | Clairance systémique | L/h/kg | Numeric | 0.001–100 | 12.5 | Calculé : dose/AUC |
| **Protein_Binding_percent** | Liaison aux protéines plasmatiques | % | Numeric | 0–100 | 89 | Ultrafiltration ou dialyse à l'équilibre |
| **API_absolute** | Arrest Potency Index (absolu) | nM⁻² | Numeric | 0.000001–10000 | 6.95 | Calculé : [(1/K_d)×τ]/[t_onset×EC₅₀] |
| **API_relative** | API normalisé (salvinorin A = 1.0) | — | Numeric | 0.00001–10 | 1.00 | API_absolu / API_salvinorin_A |
| **API_CI_lower** | Borne inférieure IC 95% (Monte Carlo) | — | Numeric | — | 0.85 | Percentile 2.5% simulation Monte Carlo (10k itérations) |
| **API_CI_upper** | Borne supérieure IC 95% (Monte Carlo) | — | Numeric | — | 1.15 | Percentile 97.5% simulation Monte Carlo |
| **AKR** | Arrest Kinetics Ratio (τ_arrest/τ_recovery) | — | Numeric | 0.01–100 | 1.5 | Ratio durée arrest / durée récupération |
| **EMC** | Entropy Modulation Coefficient | — | Numeric | –1.0 to +1.0 | –0.4 | (Complexité_traitement – Complexité_baseline) / Complexité_baseline |
| **NCR_percent** | Network Connectivity Reduction | % | Numeric | –100 to +100 | 50 | [(C_baseline – C_traitement) / C_baseline] × 100% |
| **PARI** | Post-Arrest Resilience Index | — | Numeric | –1.0 to +5.0 | 0.3 | (Performance_post-arrest – Performance_baseline) / Performance_baseline |
| **Arrest_Level** | Classification niveau arrest (1/2/3) | — | String | Enum: Level 1 / Level 2 / Level 3 | Level 3 | Basé sur seuils EMC/NCR/PARI |
| **Confidence_Grade** | Grade de confiance global | — | String | Enum: VERY HIGH / HIGH / MODERATE / LOW | MODERATE | Basé sur qualité paramètres (K_d, τ, t_onset, EC50) |
| **Clinical_Status** | Statut clinique/réglementaire | — | String | Enum: FDA approved / Phase III / Research only / OTC / Supplement | Research only | Statut réglementaire actuel |

### Encodage des données manquantes

- **NA** : Non applicable (ex: EMC pour composés non-neuraux)
- **ND** : Non déterminé (mesure non encore effectuée)
- **NR** : Non rapporté dans la littérature
- **EST** : Estimé (valeur non directement mesurée)

---

## 2. Confidence_Grading_Matrix.csv

Évaluation de confiance pour 44 prédictions quantitatives.

| Colonne | Description | Type | Valeurs possibles | Exemple |
|---------|-------------|------|-------------------|---------|
| **Category** | Catégorie de prédiction | String | Structural_Signatures / Entropy_Metrics / Connectivity_Metrics / Resilience_Metrics / Oscillatory_Predictions / Clinical_Predictions / API_Metrics / SAR_Predictions | Structural_Signatures |
| **Specific_Prediction** | Description spécifique de la prédiction | String | Texte libre | Rigidity-API correlation R² > 0.6 |
| **Value_or_Range** | Valeur prédite ou plage | String | Numérique, plage, ou qualitatif | 0.71 (SalA series) |
| **Evidence_Type** | Type de preuve supportant la prédiction | String | Texte libre décrivant source | 1 scaffold (N=8 analogs) |
| **Confidence_Level** | Niveau de confiance attribué | String | High / Moderate / Low / Very High | Moderate |
| **Validation_Required** | Validation expérimentale nécessaire | String | Description protocole | Extend to ≥3 scaffolds |
| **PMID_References** | PubMed IDs supportant la prédiction | String | PMIDs séparés par ";" ou "Multiple" / "Predicted" | Multiple |

### Critères de classification des niveaux de confiance

**High/Very High:**
- Mesure expérimentale directe chez l'espèce cible (humains/primates)
- ≥3 réplications indépendantes
- Clarté mécanistique établie
- Données publiées dans journaux à comité de lecture

**Moderate:**
- Mesure indirecte (données rongeurs extrapolées, bioassays comme proxies)
- 1–2 études supportant
- Incertitudes mécanistiques résolues partiellement

**Low:**
- Extrapolation multi-niveaux (ex: distribution KOR + mécanisme GIRK + données dissociatives → connectivité DMN prédite)
- Étude préliminaire unique
- Mécanismes contestés ou non élucidés

---

## 3. Experimental_Protocols_Summary.csv

Résumé des protocoles expérimentaux proposés et des entités de données.

| Colonne | Description | Type | Exemple |
|---------|-------------|------|---------|
| **Experiment_ID** | Identifiant unique de l'expérience | String | Exp1_Neuroimaging |
| **Section_Reference** | Référence section manuscrit | String | Section 4.2.1 |
| **Entity_Type** | Type d'entité (étude/données/code) | String | Human neuroimaging study |
| **File_Source** | Fichier source contenant détails | String | v6.txt lines 1000-1050 |
| **Description** | Description courte | String | Salvinorin A vs psilocybin entropy comparison |
| **Status** | Statut actuel | String | Proposed / Complete / Draft |
| **Sample_Size** | Taille échantillon | String | 36 / 6 compounds / N/A |
| **Power_Calculation** | Calcul de puissance statistique | String | α=0.05 β=0.20 d=1.2 |
| **Statistical_Analysis** | Méthode statistique | String | Between-subjects t-test |
| **Primary_Outcome** | Mesure de résultat primaire | String | Entropy Modulation Coefficient |
| **Secondary_Outcomes** | Mesures secondaires | String | Network connectivity & subjective effects |
| **Success_Criteria** | Critères de succès | String | Salvinorin EMC<-0.2 AND psilocybin EMC>+0.2 |
| **Falsification_Criteria** | Critères de réfutation | String | EMC indistinguishable (p>0.05) |
| **Estimated_Cost_USD** | Coût estimé en USD | Integer | 450000 |
| **Estimated_Duration_Months** | Durée estimée en mois | Integer | 18 |
| **IRB_Required** | Approbation IRB requise | String | Yes / No |
| **Special_Licenses** | Licences spéciales nécessaires | String | DEA Schedule I research license |
| **Contact_Email** | Email de contact | String | tommy.lepesteur@hotmail.fr |
| **Version** | Version du protocole | String | 1.0 |
| **Last_Updated** | Date dernière mise à jour | String | 2025-10-21 |

---

## 4. Outputs Python (Python_Code_API_Monte_Carlo.py)

Le script Python génère plusieurs outputs :

### 4.1 Fichiers CSV générés

**API_Comparison_All_Compounds.csv**

| Colonne | Description | Type | Unités |
|---------|-------------|------|--------|
| Compound | Nom du composé | String | — |
| API | API médian (Monte Carlo) | Numeric | Relatif à salvinorin A |
| CI_Lower | Borne inférieure IC 95% | Numeric | Relatif |
| CI_Upper | Borne supérieure IC 95% | Numeric | Relatif |
| Confidence | Grade de confiance | String | VERY HIGH/HIGH/MODERATE/LOW |

### 4.2 Graphiques PNG générés

- **API_Distribution_[Compound].png** : Histogramme + Q-Q plot pour chaque composé
- **API_Comparison_All_Compounds.png** : Barres comparatives avec barres d'erreur

---

## 5. Outputs R (R_Code_Figures_S2.R)

### 5.1 Figures générées

**Figure_S2_Oscillatory_Advantage.png / .tiff**
- 3 panneaux (A: moléculaire, B: cellulaire, C: clinique)
- 300 dpi, dimensions 10×14 pouces

### 5.2 Métadonnées JSON

**Figure_S2_data.json**

Structure JSON contenant paramètres des 3 panneaux et métadonnées (auteur, version, licence).

---

## 6. Conventions générales

### 6.1 Formats de fichiers

- **CSV** : UTF-8, séparateur virgule, header en ligne 1
- **JSON** : UTF-8, pretty-printed (indentation 2 espaces)
- **PNG** : RGB, 300 dpi minimum
- **TIFF** : RGB, compression LZW, 300 dpi

### 6.2 Nomenclature

- **Composés** : Noms communs (Salvinorin A) ou IUPAC
- **Gènes** : Symboles HGNC (OPRK1, MTOR)
- **Unités** : Système international (nM, min, h, mg/kg)

### 6.3 Précision numérique

- **Concentrations** : 2–3 chiffres significatifs (1.8 nM, 0.12 nM)
- **Ratios/indices** : 2–4 décimales (API = 1.00, PARI = 0.3)
- **Pourcentages** : Entiers ou 1 décimale (41%, 30.5%)

### 6.4 Codes manquants

Utiliser codes standardisés (NA, ND, NR, EST) plutôt que cellules vides ou zéros.

---

## 7. Contrôle qualité

### 7.1 Validation des données

- Plages valides vérifiées pour chaque colonne numérique
- Cohérence entre K_d et K_i (typiquement égaux pour agonistes complets)
- Cohérence τ = 1/k_off (tolérance ±5%)
- PMIDs vérifiés comme valides sur PubMed

### 7.2 Traçabilité

- Chaque valeur pharmacologique tracée jusqu'à PMID source
- Méthodes d'estimation documentées (champ *_method)
- Versions des databases externes enregistrées (ChEMBL v31, DrugBank 5.1.10)

### 7.3 Reproductibilité

- Seed Monte Carlo fixe (seed=42) pour résultats reproductibles
- Code R/Python versionné et archivé
- Environnements documentés (R version, packages, Python version)

---

## 8. Contact et support

**Auteur :** Tommy Lepesteur  
**Email :** tommy.lepesteur@hotmail.fr  
**ORCID :** 0009-0009-0577-9563  
**Repo GitHub :** https://github.com/Mythmaker28/arrest-molecules  

Pour questions sur le dictionnaire ou signaler erreurs, ouvrir un issue sur GitHub ou contacter par email.

---

## 9. Historique des versions

| Version | Date | Changements |
|---------|------|-------------|
| 1.1 | 2025-10-21 | Ajout 4 nouveaux composés (ibogaine, noribogaine, psilocybin, LSD), 44 prédictions |
| 1.0 | 2025-10-21 | Version initiale accompagnant soumission manuscrit (6 composés, 42 prédictions) |

---

**Licence:** Ce dictionnaire est publié sous CC-BY 4.0. Vous êtes libre de le partager et l'adapter avec attribution appropriée.

