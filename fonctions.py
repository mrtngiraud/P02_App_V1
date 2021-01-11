#enregistrement des images:

import requests

def saveImage(a,b):
    response = requests.get(a)
    if response.ok:
        with open('export/images/{}.jpg'.format(b), 'wb') as imageFile:
            imageFile.write(response.content)










