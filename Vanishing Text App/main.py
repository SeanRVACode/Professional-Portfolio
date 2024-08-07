import customtkinter as ctk
from customtkinter import CTkLabel,CTkEntry,CTkTextbox,StringVar,CTkButton
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
        self.root.geometry('600x400')
        self.root.protocol('WM_DELETE_WINDOW',self.on_window_close)
        # TODO need to set up grid system.
        # Grid System
        self.root.grid_columnconfigure(0,weight=1,minsize=100)
        self.root.grid_columnconfigure(1,weight=1,minsize=100)
        self.root.grid_columnconfigure(2,weight=1,minsize=100)
        self.root.grid_rowconfigure(0,weight=1,minsize=50)
        self.root.grid_rowconfigure(1,weight=1,minsize=50)
        
        # Create Frame
        self.text_entry_frame = TextEntryFrame(self.root,entry_width=300,entry_height=200)
        self.text_entry_frame.grid(row=0,column=1,padx=5,pady=5,sticky='new')
        
        # Create Button
        self.create_buttons()
        
                
    def on_window_close(self):
        '''Destroys Root'''
        print('Window Closed.')
        self.root.destroy()
        
    
    def create_buttons(self):
        # Start Button Creation
        start_button = CTkButton(self.root,text='Start',command=self.start_button)
        start_button.grid(row=1,column=1,padx=5,pady=5,sticky='w')
        # Reset Button Creation
        reset_button = CTkButton(self.root,text='Reset',command=self.reset_button)
        reset_button.grid(row=1,column=1,padx=5,pady=5,sticky='e')
        
        
    def start_button(self):
        '''Start button to start the application'''
        self.text_entry_frame.start_time()
    
    def reset_button(self):
        '''Resets the game.'''
        self.text_entry_frame.reset_game()
    
    


class TextEntryFrame(ctk.CTkFrame):
    def __init__(self,master=None,entry_width=200,entry_height=30,**kwargs):
        super().__init__(master,**kwargs)
        self.var = StringVar()
        self.entry_width = entry_width
        self.entry_height = entry_height
        self.time_to_erase = 5
        self.time_left = self.time_to_erase
        self.timer_started = False
        self.time_recorder = 0
        self.configure_grid()
        self.create_widgets()
        
        
    def configure_grid(self):
        '''Configure the grid system for the frame.'''
        self.grid_columnconfigure(0,weight=3,minsize=100)
        self.grid_columnconfigure(1,weight=3,minsize=100)
        self.grid_rowconfigure(0,weight=3,minsize=50)
        self.grid_rowconfigure(1,weight=3,minsize=50)
        
    
    def create_widgets(self):
        # Text box widget
        self.text_entry = CTkTextbox(self,font=('arial',20),width=self.entry_width,height=self.entry_height,state=ctk.DISABLED)
        self.text_entry.grid(row=0,column=0,padx=5,pady=5,sticky='new',columnspan=2)
        self.text_entry.bind("<Key>",self.reset_timer)
        
        # Countdown Widget
        self.time_keeper = CTkLabel(self,font=('arial',15),text='Time: 5')
        self.time_keeper.grid(row=1,column=0,padx=5,pady=5,sticky='sw')

        # Time passed widget
        self.time_record = CTkLabel(self,font=('arial',15),text='Time Typing: 0')
        self.time_record.grid(row=1,column=1,padx=5,pady=5,sticky='se')
    
    def reset_timer(self,event=None):
        '''Reset the timer when a key is pressed if the timer has started.'''
        if self.timer_started:
            self.time_left = self.time_to_erase
            self.update_timer_label()
    
    def track_time(self):
        if self.timer_started and self.time_left > 0:
            self.time_recorder += 1
            self.update_timer_label()
            self.after(1000,self.track_time)
        
        
        
    def start_time(self):
        self.start = time.time()
        self.timer_started = True
        self.text_entry.configure(state=ctk.NORMAL)
        self.text_entry.focus_set()
        self.check_timer()
        self.track_time()
    
    def check_timer(self):
        if self.timer_started and self.time_left > 0:
            self.time_left -= 1
            self.update_timer_label()
            self.after(1000,self.check_timer)
        elif self.time_left == 0:
            self.clear_text()
            self.text_entry.configure(state=ctk.DISABLED)
            self.timer_started = False
    
    def update_timer_label(self):
        '''Update the timer display.'''
        self.time_keeper.configure(text=f'Time: {self.time_left}')
        self.time_record.configure(text=f'Time Typing: {self.time_recorder}')
    
    def end_time(self):
        self.end = time.time()
        
    def calculate_time_passed(self):
        elapsed = self.end - self.start
        return elapsed
    
    def clear_text(self):
        '''Clear the text box.'''
        self.text_entry.delete("1.0",ctk.END)
        self.update_timer_label()
        
        
    def reset_game(self):
        self.timer_started = False
        self.time_to_erase = 5
        self.time_left = self.time_to_erase
        self.time_recorder = 0
        self.time_keeper.configure(text=f'Time: 5')
        self.time_record.configure(text=f'Time Typing: 0')
    
    
if __name__ == '__main__':
    root = ctk.CTk()
    app = VanishingApp(root)
    root.mainloop()
