import pygame


class Ship:
    def __init__(self,x,y,speed,height,width):
        self.game_height = height
        self.game_width = width
        self.graphic = pygame.transform.scale(pygame.image.load('./Assets/128px-Space-Invaders-ship.png').convert(),(100,100))
        # self.pos = (x,y) # Starting position of the ship
        self.pos = self.graphic.get_rect().move(x,y) # TODO ask for a better explanation of this
        self.speed = speed
        # TODO Ship Particles?
        
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
    
    def detect_collide(self,other_rect):
        collision = self.pos.colliderect(other_rect)
        if collision:
            print('Collision Detected.')
        return collision