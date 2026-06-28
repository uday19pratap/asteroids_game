import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids_group, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    
    player: Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field: AsteroidField = AsteroidField()
    while True: 
        log_state()
        for event in pygame.event.get() :
            pass
            if(event.type == pygame.QUIT) :
               return
        screen.fill("black")
        
        updatable.update(dt)
        for asteroid in asteroids_group :
            if asteroid.collides_with(player) :
                log_event("player_hit")
                print("Game Over !")
                sys.exit()
        
        for asteroid in asteroids_group :
            for shot in shots :
                if not asteroid.collides_with(shot) :
                    continue
                log_event("asteroid_shot")
                asteroid.split(dt)
                shot.kill()

        for thing in drawable : 
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
