import requests
import time
from bs4 import BeautifulSoup
from variables import *

find = False
# Boucle infinie pour vérifier la page toutes les minutes
while find == False:
    for nSite in range(len(sites)):
    # Récupération du code source de la page
        response = requests.get(sites[nSite]['url'])
        soup = BeautifulSoup(response.content, 'html.parser')

        # Vérification si l'élément est présent
        element = soup.select_one(sites[nSite]['selector'])
        if element and sites[nSite]['text'] not in element.text:
            # Envoi d'un message sur Discord si l'élément n'est pas présent
            requests.post(webhook_url, json={'content': 'Le produit est maintenant disponible ! sur le site : ' + sites[nSite]['url']})
            find = True
        else:
            time.sleep(60)
