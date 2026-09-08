import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop:
    # - Check for player inputs
    # - Update the game world
    # - Draw the game to the screen
    while True:
        log_state()

        # pygame event queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()  # refresh the screen


if __name__ == "__main__":
    main()
