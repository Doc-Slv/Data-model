# Rapport de Qualité des Données et Analyse Préliminaire

**Date :** 03 Février 2026
**Dataset :** `dataset_hopital_final.csv`

## 1. Synthèse de la Qualité des Données
Le dataset a subi une inspection rigoureuse avant modélisation.

*   **Complétude Temporelle :**
    *   Période couverte : **Janvier 2012 à Décembre 2016**.
    *   Nombre d'observations : **60 mois**.
    *   Continuité : **Aucun manquement** détecté (pas de "trous" dans la série temporelle).
    *   Format des dates : Cohérent (AAAA-MM-JJ).

*   **Intégrité des Valeurs :**
    *   Valeurs Manquantes (Nulls) : **0** (Dataset complet à 100%).
    *   Valeurs Négatives : **0** (Pas d'anomalies de signe sur les colonnes numériques).
    *   Duplicats : **0**.

*   **Statistiques Descriptives (Cible : `Urgences`) :**
    *   Minimum : **5,732** (Août 2012)
    *   Maximum : **11,278** (Janvier/Novembre/Décembre 2016)
    *   Moyenne : **9,051** admissions/mois.

## 2. Observations Préliminaires (Insights)

### Tendance (Trend)
*   **Hausse Structurelle :** On observe une augmentation claire et constante du volume des urgences sur les 5 années.
*   Le volume mensuel est passé d'environ **7,500** en 2012 à plus de **11,000** en 2016.

### Saisonnalité
*   **Creux Estival :** Une baisse marquée et récurrente est visible chaque année au mois d'**Août** (Minima annuels systématiques).
*   **Pics Hivernaux :** Les volumes sont généralement plus élevés en hiver (Décembre/Janvier).

### Indicateurs de Tension
*   **Ratio `Tension_Urgences_Lits` :**
    *   Cet indicateur montre une dégradation inquiétante.
    *   2012 : ~3.5
    *   2016 : > 5.0
    *   **Interprétation :** La charge sur les lits disponibles augmente plus vite que la capacité d'accueil, suggérant une saturation progressive du service, indépendamment des crises ponctuelles.

## 3. Recommandations pour la Modélisation
*   **Modèle SARIMA :** La présence conjointe d'une tendance forte et d'une saisonnalité annuelle justifie pleinement l'approche SARIMA (Saisonnalité = 12).
*   **Pré-traitement :** Aucune imputation n'est nécessaire. La stationnarisation (différenciation `d=1` et saisonnière `D=1`) sera probablement requise.
*   **Simulation de Crise :** Compte tenu de la saturation déjà visible (`Tension_Urgences_Lits`), un choc simulé en 2017 risque d'avoir des effets exponentiels sur la tension hospitalière.
