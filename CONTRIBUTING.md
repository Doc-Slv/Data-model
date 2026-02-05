# Workflow Git du Projet Data Model

Ce projet suit une architecture Git professionnelle pour garantir la stabilité du code et faciliter la collaboration.

## Branches Principales

*   **`main`** : Branche de production. Contient uniquement du code stable et validé. On ne push jamais directement dessus.
*   **`preprod`** : Branche d'intégration. C'est ici que toutes les fonctionnalités sont fusionnées pour être testées avant la mise en production.

## Workflow de Développement

Pour travailler sur une nouvelle tâche (fonctionnalité, bug, etc.) :

1.  **Partez toujours de `preprod`** :
    ```bash
    git checkout preprod
    git pull origin preprod
    ```

2.  **Créez une branche dédiée** :
    Utilisez la convention de nommage suivante :
    *   `feat/nom-de-la-feature` pour une nouvelle fonctionnalité.
    *   `fix/nom-du-bug` pour une correction de bug.
    *   `docs/nom-de-la-doc` pour de la documentation.
    
    Exemple :
    ```bash
    git checkout -b feat/simulation-monte-carlo
    ```

3.  **Développez et committez** :
    Faites des commits atomiques avec des messages clairs.
    ```bash
    git commit -m "feat: ajout de l'algorithme Monte Carlo"
    ```

4.  **Fusionnez vers `preprod`** :
    Une fois terminé, fusionnez votre branche dans `preprod` (idéalement via une Pull Request sur GitHub, ou en local si vous êtes seul).
    ```bash
    git checkout preprod
    git merge --no-ff feat/simulation-monte-carlo
    ```
    *L'option `--no-ff` est importante pour garder une trace de la branche dans l'historique.*

5.  **Mise en Production** :
    Une fois `preprod` validée, elle est fusionnée vers `main`.

## Bonnes Pratiques

*   Ne jamais réécrire l'historique (force push) sur `main` ou `preprod` une fois partagé.
*   Supprimez vos branches de features après la fusion pour garder le dépôt propre.
