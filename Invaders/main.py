import pygame.freetype
from ship import Ship
from enemies import Enemy
import pygame
from title_screen import StartScreen
from particles import ParticlePrinciple


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
        self.enemies = []
        self.ship = Ship(315,850,10,HEIGHT,WIDTH,screen=self.screen)
        self.direction = 'right'
        self.particle_system = ParticlePrinciple(screen=self.screen)
        self.game_font = pygame.font.SysFont('TT Fellows',110)

        # self.clock.tick(60)
        self.main()
        
    def main(self):

        # Create Enemies
        self.enemies_setup(rows=5,cols=8)
        

    
        
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
                    self.ship.shoot(self.enemies)
                
                # Ship Functions
                self.particle_system.emit()
                self.ship.move(keys)
                
                # Enemy Movement
                self.enemy_movement(self.enemies)
                self.update_lasers()
                
                # Place enemies on screen
                for enemy in self.enemies:
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
        for laser in self.ship.lasers:
            if not laser.update(self.screen,self.enemies):
                self.ship.lasers.remove(laser)
    
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
    
    def enemy_movement(self,enemies):
        # TODO Look into moving this to enemies class
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