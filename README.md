# NLP pour l’analyse de critiques de films

*David Scanu et Ramata Soraya Dussart*

Dans ce brief, il est question d'analyser le sentiment à travers des critiques en français de spectateurs sur des films.

---

Amélioration des performances :

- **Option 1**: voir si en enlevant des commentaires des mots qui ressortent le plus dans le nuages de mots des données d'apprentissage (quelque soit le target) 
- **Option 2**: Générer des commentaires plus cours. s'aider du nuage de mots (avis positifs, avis négatifs). 
- **Option 3**: tester sur plusieurs modèles de classification

---

## Etapes : 

- Web scraping (sauvegarde en .csv)
- Import CSV
- Encoder les notes en 1 et 0
- Suppression des lignes vides
- Suppression des avis négatifs (trop nombreux)
- Préparation entrées/sorties (X et y)
- Train Test Split
- Nettoyage des commentaires (standardize, lower case, ponctuation, stop words, tokenisation, lemmatisation)
- Word Clouds
- Vectorisation des textes
- Sélection et entrainement du modèle
- Analyse des résultats
- Export du modèle

---

<picture>
  <img alt="Logo ISEN" src="./img/logo-isen-small.png">
</picture>

<picture>
  <img alt="Logo SIMPLON" src="./img/logo-simplon-small.png">
</picture>