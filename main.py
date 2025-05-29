import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable_group.update(dt)  #updating all updatable objects

        for thing in drawable_group:    #drawing all drawable objects. has to do this trought for loop since Group.draw() requires a sprite, which objects in the groupd dont have.
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000











if __name__ == "__main__":
    main()

