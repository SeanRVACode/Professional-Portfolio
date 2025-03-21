from tkinter.colorchooser import askcolor
import customtkinter
from customtkinter import filedialog,CTkLabel,CTkImage,CTkSlider,CTkButton
from PIL import Image,ImageFont,ImageDraw,ImageTk
import os,sys
from ctypes import windll
import matplotlib.pyplot as plt
import tkinter as tk

from numpy import choose


# DPI Scaling
windll.shcore.SetProcessDpiAwareness(2)

# Set Dark Mode
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Destroy window on close
def on_window_close():
    print('Window Closed')
    root.destroy()

# Set up root
root = customtkinter.CTk()
root.title('Watermark Image')
root.geometry('800x600')
root.protocol('WM_DELETE_WINDOW',on_window_close)

# Global Watermark Image
selected_image = None
watermark_color = (100,100,100,128)

def choose_image_to_watermark():
    '''Lets user select image they wish to watermark and returns the watermarked image.'''
    image_path = filedialog.askopenfilename(title='Select Image to Watermark')
    if image_path == "":
        print('Dialog window was closed.')
    else:
        watermark_image(image_path)

def watermark_image(image_path,text=""):
    global selected_image,watermark_color

    # Open the chosen image
    image = Image.open(image_path)
    image_width,image_height = image.size
    
    
    print(image.size)
    # Creating a new image for text
    text_image = Image.new('RGBA',image.size,(255,255,255,0))
    
    # Create Text Watermark
    # wm_image = image.copy()
    
    draw_img = ImageDraw.Draw(text_image)
    
    # Define Text
    text = watermark_text.get()
    font = ImageFont.truetype('arial.ttf',80)
    
    # Get the size of the text
    text_bbox = draw_img.textbbox((0,0),text,font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    print(f'Text bbox {text_bbox}')
    # Calculate the position (centered)
    image_centerx = text_image.width//2
    image_centery = text_image.height//2
    text_x = image_centerx - (text_width // 2 )
    text_y = image_centery - (text_height // 2)
    print(f'Text x {text_x} Text y {text_y}')
    
    # Add the watermark to the image
    draw_img.text((text_x,text_y),text,fill=watermark_color,font=font)
    
    # Create a new image that can accomodate the rotated text
    max_dim = max(image_width,image_height) * 2
    large_canvas = Image.new('RGBA',(max_dim,max_dim),(255,255,255,0))
    large_canvas.paste(text_image,((max_dim-image_width)//2,(max_dim - image_height)//2))
    
    # Rotate Text Image
    rotation = slider.get()
    rotated_text = large_canvas.rotate(rotation,expand=1)
    
    
    # Final Adjustments
    final_text_image = Image.new('RGBA',image.size,(255,255,255,0))
    final_text_image.paste(rotated_text,((image_width - rotated_text.width)//2,(image_height - rotated_text.height)//2),rotated_text)
    print(final_text_image.size)
    
    # combine the two images
    combined = Image.alpha_composite(image.convert('RGBA'),final_text_image)
    display_image = combined.copy()
    app_width,app_height = 500,500
    display_image.thumbnail((app_width,app_height))
    
    selected_image = combined.copy()
    
    # Convert to TK Image
    tk_img = CTkImage(light_image=display_image,size=display_image.size)
    
    label.configure(image=tk_img)
    
    # Keeping a reference of the image
    label.image = tk_img
    
def choose_color():
    '''Open a color chooser dialog and update the selected color.'''
    global watermark_color
    color = askcolor(title='Choose Watermark Color')
    if color[1] is not None:
        # Combine selected color with the current opacity
        r,g,b= color[0]
        watermark_color = (int(r),int(g),int(b),watermark_color[3])
        print(f'Selected color is: {watermark_color}')

def update_opacity(value):
    '''Update the opacity of the watermark text'''
    global watermark_color
    # update the opacity value in the RGBA color
    watermark_color = (watermark_color[0],watermark_color[1],watermark_color[2],int(round(value,0)))


def save_image():
    '''Save the watermarked image.'''
    global selected_image
    if selected_image is not None:
        save_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files","*.png"),("All Files","*.*")])
        if save_path:
            selected_image.save(save_path)
            print(f'Image saved to {save_path}')

# Ini Frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=2,padx=2,fill='both',expand=True)
    
# Select Image button
button_select_image = customtkinter.CTkButton(master=frame,text='Select Image',command=choose_image_to_watermark)
button_select_image.pack(pady=8,padx=10)
button_select_image.place(x=2,y=250)

# Watermark Text Entry
watermark_text = customtkinter.CTkEntry(master=frame,placeholder_text='Watermark Text')
watermark_text.pack(pady=2,padx=10)
watermark_text.place(x=2,y=170)

# Font Size 
font_size = customtkinter.CTkEntry(master=frame,placeholder_text='Font Size')
font_size.pack(pady=2,padx=10)
font_size.place(x=2,y=130)

# Rotation Slider
var = tk.IntVar()
slider = CTkSlider(master=frame,from_=0,to=180,variable=var)
slider.place(x=2,y=100)
slider_rotation_label = CTkLabel(master=frame,text="Rotation: ")
slider_rotation_label.place(x=2,y=70)
slider_val = CTkLabel(master=frame,textvariable=var)
slider_val.place(x=60,y=70)

# Opacity Slider
o_var = tk.IntVar()
opacity_slider = CTkSlider(master=frame,from_=0,to=255,variable=o_var,command=update_opacity)
opacity_slider_label = CTkLabel(master=frame,text="Opacity: ")
opacity_slider_label.place(x=2,y=20)
# Opacity Val
opacity_slider_val = CTkLabel(master=frame,textvariable=o_var)
opacity_slider_val.place(x=50,y=20)
# Opacity Slider
opacity_slider.set(128) # Sets to default opacity
opacity_slider.pack(pady=8,padx=10)
opacity_slider.place(x=2,y=50)

# Color Picker Button
button_choose_color = customtkinter.CTkButton(master=frame,text='Choose Color',command=choose_color)
button_choose_color.pack(pady=8,padx=10)
button_choose_color.place(x=2,y=220)

# Save Image Button
button_save_image = CTkButton(master=frame,text='Save Image',command=save_image)
button_save_image.pack(pady=2,padx=2)
button_save_image.place(x=2,y=500)

# Frame for image
image_frame = customtkinter.CTkFrame(master=frame,width=300,height=300)
image_frame.pack(side='right',padx=10,pady=10)

# Display Image
label = customtkinter.CTkLabel(master=image_frame,text="")
label.pack()

# Start eventloop
root.mainloop()