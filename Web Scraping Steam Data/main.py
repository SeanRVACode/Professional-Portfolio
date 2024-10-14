from browser_processor import Scraper
import requests
from bs4 import BeautifulSoup
import re
import csv


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

    


# type_links = types_tag.find_all('a')
# types = [t.get_text(strip=True) for t in type_links]
 
with open('./poke.csv','w',encoding='utf-8',newline='') as csvfile:
    fieldnames = ['Number','Name','Typing']
    writer = csv.writer(csvfile,delimiter=',')
    writer.writerow(fieldnames)
    for mon in pokemon:
        numbers.append(mon.find('small').get_text(strip=True))
        names.append(mon.find(class_="ent-name").get_text(strip=True))
        type_links = mon.find_all('a',class_=re.compile('^itype'))
        print(type_links)
        types = [link.get_text(strip=True) for link in type_links]
        type_test.append(types)
    rows = zip(numbers,names,type_test)
    writer.writerows(rows)
        

# for elem in pokemon.


