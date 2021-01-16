# Import des paquets Python:
import requests

# Fonction1/ Renvoyer l'url d'une page du site:
'''
i = numéro d'une page du site
'''
def pagesite(i):
    return 'http://books.toscrape.com/catalogue/page-{}.html'.format(i)


# Fonction2/ Renvoyer l'url d'une page d'un livre:
'''
a = balise head de b
b = 'balise body de c'
c = 'class de c du lien hypertexte'
'''
def pagelivre(a, b, c):
    link = a.find(b)[c]
    return 'http://books.toscrape.com/catalogue/{}'.format(link)


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
