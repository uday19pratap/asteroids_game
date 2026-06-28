import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape) :
    def __init__(self, x: float, y: float, radius: float) :
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) :
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) :
        self.position += self.velocity * dt
    def split(self, dt: float) :
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        log_event("asteroid_split")
        random_angle: float = random.uniform(20, 50)
        ast_1_vector = self.velocity.rotate(random_angle)
        ast_2_vector = self.velocity.rotate(-1 * random_angle)
        radius_smaller: float = self.radius - ASTEROID_MIN_RADIUS
        ast1: Asteroid = Asteroid(self.position[0], self.position[1], radius_smaller)
        ast1.velocity = ast_1_vector * 1.2
        ast2: Asteroid = Asteroid(self.position[0], self.position[1], radius_smaller)
        ast2.velocity = ast_2_vector * 1.2