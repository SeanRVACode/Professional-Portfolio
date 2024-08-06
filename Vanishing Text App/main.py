import customtkinter as ctk
from ctypes import windll
import os,sys
import time

def on_window_close():
    '''Destroys Root'''
    print('Window Closed.')
    root.destroy()

# Appearance 
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')
windll.shcore.SetProcessDpiAwareness(2)

# General Set up
root = ctk.CTk()
root.title('Type Vanish')
root.geometry('800x600')
root.protocol('WM_DELETE_WINDOW',on_window_close)
timer = 0

