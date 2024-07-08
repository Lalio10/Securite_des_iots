#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time

try:
   while(True):
       message = "{'data' : 'bedead' ,'port' : 5, 'time' : 'immediately'}"

       client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
       client.username_pw_set("expemb", "Y8LyXK2QFE1D")
       client.connect("192.168.1.28", 1883, 60)
       time.sleep(1)
       client.publish("in/F4C/80A5F5F5", message)
       time.sleep(1)
       client.disconnect()

       print("Message published successfully.")
       time.sleep(60)
except:
   pass
