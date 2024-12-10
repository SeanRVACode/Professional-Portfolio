import pygame,sys

class ParticlePrinciple:
    def __init__(self,screen):
        self.particles = []
        self.screen = screen
        
    def emit(self):
        if self.particles:
            for particle in self.particles:
                # Move
                particle[0][1] += particle[2]
                # Shrink
                particle[1] -= 0.2
                # Draw a cirlce around the particle
                pygame.draw.circle(self.screen,pygame.Color('White'),particle[0], int(particle[1]))
                
    def add_particles(self):
        # Temp postions in 'middle' of screen
        pos_x = 250
        pos_y = 250
        
        radius = 10
        
        direction = 1
        
        particle_cirlce = [[pos_x,pos_y],radius,direction]
        
        self.particles.append(particle_cirlce)
        
        
    
    def delete_particles(self):
        pass # delete particles after a certain time
        