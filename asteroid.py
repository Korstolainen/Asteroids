import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            asteroid_one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            split_angle = random.uniform(20, 50)
            asteroid_one.velocity = self.velocity * 1.2
            asteroid_two.velocity = self.velocity * 1.2
            asteroid_one.velocity = asteroid_one.velocity.rotate(split_angle)
            asteroid_two.velocity = asteroid_two.velocity.rotate(split_angle * -1)
            self.kill()




        
