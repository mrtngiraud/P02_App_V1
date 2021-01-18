# Import des paquets Python:
from bs4 import BeautifulSoup
import os
import re
import csv
from math import ceil

# Import des fonctions:
from scraping_tools import *

print("Début d'extraction des données")

# Création des dossiers export/ et export/images/:
os.mkdir('export/')

# Boucle sur les pages des catégories:
for i in range(3, 7):
    response = requests.get('http://books.toscrape.com/index.html')

    # Conditionnel et définition de l'objet soup sur la page d'accueil du site:
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        categoryhome = soup.findAll('li')[i].text.replace(' ', '')
        linkcategory = soup.findAll('li')[i].find('a')['href']
        response = requests.get('http://books.toscrape.com/{}'.format(linkcategory))

        # Ouverture d'un fichier data.csv et écriture des en-têtes de colonnes:
        os.mkdir('export/{}/'.format(categoryhome))
        os.mkdir('export/{}/images/'.format(categoryhome))
        with open('export/{}/data.csv'.format(categoryhome), 'a+', newline='', encoding='utf-8-sig') as csvFile:
            writer = csv.writer(csvFile, dialect='excel')
            writer.writerow(['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax',
                             'price_excluding_tax', 'number_available', 'product_description', 'category',
                             'review_rating',
                             'image_url'])

            if response.ok:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Boucle sur les pages des livres:
                for h3 in soup.findAll('h3'):
                    response = requests.get(pagelivre(h3, 'a', 'href'))

                    # Conditionnel et définition de l'objet soup sur les pages des livres
                    if response.ok:
                        soup = BeautifulSoup(response.content, 'html.parser')

                        # Définition des données des en-têtes de colonnes:
                        urllivre = pagelivre(h3, 'a', 'href')
                        title = soup.find('h1').text
                        description = soup.findAll('p')[3].text
                        category = soup.findAll('a')[3].text
                        review = chiffre(soup.findAll('p')[2]['class'][1])
                        urlimage = soup.find('img')['src'].replace('../../', 'http://books.toscrape.com/')
                        for j in soup.findAll('th'):
                            if j.text == 'UPC':
                                code = j.findNext('td').text
                            if j.text == 'Price (excl. tax)':
                                priceBrut = j.findNext('td').text
                            if j.text == 'Price (incl. tax)':
                                priceNet = j.findNext('td').text
                            if j.text == 'Availability':
                                stock = re.findall(r'\d+', j.findNext('td').text)[0]

                        # Écriture des données des en-têtes de colonnes dans le fichier data.csv:
                        writer.writerow([urllivre, code, title, priceNet, priceBrut, stock, description, category,
                                         review, urlimage])

                        # Téléchargement des images dans le dossier export/images/:
                        #saveimage(urlimage, code)
                        response = requests.get(urlimage)
                        if response.ok:
                            with open('export/{}/images/{}.jpg'.format(categoryhome, code), 'wb') as imageFile:
                                imageFile.write(response.content)




            # Répétition sur les pages catégorie
            response = requests.get('http://books.toscrape.com/{}'.format(linkcategory))

            if response.ok:
                soup = BeautifulSoup(response.content, 'html.parser')

                result = int(str(soup.find('form').find('strong').text))
                if result > 20:
                    for l in range(2, ceil(result // 20)+2):
                        linkcategorynext = linkcategory.replace('index', 'page-{}'.format(l))
                        response = requests.get('http://books.toscrape.com/{}'.format(linkcategorynext))

                        if response.ok:
                            soup = BeautifulSoup(response.content, 'html.parser')

                            # Boucle sur les pages des livres:
                            for h3 in soup.findAll('h3'):
                                response = requests.get(pagelivre(h3, 'a', 'href'))

                                # Conditionnel et définition de l'objet soup sur les pages des livres
                                if response.ok:
                                    soup = BeautifulSoup(response.content, 'html.parser')

                                    # Définition des données des en-têtes de colonnes:
                                    urllivre = pagelivre(h3, 'a', 'href')
                                    title = soup.find('h1').text
                                    description = soup.findAll('p')[3].text
                                    category = soup.findAll('a')[3].text
                                    review = chiffre(soup.findAll('p')[2]['class'][1])
                                    urlimage = soup.find('img')['src'].replace('../../', 'http://books.toscrape.com/')
                                    for j in soup.findAll('th'):
                                        if j.text == 'UPC':
                                            code = j.findNext('td').text
                                        if j.text == 'Price (excl. tax)':
                                            priceBrut = j.findNext('td').text
                                        if j.text == 'Price (incl. tax)':
                                            priceNet = j.findNext('td').text
                                        if j.text == 'Availability':
                                            stock = re.findall(r'\d+', j.findNext('td').text)[0]

                                # Écriture des données des en-têtes de colonnes dans le fichier data.csv:
                                writer.writerow([urllivre, code, title, priceNet, priceBrut, stock, description, category,
                                                 review, urlimage])

                                # Téléchargement des images dans le dossier export/images/:
                                response = requests.get(urlimage)
                                if response.ok:
                                    with open('export/{}/images/{}.jpg'.format(categoryhome, code), 'wb') as imageFile:
                                        imageFile.write(response.content)

print("Fin d'extraction des données")
