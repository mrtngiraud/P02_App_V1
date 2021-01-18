# Import des paquets Python:
import requests
from bs4 import BeautifulSoup

# Fonction1/ Renvoyer l'url d'une page d'une catégorie d'un livre:
'''
a = balise head de b
b = 'balise body de c'
c = 'class de c du lien hypertexte'
i = itération de 3 à 53
def pagecategorie(a, b, c, i):
    response = requests.get('http://books.toscrape.com/index.html')
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        link = soup.findAll(a)[i].find(b)[c]
        return 'http://books.toscrape.com/{}'.format(link)
'''

# Fonction2/ Renvoyer l'url d'une page d'un livre:
'''
a = balise head de b
b = 'balise body de c'
c = 'class de c du lien hypertexte'
'''
def pagelivre(a, b, c):
    linklivre = a.find(b)[c]
    return linklivre.replace('../../../', 'http://books.toscrape.com/catalogue/')

# Fonction3/ Convertir nombre lettre en nombre chiffre (de 1 à 5):
'''
a = nombre lettre
'''
def chiffre(a):
    dico = {'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5'}
    return dico.get(a)




# Fonction4/ Enregistrer une image:
'''
a = url de la page d'un livre
b = titre du livre
'''
def saveimage(a, b):
    response = requests.get(a)
    if response.ok:
        with open('export/images/{}.jpg'.format(b), 'wb') as imageFile:
            imageFile.write(response.content)
