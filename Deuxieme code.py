#!/usr/bin/env python3
import time
import matplotlib.pyplot as plt
import numpy
from swARM_at.RAK3172 import RAK3172, VALID_BAUD_RATE, VALID_COM_PORT, VALIDE_BAND
from swARM_at.exceptions import InvalidBaudRateException, InvalidCOMPortException

# Crée une instance de la classe RAK3172 en spécifiant le port COM5
rak = RAK3172("COM5")

# Connecte l'appareil
rak.connect()

# Configure le mode réseau
rak.set_network_mode()
time.sleep(1)

# Récupère le devEUI de l'appareil et l'affiche
devEUI = rak.get_dev_eui()
time.sleep(1)
print(f'devEUI={devEUI}')

# Récupère l'AppKey et l'affiche
appkey = rak.get_app_key()
time.sleep(1)
print(f'appkey={appkey}')

# Configure la connexion
rak.set_join_mode()

# Tente de rejoindre le réseau LoRaWAN
rak.join_network(1, 0, 10, 8)
time.sleep(5)

# Vérifie si l'appareil a rejoint le réseau
while(not rak.check_join_status()):
    time.sleep(1)
time.sleep(5)

# Envoie des données LoRaWAN avec un port et un message spécifique
rak.send_lorawan_data(5, "AA")
time.sleep(1)

# Récupère et affiche la valeur RSSI (Received Signal Strength Indicator)
RSSI = rak.get_rssi()
time.sleep(1)

# Récupère et affiche la valeur SNR (Signal-to-Noise Ratio)
SNR = rak.get_snr()
time.sleep(1)
print(f'RSSI={RSSI}\r\nSNR={SNR}')

# Reçoit des données et les affiche
rcv = rak.receive_data()
time.sleep(1)
print(f'rcv={rcv}')

# Initialise des listes pour stocker les valeurs de temps, RSSI et SNR
j = []
x = []
y = []

# Crée une figure et un axe pour le graphique
fig, ax1 = plt.subplots()

# Initialise une variable de contrôle pour une boucle infinie
a = True

try:
    while(a):
        # Envoie des données LoRaWAN
        rak.send_lorawan_data(5, "AA")
        b = True
        while(b):
            # Reçoit des données toutes les 5 secondes
            rcv = rak.receive_data()
            time.sleep(5)

            # Si les données reçues contiennent '5', les affiche et sort de la boucle
            if(rcv[0] == '5'):
                print(f'rcv={rcv}')
                b = False

                # Récupère et affiche à nouveau les valeurs RSSI et SNR
                RSSI = rak.get_rssi()
                time.sleep(1)

                SNR = rak.get_snr()
                time.sleep(1)

                # Récupère et affiche le temps local
                t = rak.get_local_time()
                time.sleep(1)

                # Ajoute les valeurs récupérées aux listes pour le graphique
                x.append(t)
                y.append(RSSI)
                j.append(SNR)

except KeyboardInterrupt:
    # En cas d'interruption clavier, trace le graphique

    # Configure l'axe des x et l'axe y pour le RSSI
    ax1.set_xlabel('time')
    ax1.set_ylabel('RSSI', color='r')
    ax1.plot(x, y, 'r')
    ax1.tick_params(axis='y', labelcolor='r')

    # Crée un second axe y pour le SNR
    ax2 = ax1.twinx()
    ax2.set_ylabel('SNR', color='b')
    ax2.plot(x, j, 'b')
    ax2.tick_params(axis='y', labelcolor='b')

    # Ajuste la mise en page et affiche le graphique
    fig.tight_layout()
    plt.show()
