from turtle import Turtle

class Brick(Turtle):
    def __init__(self,position,color):
        super().__init__()
        self.shape('square')
        self.color(color) # TODO need to have these different color bricks
        self.shapesize(stretch_wid=.5,stretch_len=2)
        self.penup()
        # self.right(90)
        self.goto(position)