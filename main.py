import requests
from bs4 import BeautifulSoup

with open('data.csv', 'a+', newline='') as file:
    file.write('product_page_url,universal_ product_code (upc),title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url\n')
    for i in range(2):
        url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.findAll('h3')
            for h3 in articles:
                a = h3.find('a')
                link = a['href']
                urlLinks = ('http://books.toscrape.com/catalogue/' + link)
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
                            stock = i.findNext('td').text.replace('In stock (','').replace(' available)','')
                    title = str(soup.find('h1').text.replace(',',''))
                    description = soup.findAll('p')
                    category = soup.findAll('a')
                    review = soup.findAll('p')[2]['class'][1]
                    if review == 'One':
                        review = '1'
                    if review == 'Two':
                        review = '2'
                    if review == 'Three':
                        review = '3'
                    if review == 'Four':
                        review = '4'
                    if review == 'Five':
                        review = '5'
                    image = soup.find('img')['src'].replace('../../','http://books.toscrape.com/')
                    file.write( urlLinks + ',' + code + ',' + title + ',' + priceNet + ',' + priceBrut + ',' + stock + ',' + description[3].text.replace(',','') + ',' + category[3].text + ',' + review + ',' + image + '\n')




