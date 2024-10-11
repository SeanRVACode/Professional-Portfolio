from browser_processor import Scraper
import requests
from bs4 import BeautifulSoup
import re


url = 'https://pokemondb.net/pokedex/national'
headers = {
    'User-Agent':'Mozilla/5.0'
}
response = requests.get(url,headers=headers)
# print(response.text)

soup = BeautifulSoup(response.text,'html.parser')


pokemon = soup.find_all(name='span',class_='infocard-lg-data text-muted')

types = []
numbers = []
names = []
types = []
type_test = []
for mon in pokemon:
    numbers.append(mon.find('small').get_text(strip=True))
    names.append(mon.find(class_="ent-name").get_text(strip=True))
    type_test.append(mon.find(class_=re.compile("itype ")))


# type_links = types_tag.find_all('a')
# types = [t.get_text(strip=True) for t in type_links]
        
print(type_test)
    

print(numbers)
print(names)

# for elem in pokemon.


