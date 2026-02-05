import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Configuration pour un rendu "Executive"
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.figsize'] = (14, 8)

def generate_dashboard():
    print(">>> Génération du Dashboard Décisionnel...")
    
    # 1. Chargement des Résultats
    try:
        df = pd.read_csv('forecast_results_2017.csv', index_col=0, parse_dates=True)
        df.index.name = 'Date'
    except FileNotFoundError:
        print("Erreur: 'forecast_results_2017.csv' introuvable. Veuillez lancer forecast_script.py d'abord.")
        return

    # 2. Calcul des Indicateurs Clés
    peak_normal = df['Forecast_Normal'].max()
    peak_normal_date = df['Forecast_Normal'].idxmax()
    
    peak_crisis = df['Forecast_Crisis'].max()
    peak_crisis_date = df['Forecast_Crisis'].idxmax()
    
    max_surplus = (df['Forecast_Crisis'] - df['Forecast_Normal']).max()
    total_excess_patients = (df['Forecast_Crisis'] - df['Forecast_Normal']).sum()

    # 3. Création du Graphique "Executive"
    fig, ax = plt.subplots()

    # Zone de Surplus (Impact Crise)
    ax.fill_between(df.index, df['Forecast_Normal'], df['Forecast_Crisis'], 
                    color='#e74c3c', alpha=0.2, label='Surplus de Patients (Crise)')
    
    # Courbes
    ax.plot(df.index, df['Forecast_Normal'], color='#27ae60', linestyle='--', linewidth=2, label='Scénario Normal')
    ax.plot(df.index, df['Forecast_Crisis'], color='#c0392b', linewidth=3, label='Scénario Crise')

    # 4. Annotations Stratégiques (Pics & Ordres de Grandeur)
    
    # Pic Crise
    ax.annotate(f'PIC CRISE\n{int(peak_crisis)} admissions', 
                xy=(peak_crisis_date, peak_crisis), 
                xytext=(peak_crisis_date, peak_crisis + 1000),
                arrowprops=dict(facecolor='#c0392b', shrink=0.05),
                fontsize=11, fontweight='bold', color='#c0392b', ha='center')

    # Pic Normal
    ax.annotate(f'Pic Normal\n{int(peak_normal)}', 
                xy=(peak_normal_date, peak_normal), 
                xytext=(peak_normal_date, peak_normal - 1500),
                arrowprops=dict(facecolor='#27ae60', shrink=0.05),
                fontsize=10, color='#27ae60', ha='center')

    # Delta Max
    ax.text(df.index[int(len(df)/2)], peak_crisis - 500, 
            f'Surplus Max: +{int(max_surplus)} / mois', 
            fontsize=12, color='#c0392b', fontweight='bold', ha='center',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#c0392b", alpha=0.8))

    # Titres et Labels
    plt.title('DASHBOARD DÉCISIONNEL : Impact Projeté de la Crise 2017', fontsize=16, fontweight='bold', pad=20)
    plt.suptitle(f'Impact Total Estimé : +{int(total_excess_patients)} patients supplémentaires sur l\'année', 
                 fontsize=12, color='#7f8c8d', y=0.94)
    
    plt.ylabel("Admissions Mensuelles", fontsize=12)
    plt.xlabel("Mois (2017)", fontsize=12)
    
    # Formatage Dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    
    # Légende épurée
    plt.legend(loc='upper left', frameon=True, fancybox=True, framealpha=1, shadow=True)
    
    # Sauvegarde
    filename = 'docs/dashboard_decisionnel_2017.png'
    plt.savefig(filename, dpi=100, bbox_inches='tight')
    plt.close()
    print(f"    Dashboard sauvegardé : {filename}")

if __name__ == "__main__":
    generate_dashboard()
