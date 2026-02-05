# 🏥 Hôpital Prédictif - Modèle de Données

Ce projet est un outil d'aide à la décision conçu pour les établissements de santé. Il permet de visualiser les tendances des admissions aux urgences, de prévoir les pics d'activité et de simuler l'impact de crises sanitaires majeures.

## ✨ Fonctionnalités

*   **📈 Dashboard Interactif** : Une interface moderne construite avec Streamlit pour explorer les données historiques et prédictives.
*   **🔮 Prévisions Avancées** : Utilisation de modèles statistiques (SARIMA) pour anticiper les flux de patients sur les 12 prochains mois.
*   **⚠️ Simulation de Crise** : Module permettant de simuler un "choc" (ex: pandémie, vague de froid) et de visualiser l'impact sur la capacité litière.
*   **📊 Rapports d'Analyse** : Décomposition saisonnière et analyse de la qualité des données intégrées.

## 🚀 Installation

1.  **Cloner le dépôt** :
    ```bash
    git clone https://github.com/Doc-Slv/Data-model.git
    cd Data-model
    ```

2.  **Créer un environnement virtuel** :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur macOS/Linux
    ```

3.  **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Utilisation

Pour lancer l'application de tableau de bord :
```bash
streamlit run dashboard_app.py
```
Un script `lancer_app.command` est également disponible pour un lancement rapide sur macOS.

## 🛠️ Architecture du Projet

*   `dashboard_app.py` : Application principale Streamlit.
*   `analysis_script.py` : Scripts de traitement et d'analyse exploratoire.
*   `forecast_script.py` : Logique de modélisation et de prévision.
*   `Data/` : Jeux de données historiques (anonymisés).
*   `docs/` : Documentation technique et rapports générés.

## 🤝 Contribution

Ce projet suit un workflow Git professionnel. Veuillez consulter le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails sur les conventions de nommage des branches et le processus de fusion (Git Flow).

---
*Développé pour l'optimisation des ressources sanitaires.*