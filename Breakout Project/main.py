import tkinter as tk
from turtle import Screen,Turtle



# Set up screen borders
SCREEN_WIDTH = 660
SCREEN_HEIGHT = 800
TOP_BORDER = 300



class Breakout:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor ('black')
        self.screen.title('Breakout')
        self.screen.listen()
        self.screen.tracer(0)
        self.screen.setup()