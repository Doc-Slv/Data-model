# 🏥 Guide d'Utilisation Simplifié

Ce document explique comment installer et utiliser l'outil de simulation hospitalière sur votre ordinateur (Mac).

**Aucune connaissance en programmation n'est nécessaire.**

---

## 1️⃣ Étape 1 : Récupérer le projet

1.  Allez sur la page du projet (ou utilisez le lien fourni par votre administrateur).
2.  Cliquez sur le bouton vert **Code**, puis choisissez **Download ZIP**.
3.  Allez dans votre dossier **Téléchargements** et trouvez le fichier `.zip`.
4.  Double-cliquez dessus pour extraire le dossier.

> **Note :** Vous devriez maintenant avoir un dossier nommé `Data-model-main` (ou similaire).

---

## 2️⃣ Étape 2 : Lancer l'application

Nous avons créé un petit programme automatique pour tout installer à votre place.

1.  Ouvrez le dossier du projet que vous venez d'extraire.
2.  Trouvez le fichier nommé **`lancer_app.command`**.
3.  **Double-cliquez dessus**.

Une fenêtre noire (le "Terminal") va s'ouvrir. C'est normal ! 
Le programme va travailler tout seul pendant quelques secondes (ou minutes la première fois) pour "installer les outils".

> **Une fois terminé, une page internet s'ouvrira automatiquement.** 🎉
> Si la page ne s'ouvre pas, copiez-collez ce lien dans votre navigateur : `http://localhost:8501`

---

## 3️⃣ Étape 3 : Utiliser le Tableau de Bord

Une fois la page ouverte, vous verrez deux onglets en haut :

### 📊 L'Onglet "Tableau de Bord" (La Simulation)
C'est ici que vous agissez.
*   **À gauche (Barre latérale)** : C'est votre tableau de commandes.
    *   **Mois de début de crise** : Faites glisser le curseur pour dire "La crise commence en Mars".
    *   **Intensité** : Faites glisser pour dire "Il y aura +25% de patients en plus".
*   **Au centre (Graphique)** :
    *   La **Ligne Verte** montre ce qui est prévu normalement.
    *   La **Ligne Rouge** montre ce qui va se passer avec votre crise.
    *   La **Zone Rouge** montre le "surplus" de travail.

### 📚 L'Onglet "Documentation"
Cliquez sur cet onglet si vous voulez comprendre en détails les chiffres ou le vocabulaire. Tout y est expliqué en français.

---

## 🆘 En cas de problème

*   **"Commande introuvable" / Erreur Python** : Assurez-vous d'avoir installé Python sur votre Mac (téléchargeable ici : mac.python.org).
*   **La fenêtre se ferme tout de suite** : Essayez de faire un clic-droit sur `lancer_app.command`, puis "Ouvrir avec" > "Terminal".

Bonne simulation ! 
