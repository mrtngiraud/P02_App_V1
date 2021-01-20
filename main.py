# Import des paquets Python:
import requests
from bs4 import BeautifulSoup
import os
import csv
from math import ceil

# Import des fonctions:
from scraping_tools import save_data_and_image

print("Début d'extraction des données")

# Création du dossier export/:
os.mkdir('export/')

# Boucle sur les 50 pages catégorie 'index' du site:
for i in range(3, 53):
    response = requests.get('http://books.toscrape.com/index.html')

    # Conditionnel et définition de l'objet soup sur la page accueil du site:
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        category_home = soup.findAll('li')[i].get_text("\n", strip=True)
        link_category = soup.findAll('li')[i].find('a')['href']
        response = requests.get('http://books.toscrape.com/{}'.format(link_category))

        # Création des dossiers et fichiers d'extraction des données et images:
        os.mkdir('export/{}/'.format(category_home))
        os.mkdir('export/{}/images/'.format(category_home))
        with open('export/{}/data.csv'.format(category_home), 'a+', newline='', encoding='utf-8-sig') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            writer.writerow(['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax',
                             'price_excluding_tax', 'number_available', 'product_description', 'category',
                             'review_rating', 'image_url'])

            # Enregistrement des données et images des pages catégorie "index"
            if response.ok:
                save_data_and_image(response, writer, category_home)

            # Boucle sur les pages catégorie 'next'
            response = requests.get('http://books.toscrape.com/{}'.format(link_category))
            
            if response.ok:
                soup = BeautifulSoup(response.content, 'html.parser')

                result = int(str(soup.find('form').find('strong').text))
                if result > 20:
                    for k in range(2, ceil(result // 20)+2):
                        link_category_next = link_category.replace('index', 'page-{}'.format(k))
                        response = requests.get('http://books.toscrape.com/{}'.format(link_category_next))

                        # Enregistrement des données et images des pages catégorie "next"
                        if response.ok:
                            save_data_and_image(response, writer, category_home)

print("Fin d'extraction des données")
