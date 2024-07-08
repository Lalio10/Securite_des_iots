#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time

try:
    # Boucle infinie pour envoyer des messages MQTT en continu
    while(True):
        # Définition du message à envoyer
        message = "{'data' : 'bedead' ,'port' : 5, 'time' : 'immediately'}"

        # Création d'un client MQTT
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

        # Configuration des identifiants de connexion
        client.username_pw_set("expemb", "Y8LyXK2QFE1D")

        # Connexion au broker MQTT
        client.connect("192.168.1.28", 1883, 60)
        time.sleep(1)

        # Publication du message sur le topic spécifié
        client.publish("in/F4C/80A5F5F5", message)
        time.sleep(1)

        # Déconnexion du broker MQTT
        client.disconnect()

        # Affichage d'un message de confirmation
        print("Message published successfully.")
        
        # Attente de 60 secondes avant d'envoyer le prochain message
        time.sleep(60)

except:
    # En cas d'exception, le script passe simplement (ne fait rien)
    pass
