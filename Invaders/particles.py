import pygame,sys
import random

class ParticlePrinciple:
    def __init__(self,screen,color='White'):
        self.particles = []
        self.emitters = []
        self.screen = screen
        self.color = color
        
    def add_emitter(self,emitter_id,position,direction=(0,0),color=(255,255,255),spread=1):
        # Add or update an emitter with its unique ID
        emitter = next((e for e in self.emitters if e["id"] == emitter_id), None)
        if emitter:
            emitter["position"] = position
            emitter["direction"] = direction
        else:
            self.emitters.append({"id":emitter_id,
                                  "position":position,
                                  "direction":direction,
                                  "particles":[],
                                  "color":color,
                                  "spread":spread})
            
    def emit(self):
        for emitter in self.emitters:
            self.delete_particles(emitter["particles"])
            for particle in emitter["particles"]:
                # Apply movement and shrink
                particle[0][0] += emitter["direction"][0] + random.randint(-emitter["spread"],emitter["spread"])
                particle[0][1] += emitter["direction"][1] + random.randint(-emitter["spread"],emitter["spread"])
                particle[1] -= 0.5 # Shrink
                if particle[1] > 0: # Only Draw Visible Particles
                    pygame.draw.circle(self.screen,emitter["color"],particle[0],int(particle[1]))
                
    def add_particles(self,emitter_id,radius=10):
        # Add particles for each specific emitter
        emitter = next((e for e in self.emitters if e["id"] == emitter_id), None)
        
        if emitter:
            pos_x,pos_y = emitter["position"]
            particle_circle = [[pos_x,pos_y],radius,1] # Particle with position, radius, and direction
            emitter["particles"].append(particle_circle)        
        
    
    def delete_particles(self,particles):
        # Delete Particles with a radius of 0 or less
        particles[:] = [particle for particle in particles if particle[1] > 0]
        # particles_copy = [particle for particle in self.particles if particle[1] > 0]
        # self.particles = particles_copy
        
        