import requests
from bs4 import BeautifulSoup
import mysql.connector
from unidecode import unidecode

# You should change this based on your config
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='learn')

cursor = cnx.cursor()

response = requests.get('https://divar.ir/')
soup = BeautifulSoup(response.text, 'html.parser')

for wrapper in soup.find_all('div', {'class': 'city-group__header'}):
    if wrapper.text == 'همه‌ی شهرها':
        print('22222')
        x = wrapper.find_next('div')
        # print(x)
        # s = BeautifulSoup(x.text, 'html.parser')
        # print(soup)
        all_cities = x.find_all('a', {'class': 'ui button'})
        # print(all_cities)
        for cityIndex, city in enumerate(all_cities, start=1):
            city_link = ('https://divar.ir' +
                         city.get('href') + '/buy-apartment')
            res = requests.get(city_link)
            soup = BeautifulSoup(res.text, 'html.parser')
            all_apartments = soup.find_all('a', {'class': 'post-card'})

            if city_link != 'https://divar.ir/s/tehran/buy-apartment':
                for apartment in all_apartments:
                    apartment_link = ('https://divar.ir' +
                                      apartment.get('href'))
                    response = requests.get(apartment_link)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    div = soup.find_all(
                        'span', {'class': 'post-fields-item__title'})
                    link = apartment_link.split('/')[-1]
                    cursor.execute(
                        'SELECT count(*) FROM apartment where link = "%s"' % (link))
                    repeated = cursor.fetchone()
                    if repeated[0] == 0:
                        # print(link)
                        for element in div:
                            if element.text == 'متراژ':
                                size = element.find_next('div').text
                                index = size.find('م')
                                size = size[:index]
                                size = unidecode(size)
                                size = size.replace('.', '')
                            if element.text == 'سال ساخت':
                                date = element.find_next('div').text
                                date = unidecode(date)
                                if date == 'qbl z 1370':
                                    date = '1370'
                            if element.text == 'قیمت کل':
                                price = element.find_next('div').text
                                index = price.find('ت')
                                price = price[:index]
                                price = unidecode(price)
                                price = price.replace('.', '')
                        if price != '':
                            cursor.execute('INSERT INTO apartment (region, size, date, price, link) VALUES ("%s", "%s", "%s", "%s", "%s")' %
                                           (cityIndex, size, date, price, link))
                            cnx.commit()

                    else:
                        print('duplicated: ' + link)
