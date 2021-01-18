# OpenClassrooms
## Développeur d'application - Python
### Projet n°2 : Utilisez les bases de Python pour l'analyse de marché
***
#### 1. Informations générales
Ce projet a pour objectif d'automatiser le processus d'extraction des données marketing du site internet [Books to Scrap](http://books.toscrape.com), un revendeur de livres d'occasion.
<br/>

Pour cela, un script Python a été développé, mettant principalement en oeuvre les techniques de "scrapping", afin d'enregistrer :
* dans un dossier **export/** :
  * un fichier **data.csv** contenant les informations suivantes :
    * product_page_url 
    * universal_ product_code (upc)
    * title
    * price_including_tax
    * price_excluding_tax
    * number_available
    * product_description
    * category
    * review_rating
    * image_url
* dans un dossier **export/images/** :
  * les couvertures des livres au format **titre.jpg**
***
#### 2. Démarrage

Afin d'exécuter le script (main.py) correctement, il est recommandé, dans l'ordre :

######2.1 d'avoir déjà installé Python dans une version >= 3.4

Dans une ligne de terminal, écrire :

        python3 --version

Si vous recevez un message d'erreur indiquant que Python est introuvable,
ou un message similaire, il est probable que votre installation de Python
soit incorrecte ou manquante. Dans ce cas, vous devez télécharger et installer
la dernière version de Python avant de continuer.

Sinon vous devrier voir s'afficher Python 3.4...

######2.3 de créer un environnement virtuel à la racine du dossier projet

Dans une ligne de terminal, viser le dossier et écrire :

        python3 -m venv env

######2.4 d'activer l'environnement virtuel créé précédemment

Dans une ligne de terminal, écrire:

        source env/bin/activate

######2.5 d'installer les paquets Python suivants dans l'environnement virtuel activé précédemment

Dans une ligne de terminal, écrire :

        pip3 install beautifulsoup4
        pip3 install requests

Pour plus d'informations, consulter PyPi.org.

######2.6 de vérifier la bonne installation des paquets Python

Dans une ligne de terminal, taper :

        pip3 freeze

Vous devriez obtenir :

        beautifulsoup4==4.9.3
        bs4==0.0.1
        certifi==2020.12.5
        chardet==4.0.0
        idna==2.10
        requests==2.25.1
        soupsieve==2.1
        urllib3==1.26.2

######6. d'exécuter le script

Dans une ligne de terminal, taper :
        
        python3 main.py

Si, pour une raison, vous devez relancer l'exécution du script,
veillez à bien supprimer le dossier export généré auparavant,
sinon le message d'erreur ci-dessous s'affiche :

        Traceback (most recent call last):
        File "main.py", line 5, in <module>
        os.mkdir('export/')
        FileExistsError: [Errno 17] File exists: 'export/'

######7. d'attendre la fin de l'exécution du script avant de consulter les données "scrapées" dans le dossier export/ généré

***
#### 3. Auteur

Martin GIRAUD
<br/>
mrtngiraud@gmail.com

