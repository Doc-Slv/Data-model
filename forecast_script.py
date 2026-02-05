import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Configuration
# Utiliser Agg pour éviter les erreurs de GUI dans certains environnements
import matplotlib
matplotlib.use('Agg')

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (14, 7)

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.index.freq = 'MS'
    return df

def run_forecast_and_simulation(df):
    print(">>> Entraînement du modèle SARIMA(0,1,0)(1,1,0)[12]...")
    
    # 1. Train Model (2012-2016)
    model = SARIMAX(df['Urgences'], 
                    order=(0, 1, 0), 
                    seasonal_order=(1, 1, 0, 12),
                    enforce_stationarity=False,
                    enforce_invertibility=False)
    results = model.fit(disp=False)
    
    # 2. Forecast 2017 (Normal Scenario)
    print(">>> Génération des prévisions 2017 (Scénario Normal)...")
    forecast_steps = 12
    forecast_obj = results.get_forecast(steps=forecast_steps)
    forecast_mean = forecast_obj.predicted_mean
    conf_int = forecast_obj.conf_int(alpha=0.05)
    
    # Création de l'index 2017
    dates_2017 = pd.date_range(start='2017-01-01', periods=12, freq='MS')
    forecast_mean.index = dates_2017
    conf_int.index = dates_2017

    # 3. Simulation Crisis (Scenario: Demand shock starting March 2017)
    print(">>> Simulation de la Crise Sanitaire...")
    # Hypothèse : Choc progressif puis constant
    # Jan-Fev: 1.0, Mars : +10%, Avril : +20%, Mai-Dec : +25%
    shock_factors = [1.0, 1.0, 1.10, 1.20] + [1.25]*8
    crisis_forecast = forecast_mean * np.array(shock_factors)
    
    # 4. Visualization
    plt.figure(figsize=(15, 8))
    
    # Historique
    plt.plot(df.index, df['Urgences'], label='Historique (2012-2016)', color='black', alpha=0.7)
    
    # Prévision Normale
    plt.plot(forecast_mean.index, forecast_mean, label='Prévision 2017 (Normal)', color='green', linestyle='--', linewidth=2)
    plt.fill_between(conf_int.index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='green', alpha=0.1, label='IC 95%')
    
    # Prévision Crise
    plt.plot(forecast_mean.index, crisis_forecast, label='Simulation Crise (Choc Demande)', color='red', linestyle='-', linewidth=2.5)
    
    plt.title('Prévisions Urgences 2017 : Scénario Normal vs Crise', fontsize=16)
    plt.xlabel('Date')
    plt.ylabel('Nombre d\'admissions')
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)
    
    output_img = 'forecast_simulation.png'
    plt.savefig(output_img)
    plt.close()
    print(f"    Graphique sauvegardé : {output_img}")
    
    # Export CSV
    results_df = pd.DataFrame({
        'Forecast_Normal': forecast_mean.values,
        'Forecast_Crisis': crisis_forecast.values,
        'Lower_CI': conf_int.iloc[:, 0].values,
        'Upper_CI': conf_int.iloc[:, 1].values
    }, index=dates_2017)
    
    results_csv = 'forecast_results_2017.csv'
    results_df.to_csv(results_csv)
    print(f"    Données sauvegardées : {results_csv}")

if __name__ == "__main__":
    try:
        data_df = load_data('data/dataset_hopital_final.csv')
        run_forecast_and_simulation(data_df)
        print(">>> Terminé avec succès.")
    except Exception as e:
        print(f"ERROR: {e}")
