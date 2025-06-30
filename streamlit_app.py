import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Green Computing",
    page_icon="assets/green_computing_icon.png",
    layout="wide"
)
# Réduire l'espacement supérieur
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

# Fonction pour charger une page HTML externe
def load_html_page(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    st.markdown(html, unsafe_allow_html=True)

# Menu de navigation
menu = st.sidebar.radio("📚 Menu", [
    "🏠 Accueil",
    "📌 Introduction",
    "🧬 Méthodologie",
    "📊 Résultats",
    "🧠 Simulation IA",
    "✅ Conclusion"
])

# Routage
if menu == "🏠 Accueil":
    load_html_page("html/accueil.html")

elif menu == "📌 Introduction":
    st.header("📌 Introduction : Contexte et Problématique")

    tab1, tab2, tab3 = st.tabs(["🌐 Contexte", "⚠️ Problématique","🎯 Objectifs"])

    with tab1:
        st.markdown("""
<h3>Contexte</h3>

<h4>Quelques chiffres clés</h4>
<ul>
    <li>Plus de <strong>350 millions</strong> de photos sont partagées chaque jour sur Facebook</li>
    <li>Plus de <strong>500 heures</strong> de vidéos sont ajoutées à YouTube chaque minute</li>
    <li>Google traite plus de <strong>100 000 requêtes par seconde</strong></li>
</ul>
<h4>Qu’est-ce qu’un data center ?</h4>
<ul>
    <li>Un site physique hébergeant des milliers de serveurs interconnectés</li>
    <li>Permet le stockage, le traitement et la diffusion massive des données</li>
    <li>Supporte les applications critiques : IA, vidéos, réseaux sociaux, e-commerce, etc.</li>
</ul>


""", unsafe_allow_html=True)



    with tab2:
        st.markdown("""
        <h3>Problématique</h3>
        <ul>
            <li>Plus de <strong>800</strong> data centers hyperscale en 2024 (Statista)</li>
            <li>Les data centers consomment <strong>1 à 2 %</strong> de l’électricité mondiale.</li>
            <li>Environ <strong>40 %</strong> de cette énergie est utilisée pour le <strong>refroidissement</strong>.</li>
            <li>Beaucoup de machines sont <strong>sous-utilisées</strong>.</li>
            <li>Jusqu’à <strong>50 %</strong> de perte énergétique due à la mauvaise gestion des ressources</li>
        </ul>
                    
<blockquote style="color:gray; font-style:italic; border-left:4px solid #ccc; padding-left:10px;">
“Training a single large AI model can emit as much carbon as five cars in their lifetimes.” – <strong>MIT Tech Review</strong>
</blockquote>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <h3>Objectifs du projet</h3>
        <ul>
            <li> Simuler des environnements réalistes de data centers virtualisés</li>
            <li> Prédire la consommation énergétique à l’aide d’un modèle IA</li>
        </ul>
        <p style="text-align:center; font-style: italic; color: #555;">
        Objectif final : améliorer l'efficacité énergétique des infrastructures numériques 🌱
        </p>
        """, unsafe_allow_html=True)

elif menu == "🧬 Méthodologie":
    st.header("🧬 Méthodologie")

    tab1, tab2, tab3 = st.tabs(["🔧 Architecture", "🧪 Données & Prétraitement", "🧠 Modèle IA"])

    with tab1:
        st.markdown("""
        ### Architecture du système

        **Étapes principales :**
        - Génération de données synthétiques (VMs, CPU, RAM, etc.)
        - Intégration d’un modèle IA pour prédire la consommation énergétique
        - Optimisation de l'efficacité énergétique des data centers

        """)
        st.image("assets/architecture.png", caption="Architecture du système" )

    with tab2:
        st.markdown("""
        ### Données & Prétraitement

        **Caractéristiques simulées :**
        - Nombre de VMs actives
        - CPU utilisée (GHz)
        - RAM utilisée (Go)
        - Capacité totale CPU/RAM""")
        st.image("data/power_plot.png")

    with tab3:
        st.markdown("""
        ### Entraînement des Modèles IA

        #### Modèles entraînés :
        - **Random Forest Regressor**
        - **Gradient Boosting Regressor**
        - **Régression Linéaire**



        #### Méthodologie :
        - **Séparation des données** : 80 % pour l'entraînement, 20 % pour le test
        - **Métriques d’évaluation** :
            - **MAE** : Erreur Absolue Moyenne
            - **R² Score** : Qualité d’ajustement
       
        """, unsafe_allow_html=True)


elif menu == "📊 Résultats":
    st.header("📊 Résultats des Modèles de Prédiction")

    st.subheader("Comparaison des performances")
    
    # Charger le tableau comparatif
    df_metrics = pd.read_csv("ml/model_comparison.csv")
    st.dataframe(df_metrics.sort_values(by="R² Score", ascending=False), use_container_width=True)

    # Formulation interprétative
    best_model = df_metrics.sort_values(by="R² Score", ascending=False).iloc[0]


    # Affichage du graphique
    st.subheader("Prédictions vs Données réelles (échantillon de 100 points)")
    st.image("ml/prediction_comparison_power.png")



elif menu == "🧠 Simulation IA":
    st.header("🧠 Simulation de la Consommation Énergétique par IA")

    st.markdown("Ajustez les paramètres d'un hôte virtualisé pour estimer sa consommation énergétique.")

    with st.form("simulation_form"):
        col1, col2 = st.columns(2)
        with col1:
            n_vms = st.slider("Nombre de VMs actives", 0, 150, 30)
            cpu_used = st.slider("CPU utilisée (GHz)", 0.0, 64.0, 20.0)
            cpu_capacity = st.selectbox("Capacité totale CPU", [32, 64])
        with col2:
            ram_used = st.slider("RAM utilisée (Go)", 0.0, 256.0, 80.0)
            ram_capacity = st.selectbox("Capacité totale RAM", [128, 256])

        submitted = st.form_submit_button("Prédire")

    if submitted:
        # Chargement du modèle
        model = joblib.load("ml/LinearRegression_model.pkl")
        input_data = np.array([[n_vms, cpu_used, ram_used, cpu_capacity, ram_capacity]])
        predicted_power = model.predict(input_data)[0]

        # Calcul efficacité énergétique (simplifiée)
        efficiency = (cpu_used + ram_used) / predicted_power if predicted_power > 0 else 0

        col1, col2 = st.columns(2)
        col1.metric(label="⚡ Consommation estimée (Watts)", value=f"{predicted_power:.2f}")
        col2.metric(label="🌱 Efficacité énergétique (CPU+RAM/W)", value=f"{efficiency:.3f}")


elif menu == "✅ Conclusion":
    st.markdown("""
    ## ✅ Conclusion & Perspectives

    ### Bilan du projet

    Ce projet a permis de :
    -  Développer un système intelligent capable de **prédire la consommation énergétique** d’un data center virtualisé.
    -  Utiliser des algorithmes de régression performants (Random Forest, Gradient Boosting, Régression Linéaire).
    -  Simuler des environnements réalistes avec génération de données synthétiques proches de scénarios réels.
    -  Intégrer le modèle dans une **application interactive avec Streamlit** pour des prédictions en temps réel.

    ###  Perspectives d'amélioration

    - **Optimisation dynamique** : Intégration d’algorithmes d’optimisation (ex : Algorithmes évolutionnaires, PSO, Ant Colony) pour :
        -  Réduction active du nombre de serveurs allumés (consolidation)
        -  Amélioration du refroidissement et de la répartition des charges


    - **Prise en compte d'autres paramètres** :
        -  Température ambiante, type de tâches exécutées, état du réseau
        -  Source d’énergie (renouvelable vs classique) pour une approche plus durable





    """, unsafe_allow_html=True)

    st.markdown(
        "<h3 style='text-align: center;'>🌱 Vers un Green Data Center plus durables et autonomes</h3>",
        unsafe_allow_html=True
    )
