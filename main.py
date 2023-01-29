import bs4
import requests
import openpyxl
import pandas as pd

url = "http://www.cbr.ru/scripts/XML_daily.asp"
url_code = requests.get(url)
soup = bs4.BeautifulSoup(url_code.text, 'html.parser')
names = soup.find_all('name')
engnames = soup.find_all('charcode')
nominals = soup.find_all('nominal')
parentcodes = soup.find_all('value')
currencies = []
for i in range(0, len(nominals)):
    rows = [names[i].get_text(),
            engnames[i].get_text(),
            nominals[i].get_text(),
            parentcodes[i].get_text()]
    currencies.append(rows)

valuta = pd.DataFrame(currencies, columns=['name', 'charcode', 'nominal', 'value'])
valuta.to_excel('valuta.xlsx', index = False)