import customtkinter
from customtkinter import filedialog,CTkLabel,CTkEntry
import os,sys
from ctypes import windll


# DPI Scaling
windll.shcore.SetProcessDpiAwareness(2)

# Set Dark Mode
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Destroy window on close
def on_window_close():
    '''Destroys root.'''
    print('Window Closed.')
    root.destroy()
    
# Set up root
root = customtkinter.CTk()
root.title('Typing Speed Test')
root.geometry('800x600')
root.protocol('WM_DELETE_WINDOW',on_window_close)

