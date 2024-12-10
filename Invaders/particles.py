import pygame,sys

class ParticlePrinciple:
    def __init__(self,screen,mouse_pos):
        self.particles = []
        self.screen = screen
        self.mouse_pos = mouse_pos
        
    def emit(self):
        if self.particles:
            self.delete_particles()
            print('Emitting')
            for particle in self.particles:
                # Move
                particle[0][1] += particle[2]
                # Shrink
                particle[1] -= 0.2
                # Draw a cirlce around the particle
                pygame.draw.circle(self.screen,pygame.Color('White'),particle[0], int(particle[1]))
                
    def add_particles(self):
        print('Adding Particles')
        # Temp postions in 'middle' of screen
        pos_x,pos_y = self.mouse_pos
        
        radius = 10
        
        direction = 5
        
        particle_circle = [[pos_x,pos_y],radius,direction]
        
        self.particles.append(particle_circle)
        
        
    
    def delete_particles(self):
        particles_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particles_copy
        
        