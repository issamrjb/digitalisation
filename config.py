# config.py

# Configuration du data center
N_HOSTS = 100
MAX_VMS_PER_HOST = 15
TOTAL_VMS = N_HOSTS * MAX_VMS_PER_HOST

# Capacités physiques par hôte
CPU_CAPACITY = 32  # en GHz
RAM_CAPACITY = 128  # en Go

# Consommation énergétique des hôtes (Watts)
POWER_IDLE = 200
POWER_FULL = 600

# Simulation temporelle
START_DATE = "2025-01-01"
DURATION_DAYS = 30
FREQUENCY = "H"  # 'H' pour horaire, '15min' pour chaque 15 minutes

# Distribution VM
VM_CPU_MEAN = 2.5
VM_CPU_STD = 1.0
VM_RAM_MEAN = 4
VM_RAM_STD = 2
STATUS_PROBS = {'running': 0.85, 'migrating': 0.05, 'off': 0.10}
# Configuration réaliste
N_HOSTS = 20
TOTAL_VMS = 100
CPU_CAPACITY = 64  # GHz
RAM_CAPACITY = 256  # GB
VM_CPU_MEAN = 2.5
VM_CPU_STD = 1.0
VM_RAM_MEAN = 4.0
VM_RAM_STD = 2.0
STATUS_PROBS = {"active": 0.7, "idle": 0.2, "off": 0.1}
POWER_IDLE = 150  # Watts
POWER_FULL = 600  # Watts
START_DATE = "2025-06-01"
DURATION_DAYS = 30
FREQUENCY = "1h"