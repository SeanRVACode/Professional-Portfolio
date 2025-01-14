import pygame.freetype
from ship import Ship
from enemies import Enemy
import pygame
from title_screen import StartScreen
from particles import ParticlePrinciple
from enemies_manager import EnemiesManager
from score_board import ScoreBoard
from game_over import GameOver


WIDTH = 720
HEIGHT = 1000
WHITE = (255,255,255)
FPS = 60
PARTICLE_EVENT = pygame.USEREVENT + 1


class Game:
    """ Main game class handling game states and loop."""
    def __init__(self):
        """ Initialize game components and state."""
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
        self.level = 1
        self.enemies_manager = EnemiesManager(WIDTH,HEIGHT,rows=self.level,cols=8)
        self.ship = Ship(315,850,10,HEIGHT,WIDTH,screen=self.screen)
        self.direction = 'right'
        self.particle_system = ParticlePrinciple(screen=self.screen)
        self.game_font = pygame.font.SysFont('TT Fellows',110)
        self.score_board = ScoreBoard()
        

        # self.clock.tick(60)
        self.main()
        
    def main(self):
        """ Main game loop handling events and state updates."""
        
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
                        # print(self.ship.rect.midbottom)
                        # Obtain position of midbottom of ship for editing
                        ship_x,ship_y = self.ship.rect.midbottom
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
                    elif self.game_state == "game_over":
                        if self.game_over_screen.handle_click(mouse_pos):
                            self.restart_game()
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
                self.handle_game_state()
            
            elif self.game_state == "victory":
                self.display_victory()
                
            elif self.game_state == "game_over":
                self.display_game_over()
                
            # flip the display to put your work on screen
            pygame.display.flip() # Updates the entire display at once
            
            self.clock.tick(FPS) # Limits the fps to FPS global variable
            
    

    def update_lasers(self):
        for laser in self.ship.lasers:
            collided_enemy = laser.update(self.screen,self.enemies_manager.enemies)
            if collided_enemy:
                # Handle collision feed back
                self.score_board.increase_score()
                print(f'Laser hit enemy at {collided_enemy.rect} beep')
        for laser in self.enemies_manager.lasers:
            collided_player = laser.update(self.screen,self.ship,type_='enemy')
            if collided_player:
                # Handle collision feed back
                self.ship.life -= 1
                print(f'Laser hit player at {collided_player}')
                
    
    def display_game_over(self): 
        """ Display the game over Screen."""
        


        self.game_state = "game_over"
        # self.screen.blit(text_surface,position)
        mouse_pos = pygame.mouse.get_pos()
        self.game_over_screen = GameOver(text="GAME OVER",font_size=50,screen=self.screen,screen_height=HEIGHT,screen_width=WIDTH,text_rgb=(255,255,255),bg_rgb=(0,0,0),button_text="Restart",score=self.score_board.score,high_score=self.score_board.high_score)

        self.game_over_screen.draw(mouse_pos)
        
        
    def display_victory(self):
        position = (200,500)
        self.screen.fill('black')
        text_surface = self.game_font.render('VICTORY',True,WHITE)
        self.screen.blit(text_surface,position)
    
    def restart_game(self):
        # Save the high score even though player died
        self.score_board.save_high_score()
        
        # Reset the game state to the start menu when pressed
        self.game_state = "start_menu"
        
        
        # Reset the score_board
        self.score_board.reset_score()
        
        
        def reset_ship(): # TODO Possibly implement into ship class
            self.ship.rect.topleft = (315,850)
            self.ship.life = 3
            self.ship.lasers.empty()
            
        def reset_enemies(): # TODO Possibly implement this into enemies manager
            self.enemies_manager.enemies.empty()
            self.level = 1
            self.enemies_manager.setup_enemies(self.level,8) # Manually providing rows as its a restart
            self.enemies_manager.lasers.empty() # Clear enemy lasers
            
        
            
        reset_ship()
        reset_enemies()
        
        
    def handle_game_state(self):
        self.score_board.draw_scoreboard(self.screen)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.ship.shoot(self.enemies_manager.enemies)
        
        self.particle_system.emit()
        self.ship.display_ship_life(self.screen)
        self.ship.move(keys)
        self.enemies_manager.move_enemies()
        self.update_lasers()
        self.enemies_manager.draw(self.screen)
        self.enemies_manager.shoot()
        
        
        
        if self.enemies_manager.detect_collisions(self.ship):
            self.score_board.save_high_score()
            self.display_game_over()
        elif self.ship.life <= 0:
            self.score_board.save_high_score()
            self.display_game_over()
        
        self.next_level()
    
    def next_level(self):
        # Check if all enemies are defeated
        if len(self.enemies_manager.enemies) == 0:
            if self.level == 5:
                self.victory()
            elif self.level < 5:
                # Increase the level
                self.level += 1
                # Check high score and update it
                self.score_board.save_high_score()
                self.score_board.read_high_score() # Read High Score to display new value
                self.score_board.high_score = self.score_board.read_high_score()
                # TODO Look into making enemy lasers fire faster in higher levels
                # Play around with increase the amount of rows and how fast they fire lasers.
                
                # Handle Enemy Set up for level increase
                self.enemies_manager.enemies.empty()
                self.enemies_manager.setup_enemies(self.level,8)
                self.enemies_manager.lasers.empty()
                
                # Handle Ship Reposition
                self.ship.rect.topleft = (315,850)
                self.ship.lasers.empty()
                
                # We do not reset ship life as they are not lost between levels. May increase them at later levels?
                
                
            
               
            
    def victory(self):
        # Check if all enemies are defeated
        if len(self.enemies_manager.enemies) == 0:
            # Check high score and update it
            self.score_board.save_high_score()
            # Set game state to vicotry. This will result in the victory screen being displayed.
            self.game_state = "victory"
            
        
    def game_over(self):
        # self.game_state = "game_over"
        print('Unused game over function used.')
        
        
            
        
           
                 
    
        
        
            
if __name__=='__main__': 
    Game()