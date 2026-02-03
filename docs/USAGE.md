# Guide d'Utilisation du Modèle Prédictif

Ce guide vous explique comment utiliser le modèle, générer les prévisions et interpréter le Dashboard Décisionnel.

## 1. Structure du Projet

*   `data/` : Contient vos fichiers sources (`dataset_hopital_final.csv`).
*   `docs/` : Contient les graphiques et rapports générés.
*   `forecast_script.py` : Le moteur de calcul (entraîne le modèle, génère les chiffres).
*   `generate_dashboard.py` : Le moteur de visualisation (crée le graphique décisionnel).
*   `dashboard_app.py` : L'interface web interactive.

## 2. Comment Lancer une Nouvelle Analyse ?

Si vous avez de nouvelles données ou si vous voulez relancer l'analyse :

1.  **Ouvrez votre terminal** (ou demandez à l'assistant).
2.  **Activez l'environnement** (si ce n'est pas automatique) :
    ```bash
    source venv/bin/activate
    ```
3.  **Lancez le calcul des prévisions** :
    ```bash
    python forecast_script.py
    ```
    *Cela va créer/mettre à jour `forecast_results_2017.csv`.*

4.  **Générez le Dashboard Décisionnel Static** :
    ```bash
    python generate_dashboard.py
    ```
    *Cela va créer `docs/dashboard_decisionnel_2017.png`.*

5.  **Lancer l'Interface Web (Nouveau)** :
    ```bash
    # Si streamlit n'est pas dans votre PATH, utilisez python -m streamlit
    streamlit run dashboard_app.py
    ```
    *Cela ouvrira automatiquement une page web interactive dans votre navigateur.*

## 3. Interprétation du Dashboard Décisionnel

Le graphique `dashboard_decisionnel_2017.png` est conçu pour la prise de décision rapide.

### Les Courbes
*   **Verte (Pointillés)** : C'est le **"Business as Usual"**. Ce qui se passera si rien de spécial n'arrive. Elle suit la saisonnalité habituelle (pic en hiver, creux en août).
*   **Rouge (Pleine)** : C'est le **Scénario de Crise**. Elle inclut le "choc" de demande simulé (+10% à +25%).

### Les Zones Clés
1.  **Zone Rouge (Entre les courbes)** :
    *   Représente le **Surplus de Patients** dû à la crise.
    *   C'est le volume *supplémentaire* que vos services devront absorber.
    *   *Ordre de grandeur* : Regardez l'annotation "Impact Total Estimé" en haut du graphique (ex: +30 000 patients).

2.  **Les Pics (Triangles)** :
    *   **Pic Normal** : Le maximum attendu sans crise.
    *   **Pic Crise** : Le nouveau maximum à redouter. Comparez ces deux chiffres pour dimensionner vos équipes (ex: passer d'une capacité de 11k à 14k).

3.  **Surplus Max** :
    *   Indique le mois le plus critique où l'écart entre la normale et la crise est le plus fort.

## 4. Modifier les Hypothèses de Crise

Pour changer la simulation (ex: choc de +50% au lieu de +25%), vous devez modifier le fichier `forecast_script.py`, ligne ~45 :

```python
# Exemple : Choc de 50% toute l'année
shock_factors = [1.50] * 12 
```
Puis relancez les scripts comme indiqué en étape 2.
