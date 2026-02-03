import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
import pmdarima as pm
from pmdarima.arima import auto_arima

# Configuration visuelle
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def load_data(filepath):
    """Charge et nettoie les données."""
    print(">>> Chargement des données...")
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.index.freq = 'MS'  # Définir la fréquence mensuelle
    print(f"    Données chargées: {df.shape[0]} mois ({df.index.min().date()} - {df.index.max().date()})")
    return df

def plot_eda(df):
    """Génère les graphiques d'analyse exploratoire."""
    print(">>> Génération des graphiques EDA...")
    
    # 1. Série Temporelle Urgences
    plt.figure()
    plt.plot(df.index, df['Urgences'], label='Urgences', linewidth=2.5, color='#2c3e50')
    plt.title('Évolution des Admissions aux Urgences (2012-2016)', fontsize=14)
    plt.ylabel('Nombre d\'admissions')
    plt.legend()
    plt.tight_layout()
    plt.savefig('eda_trend_urgences.png')
    plt.close()

    # 2. Décomposition Saisonnière
    decomp = seasonal_decompose(df['Urgences'], model='additive')
    fig = decomp.plot()
    fig.set_size_inches(12, 10)
    plt.savefig('eda_decomposition.png')
    plt.close()

    # 3. Tension Lits vs Urgences
    fig, ax1 = plt.subplots()
    color = 'tab:blue'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Urgences', color=color)
    ax1.plot(df.index, df['Urgences'], color=color, label='Urgences')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  
    color = 'tab:red'
    ax2.set_ylabel('Tension Urgences/Lits', color=color)  
    ax2.plot(df.index, df['Tension_Urgences_Lits'], color=color, linestyle='--', label='Tension')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Corrélation Volume Urgences vs Tension des Lits')
    plt.tight_layout()
    plt.savefig('eda_tension_lits.png')
    plt.close()
    
    print("    Graphiques sauvegardés : eda_trend_urgences.png, eda_decomposition.png, eda_tension_lits.png")

def find_best_model(y):
    """Identifie les meilleurs paramètres SARIMA avec auto_arima."""
    print(">>> Recherche du modèle SARIMA optimal (Auto-ARIMA)...")
    
    # Recherche automatique avec saisonnalité m=12
    model = auto_arima(y, 
                       start_p=0, start_q=0,
                       max_p=3, max_q=3,
                       m=12,              # Saisonnalité mensuelle
                       start_P=0, seasonal=True, # Activer la partie saisonnière
                       d=1, D=1,          # Différenciation attendue
                       trace=True,
                       error_action='ignore',  
                       suppress_warnings=True, 
                       stepwise=True)

    print(f"\n    Meilleur modèle trouvé : {model.order} x {model.seasonal_order}")
    print(f"    AIC: {model.aic()}")
    return model

def main():
    filepath = 'data/dataset_hopital_final.csv'
    
    # 1. Load
    df = load_data(filepath)
    
    # 2. EDA
    plot_eda(df)
    
    # 3. Model ID
    model = find_best_model(df['Urgences'])
    
    # Sauvegarde des résultats du modèle pour la suite (ou juste affichage)
    with open("model_params.txt", "w") as f:
        f.write(f"Order: {model.order}\n")
        f.write(f"Seasonal Order: {model.seasonal_order}\n")
        f.write(f"AIC: {model.aic()}\n")

if __name__ == "__main__":
    main()
