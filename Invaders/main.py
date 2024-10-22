from ship import Ship
# from enemies import Enemy
import pygame

WIDTH = 720
HEIGHT = 1000

def main():
    pygame.init()
    pygame.display.set_caption('Invaderrrsss')
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    running = True
    clock = pygame.time.Clock()
    ship = Ship(315,850,10,HEIGHT,WIDTH)
    # enemy =
    enemies = []
    # End the game if the user presses 'X'
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Fill the screen
        screen.fill('black')
        
        # RENDER GAME HERE
        # screen.blit(ship.graphic,(ship.position*5,0))
        # Get Player Input
        keys = pygame.key.get_pressed()
        
        # Ship Movement
        if keys[pygame.K_LEFT]:
            ship.move(left=True)
        if keys[pygame.K_RIGHT]:
            ship.move(right=True)
        screen.blit(ship.graphic,(ship.pos))
        
        
        # flip the display to put your work on screen
        pygame.display.flip()
        
        clock.tick(60) # Limits the fps 60
        
if __name__=='__main__':
    main()