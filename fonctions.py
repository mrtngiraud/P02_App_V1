import requests

#renvoyer l'url d'une page du site
'''
i = numéro d'une page du site
'''
def pageSite(i):
    return 'http://books.toscrape.com/catalogue/page-{}.html'.format(i)

#renvoyer l'url d'une page d'un livre
'''
a = balise head
b = 'balise body'
c = 'class contenant le lien hypertexte'
'''
def pageLivre(a,b,c):
        link = a.find(b)[c]
        return 'http://books.toscrape.com/catalogue/{}'.format(link)

#enregistrer une image
'''
a = url de la page livre
b = titre du livre
'''
def saveImage(a,b):
    response = requests.get(a)
    if response.ok:
        with open('export/images/{}.jpg'.format(b), 'wb') as imageFile:
            imageFile.write(response.content)

#convertir nombre lettre en nombre chiffre (de 1 à 5)
'''
a = nombre en lettre
'''
def chiffre(a):
    dico = {'One':'1','Two':'2','Three':'3','Four':'4','Five':'5'}
    return dico.get(a)




















