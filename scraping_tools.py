# Import des paquets Python:
from bs4 import BeautifulSoup
import requests
import re


def get_digit_from_word(number):
    """
    Convertir nombre lettre en nombre chiffre (de 1 à 5)
    :param number: nombre lettre
    :return: nombre chiffre
    """
    dico = {'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5'}
    return dico.get(number)


def save_data_and_image(response, writer, category_home):
    """
    Enregistrer les données et images des pages livre
    :param response: résultat de requests.get sur l'url des pages catégorie
    :param writer: objet de csv.writer permettant d'écrire dans le fichier data.csv
    :param category_home: résultat de soup.find sur les catégories de la page d'accueil
    :return: writer.writerow des données scrapées et imageFile.write des images
    """
    soup = BeautifulSoup(response.content, 'html.parser')

    # Boucle sur les pages des livres:
    for h3 in soup.findAll('h3'):
        response = requests.get(h3.find('a')['href'].replace('../../../', 'http://books.toscrape.com/catalogue/'))

        # Conditionnel et définition de l'objet soup sur les pages des livres
        if response.ok:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Définition des données des en-têtes de colonnes:
            url_book = h3.find('a')['href'].replace('../../../', 'http://books.toscrape.com/catalogue/')
            title = soup.find('h1').text
            description = soup.findAll('p')[3].text
            category = soup.findAll('a')[3].text
            review = get_digit_from_word(soup.findAll('p')[2]['class'][1])
            url_image = soup.find('img')['src'].replace('../../', 'http://books.toscrape.com/')
            for j in soup.findAll('th'):
                if j.text == 'UPC':
                    code = j.find_next('td').text
                if j.text == 'Price (excl. tax)':
                    price_brut = j.find_next('td').text
                if j.text == 'Price (incl. tax)':
                    price_net = j.find_next('td').text
                if j.text == 'Availability':
                    stock = re.findall(r'\d+', j.find_next('td').text)[0]

            # Écriture des données des en-têtes de colonnes dans le fichier data.csv:
            writer.writerow([url_book, code, title, price_net, price_brut, stock, description, category,
                             review, url_image])

            # Téléchargement des images dans le dossier export/images/:
            response = requests.get(url_image)
            if response.ok:
                with open('export/{}/images/{}.jpg'.format(category_home, code), 'wb') as image_file:
                    image_file.write(response.content)
