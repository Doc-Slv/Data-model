#!/bin/bash

# Script de lancement automatique pour Mac/Linux

echo "==========================================="
echo "🏥 Lancement de l'Application Hospitalière"
echo "==========================================="
echo ""

# 1. Vérification de Python
if ! command -v python3 &> /dev/null
then
    echo "❌ Erreur : Python 3 n'est pas installé."
    echo "👉 Veuillez installer Python depuis : https://www.python.org/downloads/"
    exit
fi

# 2. Création de l'environnement virtuel si besoin
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# 3. Activation de l'environnement
source venv/bin/activate

# 4. Installation des dépendances
echo "⬇️  Vérification et installation des bibliothèques..."
pip install -r requirements.txt > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de l'installation des dépendances."
    exit
fi

# 5. Lancement de l'application
echo ""
echo "✅ Tout est prêt !"
echo "🚀 Lancement du Tableau de Bord..."
echo ""
echo "👉 Une page web va s'ouvrir automatiquement."
echo "   Si ce n'est pas le cas, cliquez ici : http://localhost:8501"
echo ""

streamlit run dashboard_app.py --server.headless false
