import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from config import *

# Générer les timestamps
timestamps = pd.date_range(start=START_DATE, periods=24 * DURATION_DAYS, freq=FREQUENCY)

# Générer la liste des VMs et leur affectation à des hôtes
vm_list = [f"vm_{i}" for i in range(TOTAL_VMS)]
vm_host_map = {vm: np.random.randint(0, N_HOSTS) for vm in vm_list}
vm_records, host_records = [], []

for ts in timestamps:
    host_usage = {h: {"cpu": 0, "ram": 0, "n_vms": 0} for h in range(N_HOSTS)}

    for vm in vm_list:
        host = vm_host_map[vm]
        cpu = round(np.clip(np.random.normal(VM_CPU_MEAN, VM_CPU_STD), 0.5, 6.0), 2)
        ram = round(np.clip(np.random.normal(VM_RAM_MEAN, VM_RAM_STD), 1, 12), 2)
        status = np.random.choice(list(STATUS_PROBS.keys()), p=list(STATUS_PROBS.values()))

        if status != 'off':
            host_usage[host]["cpu"] += cpu
            host_usage[host]["ram"] += ram
            host_usage[host]["n_vms"] += 1

        vm_records.append({
            "timestamp": ts,
            "vm_id": vm,
            "host_id": host,
            "cpu_demand": cpu,
            "ram_demand": ram,
            "status": status
        })

    for host in range(N_HOSTS):
        cpu_used = host_usage[host]["cpu"]
        ram_used = host_usage[host]["ram"]
        n_vms = host_usage[host]["n_vms"]
        usage_ratio = cpu_used / CPU_CAPACITY if CPU_CAPACITY > 0 else 0

        # Consommation énergétique de base + bruit aléatoire
        base_power = POWER_IDLE + (POWER_FULL - POWER_IDLE) * usage_ratio
        noise = np.random.normal(0, 5)  # bruit gaussien ~5W
        power = round(base_power + noise, 2)

        host_records.append({
            "timestamp": ts,
            "host_id": host,
            "n_vms": n_vms,
            "cpu_used": round(cpu_used, 2),
            "ram_used": round(ram_used, 2),
            "cpu_capacity": CPU_CAPACITY,
            "ram_capacity": RAM_CAPACITY,
            "power_consumed": power
        })

# Création du dossier si nécessaire
os.makedirs("data", exist_ok=True)

# Sauvegarde des fichiers CSV
df_vms = pd.DataFrame(vm_records)
df_hosts = pd.DataFrame(host_records)

df_vms.to_csv("data/vms_dataset.csv", index=False)
df_hosts.to_csv("data/hosts_dataset.csv", index=False)

# Visualisation : consommation moyenne par heure
avg_power = df_hosts.groupby("timestamp")["power_consumed"].mean()

plt.figure(figsize=(10, 4))
plt.plot(avg_power.index, avg_power.values)
plt.title("Évolution moyenne de la consommation énergétique par heure")
plt.xlabel("Temps")
plt.ylabel("Consommation (Watts)")
plt.grid(True)
plt.tight_layout()

# Sauvegarde du graphique
plot_path = "data/power_plot.png"
plt.savefig(plot_path)
plt.close()
