from bs4 import BeautifulSoup
import requests




class Scraper(BeautifulSoup):
    def __init__(self,html='https://steamdb.info/',parser='html.parser'):
        super().__init__()
        self.headers = {
            'User-Agent':'Mozilla/5.0'
        }
        
        response = requests.get(html)
        
        print(response)
        