import pygame


class Ship:
    def __init__(self,x,y,speed,height,width):
        self.game_height = height
        self.game_width = width
        self.graphic = pygame.image.load('./Assets/128px-Space-Invaders-ship.png').convert()
        # self.pos = (x,y) # Starting position of the ship
        self.pos = self.graphic.get_rect().move(x,y) # TODO ask for a better explanation of this
        self.speed = speed
        # self.life # TODO Add Life count?
        
        
    def move(self,left=False,right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if self.pos.right > self.game_width:
            self.pos.left = 600
        if self.pos.left < 0:
            self.pos.left = 0