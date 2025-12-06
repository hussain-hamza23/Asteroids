import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
# Define each individual asteroid

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return # do not split further
        
        log_event("asteroid_split")
        # generates a random angle between 20 and 50 degrees
        randomize = random.uniform(20, 50)

        asteroid1 = self.velocity.rotate(randomize)
        asteroid2 = self.velocity.rotate(-randomize)

        
        # new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1_sprite = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2_sprite = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        
        asteroid1_sprite.velocity = asteroid1 * 1.2
        asteroid2_sprite.velocity = asteroid2 * 1.2


