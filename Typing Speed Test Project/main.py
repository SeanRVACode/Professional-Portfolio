import customtkinter as ctk
from customtkinter import filedialog,CTkLabel,CTkEntry
import os,sys
from ctypes import windll
import time
import random

# # Global Variables
# x = 0

class TypingTest:
    def __init__(self,root):
        self.root = root
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        windll.shcore.SetProcessDpiAwareness(2)
        self.root.title('Typing Speed Test')
        self.root.geometry('800x600')
        self.root.protocol('WM_DELETE_WINDOW',self.on_window_close)
        self.create_entry()
        self.game()
        
    def on_window_close(self):
        '''Destroys Root'''
        print('Window Closed.')
        self.root.destroy()
    
    def start_button(self):
        pass
    
    def create_label(self):
        pass
    
    def create_entry(self):
        self.textbox = CTkEntry(master=root,placeholder_text='Enter Text here.',width=300)
        self.textbox.pack(pady=2,padx=10)
        self.textbox.place(x=200,y=430)
    
    def game(self):
        self.sentences = ["The quick brown fox jumps over the lazy dog.","To be or not to be, that is the question.",
        "I have a dream that one day this nation will rise up.",
        "Four score and seven years ago our fathers brought forth on this continent.",
        "It is a truth universally acknowledged that a single man in possession of a good fortune must be in want of a wife.",
        "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness."]
        self.start = None
        self.end = None
    
        def choose_random_sentence(self):
            self.sentence = random.choice(self.sentences)
            return self.sentence
        
        x = choose_random_sentence(self)
        print(x)
        
        def start_time(self):
            self.start = time.time()
            return self.start
        
        def end_time(self):
            self.end = time.time()
            
        

         


if __name__ == "__main__":
    root = ctk.CTk()
    app = TypingTest(root)
    root.mainloop()