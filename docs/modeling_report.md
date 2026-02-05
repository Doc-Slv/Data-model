# Rapport de Modélisation et Analyse Exploratoire

**Date :** 03 Février 2026
**Modèle Retenu :** SARIMA `(0, 1, 0) x (1, 1, 0, 12)`

## 1. Analyse Exploratoire (EDA)

Les graphiques générés confirment les hypothèses initiales sur la structure de la série temporelle.

### Tendance et Saisonnalité
![Tendance Urgences](/Users/romainsalavas/.gemini/antigravity/brain/4371ad8e-1488-48cd-a4d9-e0299af321c1/eda_trend_urgences.png)
*   **Tendance :** Clairement haussière sur 5 ans.
*   **Saisonnalité :** Cycle annuel très marqué avec un creux significatif en **Août** et un pic en fin d'année.

### Décomposition
![Décomposition](/Users/romainsalavas/.gemini/antigravity/brain/4371ad8e-1488-48cd-a4d9-e0299af321c1/eda_decomposition.png)
*   La décomposition additive isole parfaitement la composante saisonnière répétitive et la tendance linéaire croissante.
*   Les résidus semblent aléatoires, ce qui est bon signe pour la modélisation.

### Tension Hospitalière
![Tension Lits](/Users/romainsalavas/.gemini/antigravity/brain/4371ad8e-1488-48cd-a4d9-e0299af321c1/eda_tension_lits.png)
*   La courbe rouge (Tension) suit la courbe bleue (Volume) mais avec une pente plus accentuée, indiquant une détérioration du ratio d'accueil par rapport aux lits disponibles.

## 2. Identification du Modèle (Auto-ARIMA)

L'algorithme `auto_arima` a testé plusieurs configurations pour minimiser le critère AIC (Akaike Information Criterion).

**Meilleur Modèle :** `SARIMA(0, 1, 0)(1, 1, 0)[12]`

### Paramètres :
*   **Ordre Non-Saisonnier (p, d, q) = (0, 1, 0)**
    *   `d=1` : Une différenciation première est nécessaire pour rendre la série stationnaire (suppression de la tendance).
    *   `p=0, q=0` : Pas de termes autorégressifs ou moyenne mobile simples nécessaires après différenciation. La série se comporte comme une marche aléatoire avec dérive.
*   **Ordre Saisonnier (P, D, Q, m) = (1, 1, 0, 12)**
    *   `D=1` : Une différenciation saisonnière (annuelle) est nécessaire.
    *   `P=1` : Un terme autorégressif saisonnier capture l'effet du mois de l'année précédente.
    *   `m=12` : Périodicité de 12 mois.

**Performance :**
*   **AIC :** 561.34 (Le plus bas parmi les modèles testés).

## Prochaines Étapes
Ce modèle sera utilisé pour :
1.  Générer la prévision de base pour 2017 (Scénario Normal).
2.  Servir de base pour la simulation de crise (ajout d'un choc exogène).
