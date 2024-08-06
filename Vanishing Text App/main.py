import customtkinter as ctk
from customtkinter import CTkLabel,CTkEntry
from ctypes import windll
import os,sys
import time




def start_button():
    '''Start button to start the game.'''
    pass

def create_buttons():
    '''Creates all buttons'''



timer = 0

class VanishingApp:
    def __init__(self,root):
        self.root = root
        # Appearance 
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        windll.shcore.SetProcessDpiAwareness(2)
        # General Set up
        self.root.title('Type Vanish')
        self.root.geometry('800x600')
        self.root.protocol('WM_DELETE_WINDOW',self.on_window_close)
        # TODO need to set up grid system.
        # Grid System
        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_columnconfigure(1,weight=1)
        self.root.grid_columnconfigure(2,weight=1)
        self.root.grid_rowconfigure(1,weight=1)
        self.text_entry_box()
                
    def on_window_close(self):
        '''Destroys Root'''
        print('Window Closed.')
        self.root.destroy()
        
    def create_buttons(self):
        pass
    
    def start_button(self):
        pass
    
    def text_entry_box(self):
        '''Text entry box for user to type in.'''
        # TODO need to finish setting up font and get it placed correctly within grid system.
        text_entry = CTkEntry(self.root,font=('arial',20))
        text_entry.grid(row=1,column=1,padx=5,pady=5,sticky='news')
        
    
if __name__ == '__main__':
    root = ctk.CTk()
    app = VanishingApp(root)
    root.mainloop()
