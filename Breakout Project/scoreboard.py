from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-230,-330)
        # self.write(f'Score: {self.score}',align='Center',font=('Courier',20,'bold'))
        self.keep_score()
    
    def increase_score(self):
        self.score += 1
        self.keep_score()
    
    def keep_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align='Center',font=('Courier',20,'bold'))