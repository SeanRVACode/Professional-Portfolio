import tkinter as tk
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from brick import Brick
from scoreboard import Scoreboard


# Set up screen borders
SCREEN_WIDTH = 660
SCREEN_HEIGHT = 800
SPEED_INCREMENT = .01

# STARTING_POSITION = (0,-250)

class Breakout:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor ('black')
        self.screen.title('Breakout')
        # self.screen.listen()
        self.screen.tracer(0)
        self.screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
        self.ball = Ball()
        # self.draw_border()
        
        self.paddle = Paddle()
        self.set_up_bricks()
        
        # Paddle Moving
        self.moving_left = False
        self.moving_right = False
        
        # Set up button presses
        self.screen.listen()
        self.screen.onkeypress(self.start_move_left,"Left")
        self.screen.onkeypress(self.start_move_right,"Right")
        self.screen.onkeyrelease(self.stop_move,"Left")
        self.screen.onkeyrelease(self.stop_move,"Right")
        # Reset the game
        self.screen.onkey(self.restart_game,"r")
        
        # Ini scoreboard
        self.scoreboard = Scoreboard()
        
        self.game_on = True
        self.move_paddle()
        while self.game_on:
            self.screen.update()
            time.sleep(self.ball.move_speed)
            self.ball.move()
            
            # Detect Collision with wall
            if self.ball.xcor() < -300 or self.ball.xcor() > 300:
                self.ball.bounce_x()
                
            # Detect Collision with paddle
            if self.ball.distance(self.paddle) < 50 and self.ball.ycor() < -220:
                self.ball.bounce_y()
            
            # Detect collision with brick
            for brick in self.bricks:
                if self.ball.distance(brick) < 30:
                    self.ball.bounce_y()
                    # self.ball.move_speed *= .1
                    self.increase_ball_speed(0.03)
                    self.scoreboard.increase_score()
                    brick.hideturtle()
                    self.bricks.remove(brick)
                    
                    
                
            # Detecting hitting top wall
            if self.ball.ycor() > SCREEN_HEIGHT /2  or self.ball.ycor() < -SCREEN_HEIGHT/2:
                self.game_over()
                # self.ball.reset_position()
                
                
                
        self.screen.exitonclick()
    
    # Paddle Adjustments
    def move_paddle(self):
        if self.moving_left:
            self.paddle.move_left()
        if self.moving_right:
            self.paddle.move_right()
        self.screen.ontimer(self.move_paddle,10)
        
    def start_move_left(self):
        # print('Moving left')
        self.moving_left = True
        
    def start_move_right(self):
        # print('Moving right')
        self.moving_right = True
    
    def stop_move(self):
        self.moving_left = False
        self.moving_right = False
    
    def game_over(self):
        self.game_on = False
        self.game_over_turtle = Turtle()
        self.game_over_turtle.hideturtle()
        self.game_over_turtle.color('white')
        self.game_over_turtle.penup()
        self.game_over_turtle.goto(0,0)
        self.game_over_turtle.write('GAME OVER',align='center',font=('Courier',80,'normal'))
        self.game_over_turtle.goto(0,-200)
        self.game_over_turtle.write('Press R To Restart',align='center',font=('Courier',30,'normal'))
        
    
    def draw_border(self):
        border_turtle = Turtle()
        border_turtle.color('white')
        border_turtle.penup()
        border_turtle.goto(-SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        border_turtle.pendown()
        border_turtle.pensize(3)
        
        for _ in range(2):
            border_turtle.forward(SCREEN_WIDTH)
            border_turtle.right(90)
            border_turtle.forward(SCREEN_HEIGHT)
            border_turtle.right(90)
    
    def set_up_bricks(self):
        brick_x_axis = -305
        brick_y_axis = 380
        self.bricks = []
        brick_colors = [
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "indigo",
            "violet",
            "pink",
            "cyan",
            "lime",
            "magenta",
            "brown",
            "purple",
            "lightblue",
            "lightgreen"
        ]
        for row in range(7):
            for col in range (13):
                brick = Brick((brick_x_axis,brick_y_axis),color=brick_colors[row])
                self.bricks.append(brick)
                brick_x_axis += 50
            brick_x_axis = -305
            brick_y_axis -= 20
            
    def increase_ball_speed(self,increment):
        self.ball.move_speed *= (1 - increment)
        
    def restart_game(self):
        self.game_over_turtle.clear()
        self.screen.clearscreen()
        self.__init__()
        
        
        
        
        
Breakout()