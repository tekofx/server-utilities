"""
mm_wlan
--------
The ``mm_wlan`` module defines a couple of methods to simplify connecting to a 
wireless network. https://github.com/monkmakes/mm_wlan
"""


import network, time

def connect_to_network(ssid, password):
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def is_connected():
    return wlan.status() == network.STAT_GOT_IP