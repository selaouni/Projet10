# Openclassrooms / Projet9 - parcours "Developpeur d'application python"

Date: Octobre 2022 


## Titre du projet:  
Créez une API sécurisée RESTful en utilisant Django REST

## Mentor:
Idriss Benjeloun

## Description:   
Ce projet concerne le  developpement d'une API en utilisant Django REST.

les fonctionnalités du projet sont comme suit:

- Une application de suivi des problèmes pour les trois plateformes (site web, applications Android et iOS).
- L'application permettra essentiellement aux utilisateurs de créer divers projets, d'ajouter des utilisateurs 
  à des projets spécifiques, de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes  
  en fonction de leurs priorités, de balises, etc.
- Les trois applications exploiteront les points de terminaison d'API qui serviront les données.


Technologies utilisées:
- framework Django REST;
- SQLite comme base de données de développement locale,



## Exécution du programme
    - installer la derniere version de django (https://docs.djangoproject.com/en/4.1/topics/install/)
    - Créer un dossier projet sur votre machine comme repository local
    - Clonner le repo distant dans votre repository local
    - Se positionner dans le  répertoire "Projet10" avec:
        >> cd Projet10
    - Créer l'environnement virtuel avec:
        >> env python -m venv env
    - Activer l'environnement virtuel avec :
        >> source env/bin/activate
    - Installez les modules necessaires à l'aide du fichier requirement.txt avec:   
        >> pip install -r requirements.txt  
    - Exécuter la migration de la base de données (les modèles) avec: 
        >> python manage.py migrate
    - Lancer le serveur (en fonction de votre version de python) avec :
        >>python manage.py runserver ou >>python3 manage.py runserver
    - tester les requete à partir du l'URL :  http://127.0.0.1:8000/<requete>
      ou via un outil comme Postman.

Remarque: Assurez-vous que votre version de Python est l'une de celles prises 
en charge par la dernière version de Django :
https://docs.djangoproject.com/en/4.1/faq/install/#faq-python-version-support

Nota : les versions appliquées pour ce projet: 
    
    - python : 3.10.5
    - Django : 4.1.1
    - IDE utilisé: pycharm V2022.2.1 (Community Edition)
    - postman a été utilisé pour tester les requêtes de l'API


## Acknowledgments (code inspiration): 
- Discord DA python
- https://openclassrooms.com/fr/courses/7192416-mettez-en-place-une-api-avec-django-rest-framework/
- https://ilovedjango.com/django/rest-api-framework/django-rest-framework/
- https://code.tutsplus.com/tutorials/how-to-authenticate-with-jwt-in-django--cms-30460
- https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5
- https://pypi.org/project/drf-nested-routers/
- https://ilovedjango.com/
- https://stackoverflow.com/questions/71730342/django-rest-framework-method-delete-not-allowed-because-defaultrouter
- https://stackoverflow.com/questions/8159310/why-are-blank-and-null-distinct-options-for-a-django-model
- https://docs.djangoproject.com/en/4.1/ref/models/fields/
- https://stackoverflow.com/questions/24629705/django-using-get-user-model-vs-settings-auth-user-model
- https://www.data-bird.co/python/api-rest
- https://python.doctor/page-django-rest-framework-drf-cours-tuto-tutoriel-exemples
- https://www.youtube.com/watch?v=bpHqfT4kiR8&t=4s
- https://www.django-rest-framework.org/tutorial/3-class-based-views/
- https://learning.postman.com/docs/publishing-your-api/publishing-your-docs/
- https://stackoverflow.com/questions/65860671/nestedsimplerouter-without-using-lookup-in-router
- https://chibisov.github.io/drf-extensions/docs/#nested-routes
- https://medium.com/swlh/using-nested-routers-drf-nested-routers-in-django-rest-framework-951007d55cdc
- https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/


- 

