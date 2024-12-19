import pygame
from particles import ParticlePrinciple
from laser import Laser

class Ship:
    def __init__(self,x,y,speed,height,width,screen,particles = None,keys=None):
        self.game_height = height
        self.game_width = width
        self.keys = keys
        self.screen = screen
        self.graphic = pygame.transform.scale(pygame.image.load('./Assets/128px-Space-Invaders-ship.png').convert_alpha(),(90,90)) # Convert alpha is loading the transparent image of the file
        # self.pos = (x,y) # Starting position of the ship
        self.pos = self.graphic.get_rect().move(x,y) # TODO ask for a better explanation of this
        self.speed = speed
        self.lasers = []
        self.shoot_cooldown = 500 # In miliseconds
        self.last_shot_time = pygame.time.get_ticks() # Time when the last shot
        
         
        # self.life # TODO Add Life count? Does the life even need to be held by the ship? I guess it would as we detect collision on the ship as well.
        
        
    def move(self,keys):
        if keys[pygame.K_LEFT]:
            self.pos.right -= self.speed
        if keys[pygame.K_RIGHT]:
            self.pos.right += self.speed
        # Boundry Check
        if self.pos.right > self.game_width:
            self.pos.left = 600
        if self.pos.left < 0:
            self.pos.left = 0
        self.screen.blit(self.graphic,(self.pos))
        
    
    def detect_collide(self,other_rect):
        collision = self.pos.colliderect(other_rect)
        if collision:
            print('Collision Detected.')
        return collision

    def shoot(self,other_rect):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            laser = Laser(position=self.pos.midtop,speed=-10)
            self.lasers.append(laser)
            self.last_shot_time = current_time
                
    
    def ship_thruster(self):
        
        # Emit Particles from ship
        
        pass