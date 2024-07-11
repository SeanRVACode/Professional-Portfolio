from tkinter import END
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
        # Configures the grid.
        for i in range(4):
            self.root.grid_rowconfigure(i,weight=1,minsize=150)
        for j in range(3):
            self.root.grid_columnconfigure(j,weight=1,minsize=266)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        windll.shcore.SetProcessDpiAwareness(2)
        self.root.title('Typing Speed Test')
        self.root.geometry('800x600')
        self.root.protocol('WM_DELETE_WINDOW',self.on_window_close)
        self.sentences = ["The quick brown fox jumps over the lazy dog.","To be or not to be, that is the question.",
        "I have a dream that one day this nation will rise up.","Four score and seven years ago our fathers brought forth on this continent.","It is a truth universally acknowledged that a single man in possession of a good fortune must be in want of a wife.","It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness."]
        self.wpm = 0
        self.create_entry()
        self.create_buttons()
        self.create_labels()
        
            
    def on_window_close(self):
        '''Destroys Root'''
        print('Window Closed.')
        self.root.destroy()
        
    def create_buttons(self):
        self.start_button()
        

    def start_button(self):
        '''Function that sets up the start button. Start button
        also acts as a reset function.'''

        self.start_button = ctk.CTkButton(master=self.root,text='Start Game',command=self.start_time)
        self.start_button.grid(row=3,column=1,padx=5,pady=5,sticky='')
    
    def sentence_label(self):
        '''Sentence label to display what the user is supposed to type.'''

        self.sentence_l= CTkLabel(master=self.root,font=('arial',20),text='Press Start To Begin',anchor='center',wraplength=750)
        self.sentence_l.grid(row=1,column=0,padx=5,pady=5,sticky='',columnspan=3)
        
    
    def create_labels(self):
        '''Creates the labels on the application.'''
        self.sentence_label()
        self.wpm_label()
    
    def create_entry(self):
        '''Entry for user.'''
        self.var = ctk.StringVar()
        self.var.trace_add('write',self.check_input)
        self.textbox = CTkEntry(master=self.root,placeholder_text='Enter Text here.',width=300,textvariable=self.var)
        self.textbox.grid(row=2,column=1,padx=8,pady=8)
        self.textbox.configure(state='disabled')
        
    def wpm_label(self):
        self.label_wpm = CTkLabel(master=self.root,text=f'WPM: {self.wpm}',anchor='center',font=('arial',20))
        self.label_wpm.grid(row=0,column=2,padx=8,pady=8)
        
        
    def clear_entry(self):
        self.textbox.configure(state='normal')
        self.textbox.delete(0,'end')
        self.textbox.configure(state='disabled')
        
    def start_time(self):
        self.clear_entry()
        self.start = time.time()
        self.chosen_sentence = random.choice(self.sentences)
        print(self.chosen_sentence)
        self.sentence_l.configure(text=self.chosen_sentence)
        self.textbox.configure(state='normal')
        self.textbox.focus_set()

        
    def check_input(self,*args):
        '''Constantly checks to see if user input matches the sentence.'''
        current_input = self.var.get()
        elapsed_time = time.time() - self.start
        if elapsed_time > 0:
            self.wpm = round(len(current_input)/(5*(elapsed_time/60)),2)
            self.label_wpm.configure(text=f'WPM: {self.wpm}')
        if current_input == self.chosen_sentence:
            self.end_time()
            print('Match Found!')
            self.textbox.configure(state='disabled')
            wpm = self.calculate_wpm()
            self.label_wpm.configure(text=f'WPM: {wpm}')
    
    def calculate_wpm(self) -> int:
        '''Calculates WPM and returns it as an int.'''
        elapsed_time = self.end - self.start
        wpm = round(len(self.chosen_sentence)/(5*(elapsed_time/60)),2)
        return wpm
        
    def end_time(self):
        '''Gets end time.'''
        self.end = time.time()
            
        

         


if __name__ == "__main__":
    root = ctk.CTk()
    app = TypingTest(root)
    root.mainloop()