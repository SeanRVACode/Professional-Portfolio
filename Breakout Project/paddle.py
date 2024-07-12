from turtle import Turtle





class Paddle(Turtle):
    def __init___(self):
        super().__init__()
        self.shape('square')
        self.move_val = 25
            
        