import pygame
from enemies import Enemy

class EnemiesManager:
    def __init__(self,screen_width,screen_height,rows,cols):
        self.enemies = []
        self.direction = 'right'
        self.screen_width = screen_width
        self.scren_height = screen_height
        self.setup_enemies(rows,cols)
        
    def setup_enemies(self,rows,cols):
        xe = 30
        ye = 30
        for row in range(rows+1):
            for col in range(cols+1):
                ene = Enemy(1,self.scren_height,self.screen_width,10,xe,ye)
                self.enemies.append(ene)
                xe += 80
            xe = 30
            ye += 40
            
    def move_enemies(self):
        # Check if left most enemy hits the left boundary
        if self.enemies[0].pos.left <= 0 and self.direction == 'left':
            self.direction = 'right'
            for enemy in self.enemies:
                enemy.pos.y += 10
        elif self.enemies[-1].pos.right >= self.screen_width and self.direction == 'right':
            self.direction = 'left'
            for enemy in self.enemies:
                enemy.pos.y += 10
                
                
        # Move enemies based on direction
        for enemy in self.enemies:
            if self.direction == 'right':
                enemy.pos.x += enemy.speed
            elif self.direction == 'left':
                enemy.pos.x -= enemy.speed
                
                
    def draw(self,screen):
        for enemy in self.enemies:
            screen.blit(enemy.graphic,enemy.pos)
                