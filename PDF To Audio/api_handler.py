import requests
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://api.voicerss.org/?"


class Con:
    def __init__(self):
        self.api_key = os.getenv('api_key')
        self.language = "en-in"
        
        
    def get_mp3(self,src):
        url = f'{BASE_URL}'
        
        params = {
            'key':self.api_key,
            'src':src,
            'hl':self.language,
            'c':'MP3',
        }
        
        response = requests.get(url,params=params)
        print(response.status_code)
        
        if response.status_code == 200:
            # Writes the response to an mp3 file for listening
            with open('test.mp3','wb') as media:
                media.write(response.content)
        else:
            print('Error occured.')
            
            
if __name__ == "__main__":
    x = Con()
    x.text_to_speech('Hello World')