# Stock-checker

## Notifies on Discord when a product becomes in stock

Stock-checker allows you to access a web page, and to regularly check if a product is in stock, in order to be notified via discord as soon as it is.


## Configuration

Modifier le fichier variable.py selon vos besoin :voir [l'exemple](variables.py)


## Docker

Utiliser le fichier [docker-compose.yml](docker-compose.yml) pour lancer le container. Modifier le chemin du fichier variable.py selon vos besoins.

Dans le dossier courant du projet, lancer la commande suivante pour lancer le container :

```docker compose up -d```