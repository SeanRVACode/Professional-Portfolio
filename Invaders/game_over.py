import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect


class GameOver:
    def __init__(self,text,font_size,text_rgb,bg_rgb,screen,screen_width,screen_height,score,high_score,button_text="Restart"):
        """Creates the game over screen. It also has the restart option."""
        # TODO Finish setting up Game Over Screen
        
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.SysFont("Courier",font_size,bold=True)
        self.text_rgb = text_rgb
        self.bg_rgb = bg_rgb
        self.text = text

        
        
        # Define Restart button
        self.restart_button_font = pygame.font.SysFont("Courier",font_size,bold=True)
        self.restart_button_hover = pygame.font.SysFont("Courier",font_size + 10,bold=True)
        self.restart_button_text = button_text
        self.restart_button_color = text_rgb # Same as game over text color
        
        # Define parts of title
        self.title_font - pygame.font.SysFont("Courier",font_size + 20,bold=True)
        
        # Render Restart Button Once to calculate its size
        restart_button_surface = self.restart_button_font.render(self.restart_button_text,True,self.restart_button_color)
        # Get the top left corner of the button
        restart_button_x = screen_width // 2 - restart_button_surface.get_width() // 2
        restart_button_y = screen_height // 2 + restart_button_surface.get_height() // 2
        # Create Rectange for restart button
        self.restart_button_rect = Rect(restart_button_x,restart_button_y,restart_button_surface.get_width(),restart_button_surface.get_height())
        
        
    def draw(self,mouse_pos):
        """Draws the game over screen with hover effects based on mouse position."""
        
        # Fill the Screen
        self.screen.fill(self.bg_rgb)
        
        # Draw the Title
        title_surface = self.title_font.render(self.text,True,self.text_rgb)
        # Calculate the x position in the center of the screen
        title_x = self.screen_width //2 - title_surface.get_width() // 2
        
        # screen_width // 2 calculates the horizontal center of the screen by diving the screen width by 2 and then subtracting half the width of the title (title_surface.get_width() // 2 determines half the width)
        
        title_y = self.screen_height // 2 - title_surface.get_height() // 2 - 100
        
        # We need the -100 on this to move the title higher up on the screen so we can make room for the restart button below it.
        
        # Check if the mouse is hovering over the restart button 
        is_hovered = self.restart_button_rect and self.restart_button_rect.collidepoint(mouse_pos)
        # Button font determined by if statement
        button_font = self.restart_button_hover_font if is_hovered else self.restart_button_font
        
        # Render the restart button
        restart_button_surface = button_font.render(self.restart_button_text,True,self.restart_button_color)
        restart_button_x = self.screen_width // 2 - restart_button_surface.get_width() // 2
        restart_button_y = self.screen_height // 2 + restart_button_surface.get_height() // 2
        # Create Restart Button rectangle
        self.restart_button_rect = Rect(restart_button_x,restart_button_y,restart_button_surface.get_width(),restart_button_surface.get_height())
        # Blit the restart button to the screen
        self.screen.blit(restart_button_surface,(restart_button_x,restart_button_y))
        
        # Update the pygame display
        pygame.display.update()
        
    def handle_click(self,mouse_pos):
        # Check if the mouse click is inside the "Restart" button's rectangle
        
        if self.restart_button_rect and self.restart_button_rect.collidepoint(mouse_pos):
            return True
        return False       
        
        
        
    

