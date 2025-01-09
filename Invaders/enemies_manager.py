import pygame
from enemies import Enemy
import random
from laser import Laser

class EnemiesManager:
    def __init__(self,screen_width,screen_height,rows,cols):
        self.enemies = pygame.sprite.Group()
        self.direction = 'right'
        self.screen_width = screen_width
        self.scren_height = screen_height
        self.setup_enemies(rows,cols)
        self.drop_speed = 5
        self.lasers = pygame.sprite.Group()
        self.last_shot_time = pygame.time.get_ticks()
        self.shoot_cooldown = 1000
        
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
    
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            chosen_enemy = self.laser_select()
            laser = Laser(position=chosen_enemy.rect.midbottom,speed=10,type_='enemy')
            self.lasers.add(laser)
            self.last_shot_time = current_time
            
            
                
    def draw(self,screen):
        for enemy in self.enemies:
            screen.blit(enemy.graphic,enemy.rect)
                
    def detect_collisions(self,ship):
        for enemy in self.enemies:
            if ship.detect_collide(enemy.rect):
                self.enemies.remove(enemy)
                return True
        return False
    
    def laser_select(self):
        # Randomly select an enemy to shoot laser
        chosen_enemy = random.choice(self.enemies.sprites())
        return chosen_enemy
    