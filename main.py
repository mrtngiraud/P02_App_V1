# Import des paquets Python
import requests
from bs4 import BeautifulSoup
import os

# Création du répertoire destinataire des données scrappées
# dossier export à la racine du dossier projet
os.mkdir('export/')
# dossier images à la racine du dossier export
os.mkdir('export/images/')

# Création et ouverture du fichier data.csv en écriture et lecture
with open('export/'+'data.csv','a+',newline='') as csvFile:
    # Écriture des en-têtes de colonnes du tableau du fichier data.csv
    csvFile.write('product_page_url,universal_ product_code (upc),title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url\n')

    # Boucle itérative à travers les 50 pages url du site internet
    for i in range(51):
        url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
        # Définition de l'objet response comme résultat de la fonction requests.get sur chaque url
        response = requests.get(url)

        # Conditionnel si le code de l'objet response obtenu est 200
        if response.ok:
            # Définition de l'objet soup comme résultat de la fonction Beautifulsoup sur l'objet response
            soup = BeautifulSoup(response.text, 'html.parser')
            # Définition de l'objet articles comme résultat de la fonction findALL sur les balises h3
            articles = soup.findAll('h3')
            # Boucle itérative à travers toutes les balises h3
            for h3 in articles:
                # Définition de l'objet a comme première balise a rencontrée dans l'objet articles
                a = h3.find('a')
                # Définition de l'objet link comme partie de l'url contennue dans l'objet a
                link = a['href']
                # Définition de l'objet urlLinks comme url vers les objets articles
                urlLinks = ('http://books.toscrape.com/catalogue/' + link)
                # Définition de l'objet response comme résultat de la fonction requests.get sur chaque urlLinks
                response = requests.get(urlLinks)

                # Conditionnel si le code de l'objet response obtenu est 200
                if response.ok:
                    # Définition de l'objet soup comme résultat de la fonction Beautifulsoup sur l'objet response
                    soup = BeautifulSoup(response.text,'html.parser')
                    # Boucle itérative à travers toutes les balises th
                    for i in soup.findAll('th'):
                        # Conditionnel si le texte de la balise th vaut 'UPC'
                        if i.text == 'UPC':
                            # Définition de l'objet code comme texte de la balise td trouvée après si vrai
                            code = i.findNext('td').text
                        # Conditionnel si le texte de la balise th vaut 'Price (excl. tax)'
                        if i.text == 'Price (excl. tax)':
                            # Définition de l'objet priceBrut comme texte de la balise td trouvée après si vrai
                            priceBrut = i.findNext('td').text.replace('Â','')
                        # Conditionnel si le texte de la balise th vaut 'Price (incl. tax)'
                        if i.text == 'Price (incl. tax)':
                            # Définition de l'objet priceNet comme texte de la balise td trouvée après si vrai
                            priceNet = i.findNext('td').text.replace('Â','')
                        # Conditionnel si le texte de la balise th vaut 'Availability'
                        if i.text == 'Availability':
                            # Définition de l'objet stock comme texte de la balise td trouvée après si vrai
                            stock = i.findNext('td').text.replace('In stock (','').replace(' available)','')
                    # Définition de l'objet title comme texte de la première balise h1
                    title = str(soup.find('h1').text.replace(',','')).replace('/','')
                    # Définition de l'objet description comme toutes les balises p
                    description = soup.findAll('p')
                    # Définition de l'objet cateory comme toutes les balises a
                    category = soup.findAll('a')
                    # Définition de l'objet review comme deuxième argument class de la troisième balise p
                    review = soup.findAll('p')[2]['class'][1]
                    # Conditionnels attribuant un résultat chiffré à l'objet review
                    if review == 'One':
                        review = '1'
                    if review == 'Two':
                        review = '2'
                    if review == 'Three':
                        review = '3'
                    if review == 'Four':
                        review = '4'
                    if review == 'Five':
                        review = '5'
                    # Définition de l'objet imageLinks comme partie de l'url de l'argument src de la balise src
                    imageLinks = soup.find('img')['src'].replace('../../','http://books.toscrape.com/')
                    # Écriture des objets définis comme données des en-têtes de colonnes du fichier data.csv
                    csvFile.write(urlLinks + ',' + code + ',' + title + ',' + priceNet + ',' + priceBrut + ',' + stock + ',' + description[3].text.replace(',','').replace('"','') + ',' + category[3].text + ',' + review + ',' + imageLinks + '\n')

                    # Définition de l'objet response comme résultat de la fonction requests.get sur chaque imageLinks
                    response = requests.get(imageLinks)
                    # Conditionnel si le code de l'objet response obtenu est 200
                    if response.ok:
                        # Définition de l'objet imageName comme chaîne titre.jpg
                        imageName = title + '.jpg'
                        # Définition de l'objet imageFile comme fichier titre.jpg ouvert en écritureb dans le dossier export/image
                        imageFile = open('export/images/'+imageName, 'wb')
                        # Ecriture de l'image de l'objet response dans le fichier titre.jpg
                        imageFile.write(response.content)