#!/usr/bin/env python3
import time
from swARM_at.RAK3172 import RAK3172, VALID_BAUD_RATE, VALID_COM_PORT, VALIDE_BAND
from swARM_at.exceptions import InvalidBaudRateException, InvalidCOMPortException

rak = RAK3172("COM5")
rak.connect()
rak.set_network_mode()
time.sleep(1)
devEUI=rak.get_dev_eui()
time.sleep(1)
print(f'devEUI={devEUI}')
appkey = rak.get_app_key()
time.sleep(1)
print(f'appkey={appkey}')
rak.set_join_mode()
rak.join_network(1, 0, 10, 8)
time.sleep(5)

while(not rak.check_join_status()):
   time.sleep(1)
time.sleep(5)
rak.send_lorawan_data(5,"AA")
time.sleep(1)


RSSI = rak.get_rssi()
time.sleep(1)

SNR = rak.get_snr()
time.sleep(1)
print(f'RSSI={RSSI}\r\nSNR={SNR}')

rcv = rak.receive_data()
time.sleep(1)
print(f'rcv={rcv}')

a=True
try:
   while(a):
       rak.send_lorawan_data(5,SNR)
       b=True
       while(b):
           rcv = rak.receive_data()
           time.sleep(5)
           if(rcv[0]=='5'):
               print(f'rcv={rcv}')
               b=False

               RSSI = rak.get_rssi()
               time.sleep(1)

               SNR = rak.get_snr()
               time.sleep(1)

               
except KeyboardInterrupt:
   pass
