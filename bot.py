import requests
import time
from bs4 import BeautifulSoup

# URL de la page web à vérifier
url = 'exemple.com'

# Élément à rechercher
selector = 'element-css'

# Texte à rechercher
text = 'Texte à rechercher'

# URL du webhook Discord
webhook_url = 'URL of Discord webhook'

# Boucle infinie pour vérifier la page toutes les minutes
while True:
    # Récupération du code source de la page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Vérification si l'élément est présent
    element = soup.select_one(selector)
    if element and text not in element.text:
        # Envoi d'un message sur Discord si l'élément n'est pas présent
        requests.post(webhook_url, json={'content': 'Le produit est maintenant disponible !'})
        
    else:
        time.sleep(60)