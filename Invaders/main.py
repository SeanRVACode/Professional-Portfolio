import pygame.freetype
from ship import Ship
from enemies import Enemy
import pygame
from title_screen import StartScreen
from particles import ParticlePrinciple
from enemies_manager import EnemiesManager


WIDTH = 720
HEIGHT = 1000
WHITE = (255,255,255)
PARTICLE_EVENT = pygame.USEREVENT + 1


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Invaderrrsss')
        icon = pygame.image.load('./Assets/enemy.png')
        pygame.display.set_icon(icon)
        pygame.time.set_timer(PARTICLE_EVENT,50)
        
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        # self.mouse_pos = pygame.mouse.get_pos()
        self.game_state = "start_menu"
        self.running = True
        self.clock = pygame.time.Clock()
        self.enemies_manager = EnemiesManager(WIDTH,HEIGHT,rows=5,cols=8)
        self.ship = Ship(315,850,10,HEIGHT,WIDTH,screen=self.screen)
        self.direction = 'right'
        self.particle_system = ParticlePrinciple(screen=self.screen)
        self.game_font = pygame.font.SysFont('TT Fellows',110)

        # self.clock.tick(60)
        self.main()
        
    def main(self):

        
        # End the game if the user presses 'X'
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == PARTICLE_EVENT:
                    if self.game_state == "start_menu":
                        # Particle Stuff
                        self.particle_system.add_emitter("mouse",pygame.mouse.get_pos(),color=(255,255,255))
                        self.particle_system.add_particles("mouse")
                    elif self.game_state == "game":
                        # Debug to know midbottom of ship
                        # print(self.ship.pos.midbottom)
                        # Obtain position of midbottom of ship for editing
                        ship_x,ship_y = self.ship.pos.midbottom
                        self.particle_system.add_emitter("ship",(ship_x+5,ship_y-12),direction=(0,2),color=(255,165,0),spread=4)
                        self.particle_system.add_particles("ship")
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.game_state == "start_menu":
                        # Check if "Start" Button is clicked
                        if start_screen.handle_click(mouse_pos):
                            print("Start Button Clicked")
                            # Set the game state to game
                            self.game_state = "game"
            # Fill the screen
            self.screen.fill('black')

            

                    
            
            # RENDER GAME HERE

            # Game States Determination
            if self.game_state == "start_menu":
                
                mouse_pos = pygame.mouse.get_pos()
                start_screen = StartScreen(text="Invaders",font_size=50,screen=self.screen,screen_height=HEIGHT,screen_width=WIDTH,text_rgb=(255,255,255),bg_rgb=(0,0,0))
                start_screen.draw(mouse_pos=mouse_pos)
                self.particle_system.emit() # Emits Particles from mouse.
                
            # Actual State of playing the game
            elif self.game_state == "game":
                # Get the keys pressed
                keys = pygame.key.get_pressed()
                
                
                # Shoot Laser
                if keys[pygame.K_SPACE]:
                    self.ship.shoot(self.enemies_manager.enemies)
                
                # Ship Functions
                self.particle_system.emit()
                self.ship.move(keys)
                self.enemies_manager.move_enemies()
                self.update_lasers()
                self.enemies_manager.draw(self.screen)
                
                # Place enemies on screen
                for enemy in self.enemies_manager.enemies:
                    self.screen.blit(enemy.graphic,enemy.pos)
                    # Detect Collision
                    self.game_over(collision=self.ship.detect_collide(enemy.pos)) # TODO figure a way to either clear out enemies or reset the game to a game over screen

                
                
                
                
            elif self.game_state == "game_over":
                # TODO Finish writing and setting up game over state
                pass
                
            # flip the display to put your work on screen
            pygame.display.flip() # Updates the entire display at once
            
            self.clock.tick(60) # Limits the fps 60

    def update_lasers(self):
        self.ship.lasers.update(self.screen,self.enemies_manager.enemies)
    
    def game_over(self,collision):
        position = (130,500)
        transparent = (0,0,0,0)
        if collision:
            text_surface = self.game_font.render('GAME OVER',True,WHITE)
            self.screen.fill('black')
            self.ship.graphic.fill(transparent)
            self.screen.blit(text_surface,position)

        pass

        
            
        
           
                 
    
        
        
            
if __name__=='__main__': 
    Game()