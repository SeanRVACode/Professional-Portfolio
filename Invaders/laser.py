import pygame


class Laser(pygame.sprite.Sprite):
    laser_image = None
    def __init__(self,position,speed,type_='player'):
        super().__init__()
        if not Laser.laser_image: # Initialize the laser image once
            Laser.laser_image = pygame.Surface((5,10))
            Laser.laser_image.fill((255,0,0))  # Red Laser
        
        self.type = type_
        self.image = Laser.laser_image
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
    
    def move(self):
        self.rect.y += self.speed # TODO Write a better description for this
    
    def detect_collision(self,other_rect):
        collision = self.rect.colliderect(other_rect)
        print(f'Laser collision {collision}')
        return collision
    
    def update(self,screen,enemies,type_='player'):
        self.move() # Moves the laser
        screen.blit(self.image,self.rect)
        
        # Remove the laser if it goes off-screen
        if self.rect.bottom < 0:
            self.kill()
            return None
        
        # Check for collision with enemies
        if type_ == 'player':
            collided_enemy = pygame.sprite.spritecollideany(self,enemies)
            if collided_enemy:
                print('Collision with enemy')
                collided_enemy.kill()
                self.kill()
                return collided_enemy # Return the collided enemy
        elif type_ == 'enemy':
            collided_player = pygame.sprite.spritecollideany(self,[enemies])
            if collided_player:
                print('Collision with player')
                self.kill()
                return collided_player
        return None