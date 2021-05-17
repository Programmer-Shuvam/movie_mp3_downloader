from bs4 import BeautifulSoup
# import cfscrape
import requests
# srcape = cfscrape.create_scraper()
source = requests.get('http://extramovies.casa/?s=lootcase').text
soup = BeautifulSoup(source, 'lxml')
print(soup)
# <div class="center"><button>Aloo</button></div>
