import pygame


class Laser:
    def __init__(self,position,speed):
        self.position = position
        self.speed = speed
        self.lasers = []
        self.laser_image = pygame.Surface((5,10))
        self.laser_image.fill((255,0,0)) # Red Laser
        self.rectangle = self.laser_image.get_rect(center=self.position)
    
    def move(self):
        self.rectangle.y += self.speed # TODO Write a better description for this
    
    def detect_collision(self,other_rect):
        collision = self.rectangle.colliderect(other_rect)
        print(f'Laser collision {collision}')
        return collision
    
    def update(self,screen,enemies):
        self.move()
        screen.blit(self.laser_image,self.rectangle)
        if self.rectangle.bottom < 0:
            return False # Indicates the laser should be removed
        for enemy in enemies:
            if self.detect_collision(enemy.pos):
                enemies.remove(enemy)
                return False # Indicates the laser should be removed
        return True # Indicates the laser should remain