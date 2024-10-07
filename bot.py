import requests
import time
from bs4 import BeautifulSoup
from variables import *

find = False
# Boucle infinie pour vérifier la page toutes les minutes
while find == False:
    for nSite in range(len(sites)):
        try:
        # Récupération du code source de la page
            headers = {'User-Agent': 'Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
            response = requests.get(sites[nSite]['url'], timeout=200, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Vérification si l'élément est présent
            element = soup.select_one(sites[nSite]['selector'])
            if sites[nSite]['text'] != element.text:
                # Envoi d'un message sur Discord si l'élément n'est pas présent (le produit est disponible)
                requests.post(webhook_url, json={
                    'content': f'<@{id_user}> Le produit est maintenant disponible ! sur le site : {sites[nSite]["url"]}'
                })
                find = True
            if element == None:
                # Envoi d'un message sur Discord informant que le selecteur CSS n'a pas été trouvé
                requests.post(webhook_url, json={
                    'content': f'<@{id_user}> Le selecteur CSS du site {sites[nSite]["url"]} n\'a pas été trouvé.'
                })
                find = True
        except requests.exceptions.Timeout:
            # Envoi d'un message sur Discord informant que le site a mis trop de temps à répondre
            requests.post(webhook_url, json={
                'content': f'<@{id_user}> Le site {sites[nSite]["url"]} a mis trop de temps à répondre.'
            })

    time.sleep(60)
