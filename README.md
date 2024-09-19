```
__/\\\\\\\\\\\\\_______/\\\\\\\________/\\\\\\\__________________________________________/\\\____________/\\\______________________/\\\\\\\\\\\\_        
 _\/\\\/////////\\\___/\\\/////\\\____/\\\/////\\\____________________________________/\\\\\\\__________/\\\\\____________________/\\\//////////__       
  _\/\\\_______\/\\\__/\\\____\//\\\__/\\\____\//\\\__________________________________\/////\\\________/\\\/\\\___________________/\\\_____________      
   _\/\\\\\\\\\\\\\\__\/\\\_____\/\\\_\/\\\_____\/\\\____/\\\\\__/\\\\\____/\\\\\\\\\\_____\/\\\______/\\\/\/\\\_____/\\/\\\\\\___\/\\\____/\\\\\\\_     
    _\/\\\/////////\\\_\/\\\_____\/\\\_\/\\\_____\/\\\__/\\\///\\\\\///\\\_\/\\\//////______\/\\\____/\\\/__\/\\\____\/\\\////\\\__\/\\\___\/////\\\_    
     _\/\\\_______\/\\\_\/\\\_____\/\\\_\/\\\_____\/\\\_\/\\\_\//\\\__\/\\\_\/\\\\\\\\\\_____\/\\\__/\\\\\\\\\\\\\\\\_\/\\\__\//\\\_\/\\\_______\/\\\_   
      _\/\\\_______\/\\\_\//\\\____/\\\__\//\\\____/\\\__\/\\\__\/\\\__\/\\\_\////////\\\_____\/\\\_\///////////\\\//__\/\\\___\/\\\_\/\\\_______\/\\\_  
       _\/\\\\\\\\\\\\\/___\///\\\\\\\/____\///\\\\\\\/___\/\\\__\/\\\__\/\\\__/\\\\\\\\\\_____\/\\\___________\/\\\____\/\\\___\/\\\_\//\\\\\\\\\\\\/__ 
        _\/////////////_______\///////________\///////_____\///___\///___\///__\//////////______\///____________\///_____\///____\///___\////////////____
```

# py_map_point

Py_map_point est une API qui sert à récupérer et inserer des points d'intérêts (restaurants, arret de bus, cameras...etc) sur un carte

## Prérequis

- Python 3.10
- Django 5

## Installation

1. Clonez le dépôt :
`git clone https://github.com/votre-utilisateur/py_map_point.git`


2. Accédez au répertoire du projet :

`cd py_map_point`

<!-- 1. Créez un environnement virtuel :

`python3 -m venv venv`

4. Activez l'environnement virtuel :

`source venv/bin/activate`

5. Installez les dépendances :

`pip install -r requirements.txt`

6. Appliquez les migrations :

`python manage.py migrate`

7. Créez un superutilisateur :

`python manage.py createsuperuser`

8. Lancez le serveur de développement :

`python manage.py runserver`

9. Accédez à l'application à l'adresse suivante : 

` http://127.0.0.1:8000/` -->
 
## Structure du projet
* `config/` : dossier principal du projet, contenant les fichiers de configuration Django.
*     settings.py : fichier de configuration du projet.
*     urls.py : fichier de configuration des URL du projet.
*     wsgi.py : fichier de configuration du serveur WSGI.
* `geo/` : application de gestion de l'API.
*     models.py : fichier contenant les modèles de données de l'application.
*     views.py : fichier contenant les vues de l'application.
*     urls.py : fichier de configuration des URL de l'application.
## Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.
