import requests
from bs4 import BeautifulSoup
from model.audi import Audi
import csv


page = requests.get('https://www.audiusa.com/us/web/en/models.html')

soup = BeautifulSoup(page.text, 'html.parser')
cars = soup.find_all('div', {'class': 'audi-modelfinder__car-model-copy'})

AUDI = []
audi = Audi

for car in cars:
    name = car.find('span', {'class': 'audi-copy-m audi-modelfinder__car-model-body-type'}).get_text()
    try:
        price = car.find('p', {'class': 'audi-copy-s audi-modelfinder__car-model-price'}).get_text()
    except BaseException as e:
        price = 'No price available'

    audi = Audi(name=name, price=price)
    AUDI = AUDI + [audi]

filename = 'audi.csv'

try:
    with open(filename, 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        for row in AUDI:
            writer.writerow([row.name, row.price])

except BaseException as e:
    print('BaseException', filename)
else:
    print("Created CSV Successfully!")
