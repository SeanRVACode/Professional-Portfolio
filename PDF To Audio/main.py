from api_handler import Con
from pdf_handler import PDF
import os

# May need to use API instead of pyttsx3 
# This thought is coming from comments made by people on the course.
# http://www.voicerss.org/login.aspx Potential Free API for text to voice.




class TTS:
    def __init__(self):
        self.con = Con()
        path = input("Please provide the file path of the pdf you would like turned into speech. It must be 100 chars or less.")
        self.pdf = PDF(path)
        if self.check_file_exist(path):
            
            self.con.get_mp3(self.pdf.text_to_send)
        else:
            print("File does not exist")
        
    def check_file_exist(self,path):
        exist = os.path.isfile(path)
        return exist
         

if __name__ == "__main__":
    TTS()