import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Configuration de la page
st.set_page_config(
    page_title="Hôpital Prédictif",
    page_icon="🏥",
    layout="wide"
)

# Style CSS personnalisé
st.markdown("""
<style>
    .metric-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    .metric-value {
        font-size: 2em;
        font-weight: bold;
        color: #2c3e50;
    }
    .metric-label {
        font-size: 1em;
        color: #7f8c8d;
    }
    .crisis-mode {
        color: #e74c3c !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv('data/dataset_hopital_final.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.index.freq = 'MS'
    return df

@st.cache_resource
def train_model(df):
    model = SARIMAX(df['Urgences'], 
                    order=(0, 1, 0), 
                    seasonal_order=(1, 1, 0, 12),
                    enforce_stationarity=False,
                    enforce_invertibility=False)
    results = model.fit(disp=False)
    return results

def main():
    st.title("🏥 Dashboard Prédictif des Urgences")
    st.markdown("---")

    # Création des onglets principaux
    tab_dashboard, tab_docs = st.tabs(["📊 Tableau de Bord", "📚 Documentation & Mode d'Emploi"])

    with tab_docs:
        st.markdown("""
        ## 📘 Guide Utilisateur & Documentation du Modèle

        Bienvenue dans l'interface de pilotage prédictif des urgences hospitalières. Cette application a été conçue pour aider les directions hospitalières à anticiper la charge de travail et à simuler des scénarios de crise.

        ---

        ### 1. Comment fonctionne le modèle prédictif ? 🧠

        Le moteur de prévision repose sur un algorithme statistique avancé appelé **SARIMA** (Seasonal AutoRegressive Integrated Moving Average).

        #### 🔍 Détails techniques
        *   **Algorithme utilisé** : SARIMA `(0, 1, 0) x (1, 1, 0, 12)`
        *   **Données d'entraînement** : Historique réel des admissions de **2012 à 2016**.
        *   **Saisonnalité** : Le modèle capture parfaitement les cycles annuels (pics hivernaux de grippe/virus, baisses estivales, etc.).
        *   **Stationnarité** : Les données ont été traitées pour supprimer les tendances long terme et rendre les variances stables.

        #### 📅 Ce que le modèle prédit
        Il génère une courbe de **référence "Business As Usual"** pour l'année 2017. C'est la ligne verte en pointillés sur le graphique. Elle représente ce qui se passerait *si aucune crise majeure ne survenait*.

        ---

        ### 2. Simulateur de Crise Interactif 🎛️

        Le panneau latéral (à gauche) vous permet de superposer un scénario de crise sur les prévisions normales.

        #### Les paramètres contrôlables :
        1.  **Mois de début de crise** : Définit à quel moment le choc commence.
            *   *Exemple : Mars (Mois 3)*.
        2.  **Intensité du choc (%)** : Définit le pourcentage d'augmentation des admissions par rapport à la normale.
            *   *Exemple : +25% signifie qu'il y aura 1,25 fois plus d'admissions que prévu.*

        #### 📈 Interprétation visuelle
        *   **Courbe Verte (---)** : Scénario Normal (sans crise).
        *   **Courbe Rouge (—)** : Scénario Crise simulé.
        *   **Zone Rouge** : Le "surplus" de patients que l'hôpital devra gérer en plus de l'activité habituelle.

        ---

        ### 3. Indicateurs Clés de Performance (KPIs) 📊

        En haut du tableau de bord, vous trouverez 4 indicateurs essentiels :
        *   **Admissions Totales (Normal)** : Le volume annuel attendu sans incident.
        *   **Admissions Totales (Crise)** : Le nouveau volume annuel projeté avec vos paramètres de simulation.
        *   **Surplus Estimé** : Le nombre exact de patients supplémentaires (la différence entre les deux précédents).
        *   **Pic d'Activité** : Le mois le plus chargé et le nombre maximum d'admissions mensuelles (utile pour dimensionner les équipes au pire moment).

        ---

        ### ❓ FAQ Rapide

        **Q : Pourquoi la courbe historique s'arrête-t-elle fin 2016 ?**
        R : Nous simulons l'année 2017 comme si nous étions le 1er janvier 2017, pour tester la capacité prédictive du modèle.

        **Q : La simulation est-elle fiable à 100% ?**
        R : Non, c'est un outil d'aide à la décision. La courbe verte a une fiabilité statistique (intervalle de confiance à 95%), mais le scénario de crise dépend entièrement des paramètres que vous choisissez (c'est un "Stress Test").
        """)

    with tab_dashboard:
        # Chargement des données
        with st.spinner("Chargement des données et entraînement du modèle..."):
            df = load_data()
            model_results = train_model(df)

        # Sidebar : Paramètres de simulation
        st.sidebar.header("⚙️ Simulation de Crise")
        
        st.sidebar.subheader("Intensité du Choc")
        shock_start_month = st.sidebar.slider("Mois de début de crise", 1, 12, 3, format="Mois %d")
        shock_intensity = st.sidebar.slider("Augmentation de la demande (%)", 0, 50, 25, 5) / 100.0
        
        st.sidebar.markdown("---")
        st.sidebar.info(
            "Ce simulateur applique un choc exogène sur la prévision 'Business As Usual' (SARIMA)."
        )

        # Prévisions 2017
        forecast_steps = 12
        forecast_obj = model_results.get_forecast(steps=forecast_steps)
        forecast_mean = forecast_obj.predicted_mean
        conf_int = forecast_obj.conf_int(alpha=0.05)
        
        dates_2017 = pd.date_range(start='2017-01-01', periods=12, freq='MS')
        forecast_mean.index = dates_2017
        conf_int.index = dates_2017

        # Application de la Simulation Interactives
        shock_factors = np.ones(12)
        idx_start = shock_start_month - 1
        if idx_start < 12:
            shock_factors[idx_start] = 1 + (shock_intensity / 2)
            shock_factors[idx_start+1:] = 1 + shock_intensity

        crisis_forecast = forecast_mean * shock_factors

        # KPIs Calculés
        total_normal = int(forecast_mean.sum())
        total_crisis = int(crisis_forecast.sum())
        surplus = total_crisis - total_normal
        max_monthly_admissions = int(crisis_forecast.max())
        month_peak = crisis_forecast.idxmax().strftime('%B')

        # Affichage des KPIs
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Admissions Totales 2017 (Normal)</div>
                <div class="metric-value">{total_normal:,}</div>
            </div>""", unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Admissions Totales 2017 (Crise)</div>
                <div class="metric-value crisis-mode">{total_crisis:,}</div>
            </div>""", unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Surplus Estimaté</div>
                <div class="metric-value crisis-mode">+{surplus:,}</div>
            </div>""", unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Pic d'Activité ({month_peak})</div>
                <div class="metric-value">{max_monthly_admissions:,} / mois</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("### 📈 Visualisation Dynamique")

        # Graphique
        fig, ax = plt.subplots(figsize=(12, 6))
        
        df_recent = df[df.index.year >= 2015]
        ax.plot(df_recent.index, df_recent['Urgences'], label='Historique (2015-2016)', color='black', alpha=0.5)
        
        ax.plot(forecast_mean.index, forecast_mean, label='Scénario Normal', color='#27ae60', linestyle='--', linewidth=2)
        ax.fill_between(conf_int.index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='#27ae60', alpha=0.1)
        
        ax.plot(forecast_mean.index, crisis_forecast, label=f'Scénario Crise (+{int(shock_intensity*100)}%)', color='#c0392b', linewidth=3)
        ax.fill_between(forecast_mean.index, forecast_mean, crisis_forecast, color='#e74c3c', alpha=0.2, label='Surplus Crise')

        ax.set_title("Projection des Admissions aux Urgences", fontsize=14)
        ax.set_ylabel("Admissions / Mois")
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        st.pyplot(fig)

        with st.expander("Voir les données détaillées"):
            results_df = pd.DataFrame({
                'Normal': forecast_mean,
                'Crise': crisis_forecast,
                'Delta': crisis_forecast - forecast_mean
            })
            st.dataframe(results_df.style.format("{:.0f}"))
if __name__ == "__main__":
    main()
