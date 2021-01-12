import requests
from bs4 import BeautifulSoup
import os
import re
from fonctions import *

print("Début d'extraction des données")
os.mkdir('export/')
os.mkdir('export/images/')

with open('export/'+'data.csv','a+',newline='') as csvFile:
    csvFile.write('product_page_url,universal_ product_code (upc),title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url\n')

    for i in range(2):
        response = requests.get(pageSite(i))

        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.findAll('h3')
            for h3 in articles:
                urlLinks = pageLivre(h3,'a','href')
                response = requests.get(urlLinks)

                if response.ok:
                    soup = BeautifulSoup(response.text,'html.parser')
                    for i in soup.findAll('th'):
                        if i.text == 'UPC':
                            code = i.findNext('td').text
                        if i.text == 'Price (excl. tax)':
                            priceBrut = i.findNext('td').text.replace('Â','')
                        if i.text == 'Price (incl. tax)':
                            priceNet = i.findNext('td').text.replace('Â','')
                        if i.text == 'Availability':
                            stock = re.findall('\d+',(i.findNext('td').text))[0]
                    title = soup.find('h1').text.replace(',','').replace('/','')
                    description = soup.findAll('p')[3].text.replace(',','').replace('"','')
                    category = soup.findAll('a')[3].text
                    review = chiffre(soup.findAll('p')[2]['class'][1])
                    imageLinks = soup.find('img')['src'].replace('../../','http://books.toscrape.com/')

                    csvFile.write(urlLinks + ',' + code + ',' + title + ',' + priceNet + ',' + priceBrut + ',' + stock + ',' + description + ',' + category + ',' + review + ',' + imageLinks + '\n')
                    saveImage(imageLinks,title)

print("Fin d'extraction des données")