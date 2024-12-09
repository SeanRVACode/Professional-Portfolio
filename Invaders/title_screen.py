import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

class StartScreen:
    def __init__(self,text,font_size,text_rgb,bg_rgb):
        """Creates the start screen with text written on it."""
        
        font = pygame.freetype.SysFont("Courier",font_size,bold=True)
        surface,_ = font.render(text=text,fgcolor=text_rgb,bgcolor=bg_rgb)
        return surface.convert_alpha()