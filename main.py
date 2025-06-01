# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

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

    # set containers for the Player class
    Player.containers = (updatables, drawables)

    # create the ship (player) object
    ship = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

# this is the game loop
    while True:
        # exit the game when we close the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # load the elements that should get rendered
        screen.fill("black")
        for sprite in drawables:
            sprite.draw(screen)
        for sprite in updatables:
            sprite.update(dt)

        # render the frame
        pygame.display.flip()
 
        # limit framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
