# Import des paquets Python:
from bs4 import BeautifulSoup
import os
import re

# Import des fonctions:
from fonctions import *

print("Début d'extraction des données")

# Création des dossiers export/ et export/images/:
os.mkdir('export/')
os.mkdir('export/images/')

# Ouverture d'un fichier data.csv et écriture des en-têtes de colonnes:
with open('export/'+'data.csv', 'a+', newline='') as csvFile:
    csvFile.write('product_page_url,universal_ product_code (upc),title,price_including_tax,price_excluding_tax,'
                  'number_available,product_description,category,review_rating,image_url\n')

    # Boucle sur les 50 pages du site:
    for i in range(51):
        response = requests.get(pagesite(i))

        # Conditionnel et définition de l'objet soup sur les pages du site:
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Boucle sur les pages des livres:
            for h3 in soup.findAll('h3'):
                response = requests.get(pagelivre(h3, 'a', 'href'))

                # Conditionnel et définition de l'objet soup sur les pages des livres
                if response.ok:
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Définition des données des en-têtes de colonnes:
                    urlLinks = pagelivre(h3, 'a', 'href')
                    title = soup.find('h1').text.replace(',', '').replace('/', '')
                    description = soup.findAll('p')[3].text.replace(',', '').replace('"', '')
                    category = soup.findAll('a')[3].text
                    review = chiffre(soup.findAll('p')[2]['class'][1])
                    imageLinks = soup.find('img')['src'].replace('../../', 'http://books.toscrape.com/')
                    for j in soup.findAll('th'):
                        if j.text == 'UPC':
                            code = j.findNext('td').text
                        if j.text == 'Price (excl. tax)':
                            priceBrut = j.findNext('td').text.replace('Â', '')
                        if j.text == 'Price (incl. tax)':
                            priceNet = j.findNext('td').text.replace('Â', '')
                        if j.text == 'Availability':
                            stock = re.findall(r'\d+', j.findNext('td').text)[0]

                    # Écriture des données des en-têtes de colonnes dans le fichier data.csv:
                    csvFile.write(urlLinks + ',' + code + ',' + title + ',' + priceNet + ',' + priceBrut + ','
                                  + stock + ',' + description + ',' + category + ',' + review + ',' + imageLinks + '\n')

                    # Téléchargement des images dans le dossier export/images/:
                    saveimage(imageLinks, title)

print("Fin d'extraction des données")
