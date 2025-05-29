import pygame

from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids_group = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    AsteroidField.containers = updatable_group
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (updatable_group, drawable_group, asteroids_group)
    Shot.containers = (updatable_group, drawable_group, shots_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable_group.update(dt)  #updating all updatable objects

        for thing in asteroids_group:
            if thing.collision_check(player) == True:
                print("Game Over!")
                sys.exit()

        for thing in asteroids_group:
            for bullet in shots_group:
                if thing.collision_check(bullet) == True:
                    thing.kill()
                    bullet.kill()


        for thing in drawable_group:    #drawing all drawable objects. has to do this trought for loop since Group.draw() requires a sprite, which objects in the groupd dont have.
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000











if __name__ == "__main__":
    main()

