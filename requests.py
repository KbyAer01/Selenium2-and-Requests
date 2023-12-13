# -*- coding: utf-8 -*-

# Импорты необходимых библиотек
import requests
import json
import re
import csv
from bs4 import BeautifulSoup

# Открытие файла для записи данных
file = open('regions.csv', 'w')

# Парсинг текущего IP-адреса с сайта 'https://2ip.ru'
ipResponse = requests.get('https://2ip.ru')
soup = BeautifulSoup(ipResponse.text, 'html.parser')
ip_element = soup.find('div', {'class': 'ip'})
ip_address = ip_element.span.text

# Заголовок 'Authorization' с использованием токена, полученного с сайта 'https://www.maxmind.com'
token = 'v2.local.IHbxbaA4wMboaUYOMdjNQQoDP2nOcvQcDAQIx3bd--sCk_W9B9oe4RgJtQExEUq6Ai2u3XkCwv9xEpHaB_eLdiGG3xyEsVrjEOkU-Nj97NnDijjbfc9W73BjAJRuFhrrWqleNKp_186FkHMaSK6lkXHOmJe2xuFetYG9TFwSgVGnxqJ6QXTD_h4ZrEkcdTioVOCdPkHCKFh5GurR'
geoResponse = requests.get(f"https://geoip.maxmind.com/geoip/v2.1/city/{ip_address}?demo=1",
                           headers={'Authorization': f'Bearer {token}'})
timeZone = json.loads(geoResponse.content)["location"]["time_zone"]

#test str
# Получение данных о часовых поясах с внешнего ресурса 'https://gist.github.com/salkar/19df1918ee2aed6669e2.js'
timezonesResponse = requests.get("https://gist.github.com/salkar/19df1918ee2aed6669e2.js")
timezonesResponse.encoding = timezonesResponse.apparent_encoding
text = timezonesResponse.text
timeZonesPos = [m.start() for m in re.finditer(timeZone, text)]

# Запись данных в файл 'regions.csv'
with file:
    writer = csv.writer(file)
    writer.writerow([timeZone])
    returnStr = ''
    for timeZonePos in timeZonesPos:
        rightSidePos = text.rindex(",", None, timeZonePos)
        leftSidePos = text.rindex('[', None, timeZonePos) + 1
        subStr = text[leftSidePos: rightSidePos].replace("&quot;",'')
        returnStr = returnStr + subStr + ', '
    writer.writerow([returnStr])
