# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init() # initilize the pygame

    # print some stuff for the user
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0 # 'delta time': time since last frame has rendered

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
        ship.draw(screen)
        ship.update(dt)

        # render the frame
        pygame.display.flip()
 
        # limit framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
