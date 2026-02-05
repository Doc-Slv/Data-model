# Walkthrough : Résultats de la Prévision Hospitalière 2017

Ce document présente les résultats finaux du modèle SARIMA et l'analyse de l'impact d'une crise sanitaire simulée sur l'année 2017.

## 1. Résultats de la Prévision (Scénario Normal)

Le modèle SARIMA(0,1,0)(1,1,0)[12] prévoit une poursuite de la tendance haussière structurelle observée entre 2012 et 2016.

*   **Janvier 2017** : ~11,600 admissions prévues.
*   **Juillet 2017** : ~10,400 admissions.
*   **Août 2017** (Creux saisonnier) : ~8,800 admissions.

## 2. Simulation de Crise (Impact Sanitaire)

Nous avons simulé un choc de demande à partir de Mars 2017 :
*   **Mars** : +10%
*   **Avril** : +20%
*   **Mai à Décembre** : +25% de surcharge constante.

### Comparaison Visuelle
![Prévisions Normal vs Crise](/Users/romainsalavas/.gemini/antigravity/brain/4371ad8e-1488-48cd-a4d9-e0299af321c1/forecast_simulation.png)

### Impact Chiffré
| Mois | Prévision Normale | Simulation Crise | Écart (Admissions) |
| :--- | :--- | :--- | :--- |
| Mars 2017 | ~11,100 | ~12,200 | +1,100 |
| Juin 2017 | ~10,900 | ~13,600 | +2,700 |
| Décembre 2017 | ~11,600 | ~14,500 | +2,900 |

## 3. Analyse de la Tension
Compte tenu de la saturation déjà observée en 2016 (Ratio > 5), le passage à plus de 14,000 admissions mensuelles en fin d'année 2017 dans le scénario de crise entraînerait une saturation critique des lits si aucune mesure capacitaire n'est prise.

## Livrables Disponibles
*   **Documentations** : [docs/](file:///Users/romainsalavas/Documents/New%20project/docs/)
*   **Graphiques** : `eda_*.png` et `forecast_simulation.png`
*   **Données Brutes** : [forecast_results_2017.csv](file:///Users/romainsalavas/Documents/New%20project/forecast_results_2017.csv)
