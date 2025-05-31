# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init() # initilize the pygame
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    while running:
        # exit the game when we close the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # render the game
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
