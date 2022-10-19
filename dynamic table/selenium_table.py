import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


# these options are give for chrome driver to open in backgroud without poping any new browser window
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

site = 'https://ahdb.org.uk/cereals-oilseeds-markets' 

PATH = "C:\Program Files (x86)\chromedriver.exe"
wd = webdriver.Chrome(PATH,options=options)
wd.get(site)

# grab the html from page_source 
html = wd.page_source

# load the data into DataFrame 
df = pd.read_html(html)

# print(df[0])

df[1].to_csv('MATIF.csv')

print(df[2])