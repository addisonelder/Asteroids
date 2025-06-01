import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface = screen,
                           color = "white",
                           center = self.position,
                           radius = self.radius,
                           width = 2,
                           )
        
    def split(self):
        # remove the asteroid that was hit
        self.kill()

        # end method if asteroid was already the smallest possible
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # generate new angles and radii for the split asteroids
        random_angle = random.uniform(20, 50)
        right = self.velocity.rotate(random_angle) * ASTEROID_SPILT_ACCELERATION
        left = self.velocity.rotate(-random_angle) * ASTEROID_SPILT_ACCELERATION
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create the new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = right
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = left

    def update(self, dt):
        self.position += self.velocity * dt