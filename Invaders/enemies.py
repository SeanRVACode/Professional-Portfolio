import pygame
import random
from laser import Laser


class Enemy(pygame.sprite.Sprite):
    def __init__(self,speed,height,width,ene_height,x,y):
        super().__init__()
        self.game_height = height
        self.game_width = width
        self.graphic = pygame.image.load('./Assets/enemy.png')
        self.graphic = pygame.transform.scale(self.graphic,(25,25))
        self.rect = self.graphic.get_rect(topleft=(x,y))
        # self.pos = self.rect.move(x,y)
        self.speed = speed
        

    def shoot(self):
        # TODO work on getting aliens to shoot randomly. Need to make sure it isn't shooting too fast.
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            laser = Laser(position=self.rect.midbottom,speed=10,type_='enemy')
            self.last_shot_time = current_time
            

    
  
        
        