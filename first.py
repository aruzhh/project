from google.colab import drive
drive.mount('/content/drive/')

path = r'/content/drive/My Drive/'

import urllib.request
from bs4 import BeautifulSoup
import csv

link = 'https://pogoda.mail.ru/country/kazakhstan/january-2021/'
host = 'https://pogoda.mail.ru'
links_cities = []
links_month = []
card_cities = []
weather_day = []
weather_night = []
date = []
city = []
cities = []
necessary_cities = ['Актау', 'Актобе', 'Алматы', 'Атырау', 'Караганда', 'Кызылорда', 'Нур-Султан', 'Павлодар', 'Петропавловск', 'Семей', 'Талдыкорган', 'Тараз', 'Туркестан', 'Усть-Каменогорск', 'Шымкент']

req = urllib.request.urlopen(link)
soup = BeautifulSoup(req, 'html.parser')
card = soup.find_all('span', class_='city-list__val city-list__val-text')
card_cities.extend(card)
for x in card_cities:
    city_name = x.text.strip()
    if city_name in necessary_cities:
        links_cities.append(host + x.find_next('a')['href'])
    else:
        pass


def monyh_link():
    a = 0
    for x in links_cities:
        req2 = urllib.request.urlopen(x)
        soup2 = BeautifulSoup(req2, 'html.parser')
        card1 = soup2.find_all('a', class_='month-menu__month__item')
        for y in card1:
            a = a + 1
            if a < 5:
                pass
            else:
                links_month.append(host + y['href'])
            if a == 12:
                a = 0
    card_cities.clear()
    for i in links_month:
        req3 = urllib.request.urlopen(i)
        soup3 = BeautifulSoup(req3, 'html.parser')
        card_tem = soup3.find_all('div', class_='day__temperature ')
        card_date = soup3.find_all('div', class_='day__date')
        card_city = soup3.find_all('span', class_='js-text pm-toolbar__button__text  pm-toolbar__button__text_noicon pm-toolbar__button__text_dropdown')
        card_cities.extend(card_tem)
        for a in card_cities:
          c = (a.text.split('\n'))
          weather_day.append(c[0])
          weather_night.append(a.find_next('span', class_='day__temperature__night').text.strip())
        card_cities.clear()
        for x in card_date:
          date.append(x.text.strip())
        for y in card_city:
          print(y.text.strip())
    for x in range(0,15):
      city.append(necessary_cities[x])
      for x in city*245:
        cities.append(x)
      city.clear()