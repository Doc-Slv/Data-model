# Plan d'Implémentation : Modèle Prédictif Urgences Hospitalières

Ce projet vise à développer un modèle SARIMA pour prédire les admissions aux urgences hospitalières pour l'année 2017, basé sur des données mensuelles de 2012 à 2016, et à simuler l'impact d'une crise sanitaire.

## User Review Required

> [!IMPORTANT]
> **Données requises** : J'ai besoin du dataset (CSV ou Excel) et du PDF explicatif mentionnés. Veuillez les placer dans le dossier du projet ou m'indiquer leur emplacement.

## Proposed Changes

### Structure du Projet

Je propose d'utiliser **Python** car c'est le standard de l'industrie pour la Data Science, avec des bibliothèques robustes comme `pandas`, `statsmodels`, et `pmdarima` pour l'analyse de séries temporelles.


#### [NEW] [analysis_script.py](file:///Users/romainsalavas/Documents/New%20project/analysis_script.py)
Ce script sera le coeur du projet. Il effectuera les étapes suivantes :

1.  **Chargement et Prétraitement** :
    *   Lecture de `data/dataset_hopital_final.csv`.
    *   Conversion de la colonne `Date` en index datetime.
    *   Target : Colonne `Urgences`.

2.  **Analyse Exploratoire (EDA)** :
    *   Décomposition de la série `Urgences` (Tendance, Saisonnalité).
    *   Visualisation de la corrélation avec `Tension_Urgences_Lits`.

3.  **Modélisation SARIMA** :
    *   Identification des paramètres (p,d,q)(P,D,Q)m avec `pmdarima.auto_arima`.
    *   Saisonnalité attendue : m=12 (mensuelle).
    *   Entraînement sur Jan 2012 - Déc 2016.

4.  **Prévision 2017 (Scénario Normal)** :
    *   Prévision sur 12 mois (Jan - Déc 2017).
    *   Calcul des intervalles de confiance à 95%.

5.  **Simulation de Crise Sanitaire (Scénario "Choc")** :
    *   Définition d'un scénario de crise : Hausse brutale de la demande (ex: +20% à +40%) sur une période critique (ex: hiver 2017) ou choc constant.
    *   Simulation : Ajout d'une composante de choc exogène artificielle ou modification des prévisions.
    *   Analyse d'Impact : Comparaison des courbes "Normale" vs "Crise" et calcul du `Tension_Urgences_Lits` estimé (en supposant `Lits` constant ou saturé).

#### [NEW] [requirements.txt](file:///Users/romainsalavas/Documents/New%20project/requirements.txt)
Liste des dépendances : `pandas`, `numpy`, `matplotlib`, `seaborn`, `statsmodels`, `pmdarima`.

## Verification Plan

### Automated Tests
*   Le script inclura une validation croisée ou une validation sur une période de test (hold-out) si les données le permettent (ex: garder fin 2016 pour valider avant de prédire 2017, bien que le dataset soit petit).
*   Vérification des diagnostics du modèle (normalité des résidus, pas d'autocorrélation).

### Manual Verification
*   Inspection visuelle des graphiques générés :
    1.  Décomposition saisonnière.
    2.  Prévision 2017 vs Historique.
    3.  Comparaison Scénario Normal vs Crise.
