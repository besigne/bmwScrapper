import requests
from bs4 import BeautifulSoup
from model.car import Car
import csv

page = requests.get('https://www.bmw.com.br/pt/all-models.html')

soup = BeautifulSoup(page.text, "html.parser")
car_models = soup.find_all('div', {'class': 'cmp-modelcard__entry'})

BMW = []
bmw = Car

for cars in car_models:
    car = cars.find('h5', {'class': 'cmp-modelcard__name'})
    car = car.get_text()

    fuel = cars.find('div', {'class': 'cmp-modelcard__fuel-type'})
    fuel = fuel.get_text()
    fuel = fuel.replace(' ', '')
    fuel = fuel.replace('•',' with ')

    price = cars.find('span', {'class': 'cmp-modelcard__price'})
    price = price.get_text()
    price = price.replace(' A partir de ', '')
    price = price.replace(' à vista*. ', '')
    price = price.replace(' à vista* ', '')

    if price == '':
        price = 'Multiple values, please verify website'

    if fuel == '':
        fuel = 'More than one version available, please verify website'

    bmw = Car(name=car, price=price, fuel=fuel)
    BMW = BMW + [bmw]

filename = 'bmw.csv'

try:
    with open(filename, 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        for row in BMW:
            writer.writerow([row.name, row.price, row.fuel])

except BaseException as e:
    print('BaseException', filename)
else:
    print("Created CSV Successfully!")
