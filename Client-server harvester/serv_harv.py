import socket
import sys
import cv2
import getpass
import os


s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(('',1244))

s.listen(5)
print("oczekiwanie na polaczenie")
client,adres = s.accept()
lista_klientow = []

print("******************************")
print("HELP TO WPISZ : help")



print(f"polaczenie od {adres} zostalo nawiazane")
#otrzymaj txt i zrob baze danych
print('oczekiwanie na txt')
while True:
    txt = open('mail.txt','w+')
    while True:
        data = client.recv(1024)
        print(data)
        if data:
            txt.write(data.decode())
        else:
            client.close()
            
            break

