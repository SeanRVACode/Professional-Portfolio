from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.mspeed = 1
        self.x_move = 10
        self.y_move = -10
        self.move_speed = 0.09
        
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        # self.move_speed *= .9
    
    def reset_position(self):
        self.goto(0,0)
        self.bounce_y()
        self.x_move = 10
        self.y_move = -10
        
        self.move_speed = .09