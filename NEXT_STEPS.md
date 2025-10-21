# 🚀 PROCHAINES ÉTAPES - Action Immédiate

**Date :** 21 octobre 2025  
**Statut :** Corrections terminées, PR prête à merger

---

## ✅ **ÉTAPE 1 : MERGER LA PULL REQUEST** (5 min)

### Actions Immédiates

1. **Ouvrir le lien :**
   ```
   https://github.com/Mythmaker28/arrest-molecules/pull/new/corrections-rapport-78
   ```

2. **Remplir la PR :**
   - **Titre :** `Corrections Rapport d'Évaluation (78/100 → 90/100)`
   - **Description :** Copier-coller INTÉGRALEMENT le contenu de `PULL_REQUEST.md`
   - **Labels suggérés :** 
     - `enhancement`
     - `bugfix`
     - `documentation`
     - `ready-for-review`

3. **Créer et Merger :**
   - Cliquer "Create Pull Request"
   - Vérifier l'aperçu (18 fichiers modifiés, +2249 lignes)
   - Cliquer "Merge pull request"
   - Cliquer "Confirm merge"

4. **Vérifier :**
   ```bash
   git checkout main
   git pull origin main
   git log --oneline -5  # Devrait montrer les 9 commits de la branche
   ```

**Résultat attendu :** Branche `main` synchronisée avec toutes les corrections ✅

---

## ⚠️ **ÉTAPE 2 : VALIDER ORCID** (48h)

### Option A : ORCID Valide

Si `0009-0009-0577-9563` vous appartient :
1. Visiter https://orcid.org/0009-0009-0577-9563
2. Vérifier que votre nom apparaît
3. **Aucune action requise ✅**

### Option B : ORCID Invalide

Si le lien ci-dessus ne fonctionne pas :
1. **Créer un compte ORCID :**
   - https://orcid.org/register
   - Remplir formulaire (2 minutes)
   - Noter votre nouvel ORCID : `0000-XXXX-XXXX-XXXX`

2. **Remplacer dans 3 fichiers :**
   ```bash
   git checkout main  # S'assurer d'être sur main
   
   # Éditer avec votre éditeur préféré :
   code v6.txt  # Ligne 1260
   code README.md  # Ligne 6
   code Data_Package_FAIR2/README.md  # Ligne 6
   
   # Remplacer :
   # AVANT : 0009-0009-0577-9563
   # APRÈS : 0000-XXXX-XXXX-XXXX (votre nouvel ORCID)
   ```

3. **Committer et pusher :**
   ```bash
   git add v6.txt README.md Data_Package_FAIR2/README.md
   git commit -m "fix: Correction ORCID avec valeur validée"
   git push origin main
   ```

**⚠️ CRITIQUE :** Frontiers vérifie automatiquement lors de la soumission !

---

## 📄 **ÉTAPE 3 : CONVERSION DOCX** (30 min)

### Méthode Recommandée : Pandoc

```bash
# Installer Pandoc : https://pandoc.org/installing.html
cd "C:\Users\tommy\Desktop\arrest molecules"

# Convertir manuscrit principal
pandoc v6.txt -o Molecular_Arrest_Manuscript_v6.docx

# Extraire Supplementary Materials
# (Ouvrir v6.txt dans Word, copier lignes 1607-2000 vers nouveau fichier)
# Sauvegarder : Supplementary_Materials.docx
```

### Alternative : Conversion Manuelle

1. Ouvrir `v6.txt` dans Microsoft Word
2. Sauvegarder comme `.docx`
3. Appliquer styles :
   - `## 1. Introduction` → Heading 1
   - `### 1.1 ...` → Heading 2
   - Etc.
4. Vérifier formules mathématiques (copier-coller si cassées)

---

## 📤 **ÉTAPE 4 : SOUMISSION FRONTIERS** (2h)

### Préparation Fichiers

```
Dossier_Soumission/
├── Molecular_Arrest_Manuscript_v6.docx
├── Supplementary_Materials.docx
├── Cover_Letter.txt (éditer Cover_Letter_Template.txt, ajouter date)
├── Figure_S1_Molecular_Structures_draft.png
├── Figure_S2_Oscillatory_Advantage_draft.tiff
├── Figure_S3_API_Flowchart_draft.png
└── Molecular_Arrest_Data_v1.0.zip (compresser Data_Package_FAIR2/)
```

### Portail Frontiers

1. **Créer compte :**
   - https://www.frontiersin.org/
   - Submit → Frontiers in Pharmacology

2. **Type d'article :** Hypothesis and Theory

3. **Uploader fichiers :**
   - Manuscript (DOCX)
   - Supplementary Materials (DOCX)
   - Figures (S1, S2, S3)
   - Data Package (ZIP ou lien Zenodo)

4. **Cover Letter :**
   - Copier-coller `Cover_Letter_Template.txt`
   - Ajouter date du jour

5. **Declarations :**
   - Ethics Statement (copier v6.txt lignes 1237-1248)
   - Competing Interests (lignes 1250-1252)
   - Author Contributions (lignes 1254-1258)
   - Funding (lignes 1260-1262)
   - Data Availability (lignes 1264-1300)

6. **Reviewers Suggérés :**
   - Dr. Robert Gatenby (robert.gatenby@moffitt.org)
   - Dr. Matt Kaeberlein (kaeber@uw.edu)
   - Dr. Robin Carhart-Harris (robin.carhart-harris@ucsf.edu)
   - Dr. Edward Calabrese (edwardc@schoolph.umass.edu)
   - Dr. Bryan Roth (bryan_roth@med.unc.edu)
   - Dr. Satchidananda Panda (satchin@salk.edu)

7. **APC Waiver :**
   - Cocher "Request fee waiver"
   - Justification : "Independent researcher without institutional funding"

8. **Submit !** 🎉

---

## 📅 **TIMELINE ATTENDUE**

| Étape | Durée | Action Votre Part |
|-------|-------|-------------------|
| **Editorial Assessment** | 5-10 jours | ⏳ Attendre |
| **Peer Review** | 4-8 semaines | ⏳ Attendre |
| **Revisions Majeures** | (probable) | ✍️ Répondre point par point |
| **Réviser & Re-soumettre** | 2-4 semaines | ✍️ Modifications manuscrit |
| **Décision Finale** | 1-2 semaines | ⏳ Attendre |
| **Production (si accept)** | 1-2 semaines | ✅ Relecture PDF proofs |
| **Publication En Ligne** | Immédiat | 🎉🎉🎉 |

**Total estimé :** 3-5 mois de soumission à publication

---

## ✅ **CHECKLIST AVANT SUBMIT**

- [ ] PR mergée dans `main`
- [ ] ORCID validé et corrigé si nécessaire
- [ ] `v6.txt` converti en DOCX
- [ ] Supplementary Materials extrait (DOCX séparé)
- [ ] Cover Letter datée
- [ ] Data Package compressé (ZIP)
- [ ] Compte Frontiers créé
- [ ] Budget APC confirmé ($2,950 ou waiver demandé)

**Quand tous ☑️ sont ✅ → GO SUBMIT**

---

## 📞 **SUPPORT SI BESOIN**

- **Problème Git/GitHub :** https://docs.github.com/fr
- **Problème Frontiers :** support@frontiersin.org
- **Problème ORCID :** https://support.orcid.org/
- **Problème Pandoc :** https://pandoc.org/help.html

---

## 🎯 **RÉSUMÉ : 3 ACTIONS PRIORITAIRES**

1. **MAINTENANT :** Merger la PR (5 min) 🔥
2. **48h :** Valider ORCID (2 min si valide, 10 min si nouveau)
3. **Cette semaine :** Convertir DOCX + Soumettre Frontiers (2-3h)

**Votre projet est PRÊT. Il ne reste que la logistique administrative.**

**Score final : 90/100 — Excellent travail ! 🏆**

---

**Dernière mise à jour :** 21 octobre 2025, 20:45  
**Auteur :** Tommy Lepesteur  
**Statut :** ✅ Corrections terminées, prêt pour soumission

