import customtkinter
from PIL import Image
import os,sys

# Set Dark Mode
customtkinter.set_appearance_mod('dark')
customtkinter.set_default_color_theme('dark-blue')

# Destroy window on close
def on_window_close():
    print('Window Closed')
    root.destroy()

# Set up root
root = customtkinter.CTk()
root.title('Watermark Image')
root.geometry('500x350')
root.protocol('WM_DELETE_WINDOW',on_window_close)




    
    