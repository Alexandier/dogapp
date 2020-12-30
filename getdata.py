import requests
from bs4 import BeautifulSoup

def getdata(osoite):

    koiralista = []

    kuvalista = []

    URL = osoite

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    nimet = soup.find_all('a', class_='list-item-title')

    kuvat = soup.find_all('img', class_='list-item-breed-img')

    for laji in nimet:
        koiralista.append(list(laji)[0])

    for laji in kuvat:
        kuvalista.append(laji.get('src'))

    return koiralista, kuvalista