import pypdf
import requests
from api_handler import Con


# May need to use API instead of pyttsx3 
# This thought is coming from comments made by people on the course.
# http://www.voicerss.org/login.aspx Potential Free API for text to voice.




class TTS:
    def __init__(self,text=""):
        self.x = Con()
        self.x.get_mp3(text)
        
        


if __name__ == "__main__":
    TTS("Beep Boop")