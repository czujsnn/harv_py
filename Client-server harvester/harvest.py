from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import requests
import re
import configparser
import os
import urllib.parse as url_parse

import ini
import minimalize
import replace

def harvest():

    if os.path.exists('cfg.ini'):
        pass
    else:
        ini.ini()

    config = configparser.ConfigParser()
    config.read('cfg.ini')
    adres = config['DEFAULT']['adreswww']

    request = requests.get(f"{adres}")
    tekst = request.text
    soup = BeautifulSoup(tekst,'html.parser')

    linki = []
    link_ = ''

    for link in soup.find_all('a'):
        link_ = link.get("href")
        linki.append(link_)

    linki.append(f'{adres}')

    if '#content' in linki:
        linki.remove('#content')

    #cleanup taki z linkow, usuwa typy none, co maja # albo None
    for x in range(len(linki)):
        try:

            if type(linki[x]) == None:
                linki.pop(x)

            elif linki[x] == "#":
                linki.pop(x)

            elif linki[x] == "None":
                linki.pop(x)

        except IndexError:
            pass
        
    new_links =[]
    for x in linki:
        try:

            if str(x[0:4]) == "http":
                new_links.append(str(x))

            else:
                url = url_parse.urljoin(adres,x)
                new_links.append(str(url))
                pass

        except TypeError:
            pass

    linki = new_links.copy()
    maile = []
    for link in linki:
        try:
            N_request = requests.get(link)

        except requests.exceptions.RequestException as e:
            print(e)
            N_tekst = f"{adres}/{link}"
            
        except request.exceptions.MissingSchema:
            N_tekst = f"{adres}/{link}"
        
        except ConnectionError as e:
            print(e)
            pass
        
        except requests.exceptions.ConnectionError as e:
            print("error z polaczeniem")
            pass

        N_tekst = N_request.text

        soup = BeautifulSoup(N_tekst,'lxml')
        reobj = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}\b", re.IGNORECASE)
        mail = re.findall(reobj,N_tekst)

        if mail == []:
            pass
        elif mail in maile:
            pass
        elif mail[-4:] == ".jpg" or mail[-4:] == ".png": #np w olxie znajdowalo jakies stringi co mialy @ w sobie ale to byly zdjecia
            pass
        else:
            maile.append(mail)
        
        if mail != [] or mail not in maile:print(mail)

    #petla do usuwania powtórzonych mailów

    maile = minimalize.minimalize_email_set(maile)

    if 'https' in adres:nazwa = adres[8:]
    else:nazwa = adres[7:]

    nazwa = replace.repl(nazwa)

    with open(f"{nazwa}.txt","w+") as f:
        for x in range(len(maile)):
            f.write(f"{maile[x]} \n")

    return nazwa