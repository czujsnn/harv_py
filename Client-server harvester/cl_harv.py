import socket
import os
import subprocess
import getpass
import time
import sys

from harvest import harvest as harv

print("1 aby polaczyc sie z serwerem.")

i_ =input(">_")
if int(i_) == 1:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("3.15.168.105",1244))
    print("połączono z serwerem")
else:print("niepoprawny input, spróbuj jeszcze raz")

print("tu bedzie menu wyboru trybu, domena,pojedyncza strona,sprawdz pojedynczy mail")

nazwa = harv()


with open(f"{nazwa}.txt","r") as f:
    SEND_DATA = f.read().encode()
    print(SEND_DATA)
    print("przesyłanie txt do serwera")
    s.send(SEND_DATA)




       