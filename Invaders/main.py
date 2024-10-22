from ship import Ship
# from enemies import Enemy
import pygame



def main():
    pygame.init()
    screen = pygame.display.set_mode((720,1000))
    running = True
    clock = pygame.time.Clock()
    ship = Ship()
    # End the game if the user presses 'X'
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Fill the screen
        screen.fill('black')
        
        # RENDER GAME HERE
        screen.blit(ship.graphic,(ship.position*5,0))
        
        
        # flip the display to put your work on screen
        pygame.display.flip()
        
        clock.tick(60) # Limits the fps 60
        
if __name__=='__main__':
    main()