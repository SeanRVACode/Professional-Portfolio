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
        self.lasers = pygame.sprite.Group() # Group lasers into sprite group
        self.shoot_cooldown = 300 # In miliseconds
        self.last_shot_time = pygame.time.get_ticks() # Time when the last shot
        self.life = 3
        
         
        # TODO Add Life count? Does the life even need to be held by the ship? I guess it would as we detect collision on the ship as well.
        
        
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
        # Collision between ship and other_rect. This will return true or false which will either be used to reduce ship life or end the game.
        collision = self.pos.colliderect(other_rect)
        if collision:
            print('Collision Detected.')
            if other_rect.name == 'laser':
                # Lower life by one if hit by laser
                self.life -= 1
        return collision

    def shoot(self,other_rect):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            laser = Laser(position=self.pos.midtop,speed=-10)
            self.lasers.add(laser) # Add laser to the sprite group
            self.last_shot_time = current_time
    
    def update_lasers(self,screen,enemies):
        self.lasers.update() # Automatically calls 'update()' on each laser in the sprite group
        for laser in self.lasers:
            if laser.rect.bottom < 0:  # Remove off screen lasers
                self.lasers.remove(laser)
            else:
                screen.blit(laser.image,laser.rect)
    
    def display_ship_life(self,screen):
        # TODO look into changing this into hearts
        # Display the life of the ship
        
        position = (10,950)
        self.setup_hearts(screen,position=position)

    def setup_hearts(self,screen,position):
        heart = pygame.transform.scale(pygame.image.load('./Assets/heart-pixelate-png.png').convert_alpha(),(20,20))
        rect = heart.get_rect(topleft=position)
        # Setup the hearts for the ship
        for col in range(self.life):
            screen.blit(heart,rect)
            rect.x += 40
            
            
            
  
    def ship_thruster(self):
        
        # Emit Particles from ship
        
        pass