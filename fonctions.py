import requests
from bs4 import BeautifulSoup

#enregistrer des images:
'''
a = url de la page livre
b = titre du livre
'''
def saveImage(a,b):
    response = requests.get(a)
    if response.ok:
        with open('export/images/{}.jpg'.format(b), 'wb') as imageFile:
            imageFile.write(response.content)

#convertir nombre en lettre vers nombre en chiffre (de 1 à 5)
'''
a = chiffre écrit en lettre
'''
def chiffre(a):
    dico = {'One':'1','Two':'2','Three':'3','Four':'4','Five':'5'}
    return dico.get(a)










