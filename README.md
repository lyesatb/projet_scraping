AIT TAYEB LYES
DZIRI RAYANE
HAMMA SOFIANE
Govindarajen COODIEN

﻿Projet : Analyse de voitures d'occasion

Ce projet contient deux parties :

1. Scraping de données
2. Analyse des données

-----------------------------
1. Scraping (scraping_voitures.py)
-----------------------------
- Ce script récupère des annonces de voitures (marque, modèle, prix, km, année, etc.).
- Il enregistre les données dans un fichier CSV : voitures.csv

Utilisation :
> python scraping_voitures.py

-----------------------------
2. Analyse (analyse_voitures.ipynb)
-----------------------------
- Ouvrir ce fichier dans Jupyter Notebook.
- Il contient :
  - Statistiques descriptives (prix, km, année)
  - Visualisations (histogrammes, pairplot, heatmap)
  - Classement des modèles les plus fréquents
  - Analyse par département
  - Clustering automatique des modèles ou marques

Librairies nécessaires :
- pandas
- matplotlib
- seaborn
- numpy
- scikit-learn

Exécution :
> jupyter notebook
Ouvrir ensuite le fichier et exécuter les cellules.

-----------------------------
Fichiers principaux :
- voitures.csv         => Données brutes
- scraping_voitures.py => Code de récupération
- analyse_voitures.ipynb => Analyse exploratoire

