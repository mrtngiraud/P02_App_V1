# Import des paquets Python:
from bs4 import BeautifulSoup
import requests
import re


# Fonction1/ Convertir nombre lettre en nombre chiffre (de 1 à 5):
'''
number = nombre lettre
'''
def get_digit_from_word(number):
    dico = {'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5'}
    return dico.get(number)


# Fonction 2/ Enregistrer les données et images des pages livre:
'''
response = résultat de requests.get sur l'url des pages catégorie
writer = objet de csv.writer permettant d'écrire dans le fichier data.csv
categoryhome = résultat de soup.find sur les catégories de la page d'accueil
'''
def save_data_and_image(response, writer, categoryhome):
    soup = BeautifulSoup(response.content, 'html.parser')

    # Boucle sur les pages des livres:
    for h3 in soup.findAll('h3'):
        response = requests.get(h3.find('a')['href'].replace('../../../', 'http://books.toscrape.com/catalogue/'))

        # Conditionnel et définition de l'objet soup sur les pages des livres
        if response.ok:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Définition des données des en-têtes de colonnes:
            urllivre = h3.find('a')['href'].replace('../../../', 'http://books.toscrape.com/catalogue/')
            title = soup.find('h1').text
            description = soup.findAll('p')[3].text
            category = soup.findAll('a')[3].text
            review = get_digit_from_word(soup.findAll('p')[2]['class'][1])
            urlimage = soup.find('img')['src'].replace('../../', 'http://books.toscrape.com/')
            for j in soup.findAll('th'):
                if j.text == 'UPC':
                    code = j.find_next('td').text
                if j.text == 'Price (excl. tax)':
                    priceBrut = j.find_next('td').text
                if j.text == 'Price (incl. tax)':
                    priceNet = j.find_next('td').text
                if j.text == 'Availability':
                    stock = re.findall(r'\d+', j.find_next('td').text)[0]

            # Écriture des données des en-têtes de colonnes dans le fichier data.csv:
            writer.writerow([urllivre, code, title, priceNet, priceBrut, stock, description, category,
                             review, urlimage])

            # Téléchargement des images dans le dossier export/images/:
            response = requests.get(urlimage)
            if response.ok:
                with open('export/{}/images/{}.jpg'.format(categoryhome, code), 'wb') as imageFile:
                    imageFile.write(response.content)
