from ship import Ship
from enemies import Enemy
import pygame

WIDTH = 720
HEIGHT = 1000

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
        self.main()
        
    def main(self):

        # ship = Ship(315,850,10,HEIGHT,WIDTH)

        

        # # Create Enemies
        self.enemies_setup(rows=4,cols=8)
        
        # End the game if the user presses 'X'
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # Fill the screen
            self.screen.fill('black')

            for enemy in self.enemies:
                self.screen.blit(enemy.graphic,enemy.pos)
            
            # RENDER GAME HERE

            # Get Player Input
            keys = pygame.key.get_pressed()
            

            self.ship_movement(keys)
            
            # flip the display to put your work on screen
            pygame.display.flip()
            
            self.clock.tick(60) # Limits the fps 60
    def enemies_setup(self,rows,cols):
        xe = 30
        ye = 30
        for row in range(rows+1):
            for col in range(cols+1):
                ene = Enemy(5,HEIGHT,WIDTH,10,xe,ye)
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
            
if __name__=='__main__':
    Game()