# NLP pour l’analyse de critiques de films

*David Scanu et Ramata Soraya Dussart*

Dans ce brief, il est question d'analyser le sentiment à travers des critiques en français de spectateurs sur des films.
  
---

## Etapes : 

- Web scraping (sauvegarde en .csv)
- Import CSV
- Encoder les notes en 1 et 0
- Suppression des NaN
- Suppression des commentaires trop courts
- Suppression des avis positifs (trop nombreux)
- Préparation entrées/sorties (X et y)
- Train Test Split
- Text Augmentation par Back-Translation
- Nettoyage des commentaires (standardize, lower case, ponctuation, stop words, tokenisation, lemmatisation)
- Word Clouds
- Vectorisation des textes
- Sélection et entrainement du modèle
- Analyse des résultats
- Export du modèle

---

Amélioration des performances :

- **Option 1**: voir si en enlevant des commentaires des mots qui ressortent le plus dans le nuages de mots des données d'apprentissage (quelque soit la target). Mots en commun entre avis positifs et négatifs. 
- **Option 2**: Générer des **commentaires cours**. s'aider du nuage de mots (avis positifs, avis négatifs).

---

<picture>
  <img alt="Logo ISEN" src="./img/logo-isen-small.png">
</picture>

<picture>
  <img alt="Logo SIMPLON" src="./img/logo-simplon-small.png">
</picture>