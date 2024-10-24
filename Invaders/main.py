import pygame.freetype
from ship import Ship
from enemies import Enemy
import pygame

WIDTH = 720
HEIGHT = 1000
WHITE = (255,255,255)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Invaderrrsss')
        icon = pygame.image.load('./Assets/enemy.png')
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()
        self.enemies = []
        self.ship = Ship(315,850,10,HEIGHT,WIDTH)
        self.direction = 'right'
        self.game_font = pygame.font.SysFont('TT Fellows',110)
        # self.clock.tick(60)
        self.main()
        
    def main(self):

        # ship = Ship(315,850,10,HEIGHT,WIDTH)

        

        # Create Enemies
        self.enemies_setup(rows=5,cols=8)
        
        
        
        # End the game if the user presses 'X'
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # Fill the screen
            self.screen.fill('black')

            # Place enemies on screen
            for enemy in self.enemies:
                self.screen.blit(enemy.graphic,enemy.pos)
                # Detect Collision
                self.game_over(collision=self.ship.detect_collide(enemy.pos))

                    
            
            # RENDER GAME HERE

            # Get Player Input
            keys = pygame.key.get_pressed()
            self.ship_movement(keys)
            
            
            
            
            # Enemy Movement
            self.enemy_movement(self.enemies)
            
            # flip the display to put your work on screen
            pygame.display.flip()
            
            self.clock.tick(60) # Limits the fps 60
            
    def game_over(self,collision):
        position = (130,500)
        transparent = (0,0,0,0)
        if collision:
            text_surface = self.game_font.render('GAME OVER',True,WHITE)
            self.screen.fill('black')
            self.ship.graphic.fill(transparent)
            self.screen.blit(text_surface,position)
            # self.clock.tick(None)
            # self.running = False
        pass
    def enemies_setup(self,rows,cols):
        xe = 30
        ye = 30
        for row in range(rows+1):
            for col in range(cols+1):
                ene = Enemy(1,HEIGHT,WIDTH,10,xe,ye)
                self.enemies.append(ene)
                xe += 80
            xe = 30
            ye += 40
        
    def ship_movement(self,keys):
        # Ship Movement
        if keys[pygame.K_LEFT]:
            self.ship.move(left=True)
        if keys[pygame.K_RIGHT]:
            self.ship.move(right=True)
        self.screen.blit(self.ship.graphic,(self.ship.pos))
    
    def enemy_movement(self,enemies):
        # Check if left most enemy hits the left boundary
        if enemies[0].pos.left <= 0 and self.direction == 'left':
            self.direction = 'right' # Change the direction to right
            for alien in enemies:
                alien.pos.y += 10 # Move alien down
        # Check if last enemy (right most enemy) hits the right boundry
        elif enemies[-1].pos.right >= WIDTH and self.direction == 'right':
            self.direction = 'left' # Change direction to left
            for alien in enemies:
                alien.pos.y += 10 # Move alien down
        
        # Move alients left to right
        for alien in enemies:
            if self.direction == 'right':
                alien.pos.x += alien.speed # Move alien to the right at set speed
            elif self.direction == 'left':
                alien.pos.x -= alien.speed # Move alien to the left at set speed
        
            
        
           
                 
    
        
        
            
if __name__=='__main__':
    Game()