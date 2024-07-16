from turtle import Turtle



# STARTING_POSITION = (330,50)

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=4,stretch_len=1)
        self.penup()
        self.right(90)
        self.goto(0,-250)
        
    def move_left(self):
        
        new_x = self.xcor() - 20
        if new_x > -300:
            self.goto(new_x,self.ycor())
    
    def move_right(self):
        new_x = self.xcor() + 20
        if new_x < 300:
            self.goto(new_x,self.ycor())
    
    def reset_position(self):
        self.goto(0,-250)