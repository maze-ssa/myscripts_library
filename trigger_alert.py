import os
import time

ip_address = "192.168.11.199"
timeout = 300  # seconds

while True:
    response = os.system("ping -c 1 " + ip_address)
    if response!= 0:
        print("No response from", ip_address)
        os.system("systemctl stop datasyncn.service")
        break
    time.sleep(timeout)
