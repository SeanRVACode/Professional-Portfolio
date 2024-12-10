import pygame
from particles import ParticlePrinciple


class Ship:
    def __init__(self,x,y,speed,height,width,particles = None):
        self.game_height = height
        self.game_width = width
        self.graphic = pygame.transform.scale(pygame.image.load('./Assets/128px-Space-Invaders-ship.png').convert_alpha(),(100,100))
        # self.pos = (x,y) # Starting position of the ship
        self.pos = self.graphic.get_rect().move(x,y) # TODO ask for a better explanation of this
        self.speed = speed
        
        # self.life # TODO Add Life count? Does the life even need to be held by the ship? I guess it would as we detect collision on the ship as well.
        
        
    def move(self,left=False,right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if self.pos.right > self.game_width:
            self.pos.left = 600
        if self.pos.left < 0:
            self.pos.left = 0
    
    def detect_collide(self,other_rect):
        collision = self.pos.colliderect(other_rect)
        if collision:
            print('Collision Detected.')
        return collision
    
    def ship_thruster(self):
        
        # Emit Particles from ship
        
        pass