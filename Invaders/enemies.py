import pygame
import random


class Enemy:
    def __init__(self,speed,height,width,ene_height,x,y):
        self.game_height = height
        self.game_width = width
        self.graphic = pygame.image.load('./Assets/enemy.png')
        self.graphic = pygame.transform.scale(self.graphic,(25,25))
        self.pos = self.graphic.get_rect().move(x,y)
        self.speed = speed

    def move(self,direction):
        pass
    
  
        
        