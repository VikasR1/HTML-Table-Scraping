import requests
import urllib.request
from bs4 import BeautifulSoup
from random import randint
import time
from time import sleep 

url = 'https://www.yarnplaza.com/yarn/budgetyarn/budgetyarn-chunky-chenille?qty=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
doc = BeautifulSoup(response.content, 'html.parser')

table_row = doc.select('div#pdetailTableSpecs tr')

# len(table_row)

table_col = doc.select('div#pdetailTableSpecs tr td')

data = {}
for items in doc.select('div#pdetailTableSpecs tr'):
    data[items.select('td')[0].text] = items.select('td')[1].text

print(data)