# Guide de Contribution - Molecular Arrest Framework

Merci de votre intérêt pour contribuer au projet Molecular Arrest Framework !

## 🎯 Types de Contributions Acceptées

### ✅ Bienvenues
- **Ajout de nouveaux composés** avec données pharmacologiques complètes (K_d, τ, t_onset, EC₅₀) et PMIDs sources
- **Corrections de bugs** dans le code Python/R (avec tests)
- **Améliorations documentation** (clarifications, exemples, traductions)
- **Suggestions de métriques** additionnelles (avec justification théorique)
- **Validation expérimentale** des prédictions (données primaires requises)

### ⚠️ Discussions Requises Avant PR
- Changements majeurs aux métriques (API, EMC, NCR, AKR, PARI)
- Modifications des seuils (Level 1/2/3)
- Ajout de nouvelles dépendances logicielles

### ❌ Non Acceptées
- Données sans sources (PMIDs obligatoires)
- Modifications rétrospectives des résultats publiés
- Composés sans cibles moléculaires clairement identifiées

---

## 📋 Processus de Contribution

### 1. Fork & Clone
```bash
git clone https://github.com/VOTRE_USERNAME/arrest-molecules.git
cd arrest-molecules
git checkout -b feature/votre-contribution
```

### 2. Développer
- Suivre style Python PEP 8, R tidyverse
- Ajouter docstrings/commentaires en français ou anglais
- Tester localement :
  ```bash
  python Data_Package_FAIR2/Python_Code_API_Monte_Carlo.py --all
  ```

### 3. Commit
- Messages clairs : `feat:`, `fix:`, `docs:`, `refactor:`
- Atomiques (1 changement logique par commit)

### 4. Pull Request
- Titre descriptif
- Description : contexte, changements, tests effectués
- Lier issues si applicable : `Fixes #123`

---

## 🧪 Standards Qualité

### Données
- **Sources :** PMIDs pour chaque valeur pharmacologique
- **Format :** CSV UTF-8, colonnes standardisées
- **Validation :** Plages valides (K_d 0.001-100000 nM, etc.)

### Code
- **Tests :** Résultats reproductibles (seed=42 par défaut)
- **Documentation :** Docstrings pour fonctions publiques
- **Style :** PEP 8 (Python), tidyverse (R)

### Documentation
- **Clarté :** Éviter jargon sans définition
- **Exemples :** Code exécutable inclus
- **Références :** Liens vers littérature pertinente

---

## 📧 Contact

**Questions :** tommy.lepesteur@hotmail.fr  
**Issues :** https://github.com/Mythmaker28/arrest-molecules/issues  

**Délai de réponse :** 7 jours ouvrables

---

## 📜 Licence

En contribuant, vous acceptez que vos contributions soient publiées sous :
- **Données :** CC-BY 4.0
- **Code :** MIT License

---

## 🙏 Remerciements

Les contributeurs seront listés dans `README.md` et reconnus dans les publications futures (co-authorship si contribution substantielle : >10 nouveaux composés avec validation).

Merci de votre contribution à la science ouverte ! 🚀

