#!/usr/bin/env python3
import time
from swARM_at.RAK3172 import RAK3172, VALID_BAUD_RATE, VALID_COM_PORT, VALIDE_BAND
from swARM_at.exceptions import InvalidBaudRateException, InvalidCOMPortException

# Crée une instance de la classe RAK3172 en spécifiant le port COM5
rak = RAK3172("COM5")

# Connecte l'appareil
rak.connect()

# Configure le mode réseau
rak.set_network_mode()

# Pause d'une seconde
time.sleep(1)

# Récupère le devEUI de l'appareil et l'affiche
devEUI = rak.get_dev_eui()
time.sleep(1)
print(f'devEUI={devEUI}')

# Récupère l'AppKey et l'affiche
appkey = rak.get_app_key()
time.sleep(1)
print(f'appkey={appkey}')

# configure la connexion 
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

# Initialise une variable de contrôle pour une boucle infinie
a = True

try:
    while(a):
        # Envoie des données LoRaWAN, envoie le SNR
        rak.send_lorawan_data(5, SNR)
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

except KeyboardInterrupt:
    # Capture l'interruption clavier pour arrêter proprement le script
    pass
