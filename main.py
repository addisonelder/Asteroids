# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init() # initilize the pygame

    # print some info for the user
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create the background
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create the clock and init delta time
    clock = pygame.time.Clock()
    dt = 0 # 'delta time': time since last frame has rendered

    # create the pygame groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # set containers attributes
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    # create the initial obejcts
    ship = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


# this is the game loop
    while True:
        # exit the game loop when we close the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # load the elements that should get rendered
        screen.fill("black")
        for sprite in drawables:
            sprite.draw(screen)
        for sprite in updatables:
            sprite.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(ship):
                sys.exit("Game Over!")

        # render the frame
        pygame.display.flip()
 
        # limit framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
