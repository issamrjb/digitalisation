import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Chargement des données
df = pd.read_csv("data/hosts_dataset.csv")

# Préparation des données
features = ["n_vms", "cpu_used", "ram_used", "cpu_capacity", "ram_capacity"]
target = "power_consumed"
X = df[features]
y = df[target]

# Division en jeu d'entraînement/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création du dossier ml s'il n'existe pas
os.makedirs("ml", exist_ok=True)

# Modèles à entraîner
models = {
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
    "GradientBoosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "LinearRegression": LinearRegression()
}

# Entraînement, prédiction, évaluation et sauvegarde
results = {"true": y_test.reset_index(drop=True)}
metrics = []

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    results[name] = preds

    # Sauvegarde du modèle
    joblib.dump(model, f"ml/{name}_model.pkl")

    # Évaluation
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    metrics.append({
        "Modèle": name,
        "MAE": round(mae, 2),
        "R² Score": round(r2, 3)
    })

# 🔍 Tableau comparatif
df_metrics = pd.DataFrame(metrics)
df_metrics.to_csv("ml/model_comparison.csv", index=False)

# Création du graphique de comparaison
plt.figure(figsize=(10, 5))
plt.plot(results["true"][:100], label="True Data", linewidth=2)

for name in models.keys():
    plt.plot(results[name][:100], linestyle="--", label=f"{name} Prediction")

plt.title("Prediction vs True Values for power_consumed")
plt.xlabel("Sample")
plt.ylabel("power_consumed")
plt.legend()
plt.tight_layout()

# Sauvegarde du graphique
plt.savefig("ml/prediction_comparison_power.png")
plt.close()

# ✅ Affichage console pour vérification
print("✅ Modèles entraînés et évalués avec succès !")
print(df_metrics)
