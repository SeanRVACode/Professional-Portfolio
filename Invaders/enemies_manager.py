import pygame
from enemies import Enemy

class EnemiesManager:
    def __init__(self,screen_width,screen_height,rows,cols):
        self.enemies = pygame.sprite.Group()
        self.direction = 'right'
        self.screen_width = screen_width
        self.scren_height = screen_height
        self.setup_enemies(rows,cols)
        self.drop_speed = 5
        
    def setup_enemies(self,rows,cols):
        xe = 30
        ye = 30
        for row in range(rows+1):
            for col in range(cols+1):
                ene = Enemy(1,self.scren_height,self.screen_width,10,xe,ye)
                self.enemies.add(ene)
                xe += 80
            xe = 30
            ye += 40
            
    def move_enemies(self):
        # Check if enemies have reached the edge of the screen
        change_direction = False
        for enemy in self.enemies:
            if (enemy.rect.left <= 0 and self.direction == 'left') or \
                (enemy.rect.right >= self.screen_width and self.direction == 'right'):
                    change_direction = True
                    break
        
        # If boundry is hit, change direction and move enemies down
        if change_direction:
            self.direction = 'left' if self.direction == 'right' else 'right'
            for enemy in self.enemies:
                enemy.rect.y += self.drop_speed # Move down by 10 pixels
                
                
        # Move enemies horizontally based on the current direction
        for enemy in self.enemies:
            if self.direction == 'right':
                enemy.rect.x += enemy.speed
            elif self.direction == 'left':
                enemy.rect.x -= enemy.speed
                
                
    def draw(self,screen):
        for enemy in self.enemies:
            screen.blit(enemy.graphic,enemy.rect)
                