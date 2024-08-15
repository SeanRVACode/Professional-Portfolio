from pypdf import PdfReader



class PDF:
    def __init__(self,path):
        print(path)
        
        # Reads the text of the pdf
        self.text = self.extract_pdf_text(path)
        print(self.text)
        
        self.text_to_send = self.limit_to_100(self.text)
        
        
        
    def limit_to_100(self,text):
        # Set the max size in bytes
        max_size = 1024
        
        # Encode the string
        encoded_string = text.encode('utf-8')
        
        # Encode the string to bytes and check its length
        size_in_bytes = len(encoded_string)
        
        
        if len(encoded_string) > max_size:
            # Truncate the string to fit within the limit
            print('The pdf text will be shortened to fit API requirements.')
            
            truncated_string = encoded_string[:max_size]
            
            return truncated_string
        
        
        else:
            
            return encoded_string
        
    def extract_pdf_text(self,path):
        with open(path,'rb') as file:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
            
        
        
        
        