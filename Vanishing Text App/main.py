import customtkinter as ctk
from customtkinter import CTkLabel,CTkEntry,CTkTextbox
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
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_rowconfigure(1,weight=1)
        
        # Create Frame
        self.text_entry_frame = TextEntryFrame(self.root,entry_width=300,entry_height=200)
        self.text_entry_frame.grid(row=0,column=1,padx=5,pady=5,sticky='new')
        
                
    def on_window_close(self):
        '''Destroys Root'''
        print('Window Closed.')
        self.root.destroy()
        
    def create_buttons(self):
        pass
    
    def start_button(self):
        pass
    


class TextEntryFrame(ctk.CTkFrame):
    def __init__(self,master=None,entry_width=200,entry_height=30,**kwargs):
        super().__init__(master,**kwargs)
        self.entry_width = entry_width
        self.entry_height = entry_height
        self.configure_grid()
        self.text_entry_box()
    
    def configure_grid(self):
        '''Configure the grid system for the frame.'''
        self.grid_columnconfigure(0,weight=3)
        self.grid_rowconfigure(0,weight=3)
        self.grid_rowconfigure(1,weight=3)
        self.grid_rowconfigure(2,weight=3)
    
    def text_entry_box(self):
        text_entry = CTkTextbox(self,font=('arial',20),width=self.entry_width,height=self.entry_height)
        text_entry.grid(row=2,column=0,padx=5,pady=5,sticky='new',rowspan=2)
    
if __name__ == '__main__':
    root = ctk.CTk()
    app = VanishingApp(root)
    root.mainloop()
