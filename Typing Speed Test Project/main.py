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
        for i in range(4):
            self.root.grid_rowconfigure(i,weight=1,minsize=150)
        for j in range(3):
            self.root.grid_columnconfigure(j,weight=1,minsize=266)
        # self.create_grid()
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        windll.shcore.SetProcessDpiAwareness(2)
        self.root.title('Typing Speed Test')
        self.root.geometry('800x600')
        self.root.protocol('WM_DELETE_WINDOW',self.on_window_close)
        self.create_entry()
        self.create_buttons()
        self.create_labels()
        self.sentences = ["The quick brown fox jumps over the lazy dog.","To be or not to be, that is the question.",
        "I have a dream that one day this nation will rise up.",
        "Four score and seven years ago our fathers brought forth on this continent.",
        "It is a truth universally acknowledged that a single man in possession of a good fortune must be in want of a wife.",
        "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness."]
        
    def create_grid(self):
        self.frames=[]
        for row in range(4):
            row_frames = []
            for col in range(3):
                
                # frame = ctk.CTkFrame(self.root)
                # frame.grid(row=row,column=col,padx=5,pady=5,sticky='nsew')
                # label = ctk.CTkLabel(frame,text=f'Row {row}, Col {col}',anchor='center')
                # label.pack(side='top',fill='both',expand=True)
                row_frames.append(frame)
            self.frames.append(row_frames)
            
    def on_window_close(self):
        '''Destroys Root'''
        print('Window Closed.')
        self.root.destroy()
        
    def create_buttons(self):
        self.start_button()
        

    def start_button(self):
        '''Function that sets up the start button.'''

        self.start_button = ctk.CTkButton(master=self.root,text='Start Game',command=self.start_time)
        self.start_button.grid(row=3,column=1,padx=5,pady=5,sticky='')
    
    def sentence_label(self):

        self.sentence_l= CTkLabel(master=self.root,font=('arial',20),text='Press Start To Begin',anchor='center',wraplength=750)
        self.sentence_l.grid(row=1,column=0,padx=5,pady=5,sticky='',columnspan=3)
        
    
    def create_labels(self):
        self.sentence_label()
    
    def create_entry(self):
        self.textbox = CTkEntry(master=self.root,placeholder_text='Enter Text here.',width=300)
        self.textbox.grid(row=2,column=1,padx=8,pady=8)
        self.textbox.configure(state='disabled')
    
    def choose_random_sentence(self):
        self.sentence = random.choice(self.sentences)
    
        
    def start_time(self):
        self.start = time.time()
        self.chosen_sentence = random.choice(self.sentences)
        print(self.chosen_sentence)
        self.sentence_l.configure(text=self.chosen_sentence)
        self.textbox.configure(state='normal')
        self.textbox.focus_set()
        match = False
        
        while not match:
            var = ctk.StringVar(self.root)
            print(var.trace_add("w",self.check_entry_match()))
            
        
    def check_entry_match(self):
        user_input = self.textbox.get()
        
        if self.chosen_sentence in user_input:
            return True
        
        
            
            
    
    def end_time(self):
        self.end = time.time()
            
        

         


if __name__ == "__main__":
    root = ctk.CTk()
    app = TypingTest(root)
    root.mainloop()