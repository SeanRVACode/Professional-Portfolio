import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

class StartScreen:
    def __init__(self,text,font_size,text_rgb,bg_rgb,screen,screen_width,screen_height):
        # TODO Add Hover Effects
        """Creates the start screen with text written on it."""
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.SysFont("Courier",font_size,bold=True)
        self.text_rgb = text_rgb
        self.bg_rgb = bg_rgb
        self.text = text
        # screen.fill((0,0,0))
        # font = pygame.font.SysFont("Courier",font_size,bold=True)
        # title = font.render(text,True,(255,255,255))
        
        
        # Define Start Button
        self.start_button_font = pygame.font.SysFont("Courier",font_size,bold=True)
        self.start_button_hover_font = pygame.font.SysFont("Courier",font_size + 10,bold=True)
        self.start_button_text = "Start"
        self.start_button_color = text_rgb
        
        # Define Parts of Title
        self.title_font = pygame.font.SysFont("Courier",font_size + 20, bold=True)
        
        # Render Start Button Once to calculate its size
        start_button_surface = self.start_button_font.render(self.start_button_text,True,self.start_button_color)
        start_button_x = screen_width // 2 - start_button_surface.get_width() // 2
        start_button_y = screen_height // 2 + start_button_surface.get_height() // 2
        self.start_button_rect = Rect(start_button_x,start_button_y,start_button_surface.get_width(),start_button_surface.get_height())
        # TODO Feed mouse postion into here so that I can determine when to make buttons larger
        
    def draw(self,mouse_pos):
        # TODO Maybe should have mouse effects be handled in its own class.
        """Draws the start screen with hover effects based on mouse position."""
        
        # Fill the Screen
        self.screen.fill(self.bg_rgb)
        
        # Draw the Title
        title_surface = self.title_font.render(self.text,True,self.text_rgb) # We put title_font here to then render the text contained within self.text
        title_x = self.screen_width // 2 - title_surface.get_width() // 2
        title_y = self.screen_height // 2 - title_surface.get_height() // 2 - 100
        self.screen.blit(title_surface,(title_x,title_y)) # Blit draws to screen
        
        
        # Check if mouse is hovering over the "Start" Button
        is_hovered = self.start_button_rect and self.start_button_rect.collidepoint(mouse_pos)
        # print(f'Is Hovered? {is_hovered}')
        button_font = self.start_button_hover_font if is_hovered else self.start_button_font
        print(mouse_pos)

        # Render the "Start Button"
        start_button_surface = button_font.render(self.start_button_text,True,self.start_button_color)
        start_button_x  = self.screen_width // 2 - start_button_surface.get_width() // 2
        start_button_y = self.screen_height // 2 + start_button_surface.get_height() // 2
        self.start_button_rect = Rect(start_button_x,start_button_y,start_button_surface.get_width(),start_button_surface.get_height())
        # print(start_button_x,start_button_y)
        self.screen.blit(start_button_surface,(start_button_x,start_button_y))
        
       
        
        
        # Update the pygame display
        pygame.display.update()
        
        
    def handle_click(self,mouse_pos):
        # Check if the mouse click is inside the "Start" button's rectangle
        if self.start_button_rect and self.start_button_rect.collidepoint(mouse_pos):
            return True
        return False
    