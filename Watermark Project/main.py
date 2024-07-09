import customtkinter
from customtkinter import filedialog,CTkLabel
from PIL import Image,ImageFont,ImageDraw
import os,sys
from ctypes import windll
import matplotlib.pyplot as plt


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
root.geometry('500x350')
root.protocol('WM_DELETE_WINDOW',on_window_close)

def choose_image_to_watermark():
    '''Lets user select image they wish to watermark and returns the watermarked image.'''
    image_path = filedialog.askopenfilename(title='Select Image to Watermark')
    if image_path == "":
        print('Dialog window was closed.')
    else:
        watermark_image(image_path)

def watermark_image(image_path):
    size = (75,75)
    transparancy = 65

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
    text = "Sean P"
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
    draw_img.text((text_x,text_y),text,fill=(100,100,100,128),font=font)
    
    # Create a new image that can accomodate the rotated text
    max_dim = max(image_width,image_height) * 2
    large_canvas = Image.new('RGBA',(max_dim,max_dim),(255,255,255,0))
    large_canvas.paste(text_image,((max_dim-image_width)//2,(max_dim - image_height)//2))
    
    # Rotate Text Image
    rotated_text = large_canvas.rotate(60,expand=1)
    
    
    # Final Adjustments
    final_text_image = Image.new('RGBA',image.size,(255,255,255,0))
    final_text_image.paste(rotated_text,((image_width - rotated_text.width)//2,(image_height - rotated_text.height)//2),rotated_text)
    print(final_text_image.size)
    
    # combine the two images
    combined = Image.alpha_composite(image.convert('RGBA'),final_text_image)
    
    return combined
    
    
    # wm_image.show()
    



# Ini Frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=2,padx=2,fill='both',expand=True)
    
# Select Image button
button_select_image = customtkinter.CTkButton(master=frame,text='Select Image',command=choose_image_to_watermark)
button_select_image.pack(pady=8,padx=10)
button_select_image.place(x=2,y=110)

    
# Start eventloop
root.mainloop()