import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

class StartScreen:
    def __init__(self,text,font_size,text_rgb,bg_rgb,screen,screen_width,screen_height,mouse_pos):
        # TODO Add Hover Effects
        """Creates the start screen with text written on it."""
        screen.fill((0,0,0))
        font = pygame.font.SysFont("Courier",font_size,bold=True)
        title = font.render(text,True,(255,255,255))
        start_button = font.render('Start',True,(255,255,255))
        screen.blit(title,(screen_width/2 - title.get_width()/2,screen_height/2 - title.get_height()/2))
        screen.blit(start_button,(screen_width/2 - start_button.get_width()/2,screen_height/2 + start_button.get_height()/2))
        pygame.display.update()
        # surface,_ = font.render(text=text,fgcolor=text_rgb,bgcolor=bg_rgb)
        # TODO Feed mouse postion into here so that I can determine when to make buttons larger
        