# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
    # Create a Game Clock
    game_clock = pygame.time.Clock()
    dt = 0

    # Create a Player object
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    # Setup the Game Event Loop
    game_loop = True
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # blanking the screen??
        screen.fill("black")

        # have the player draw itself into the screen buffer
        # first update the player's information
        player.update(dt)
        # lastly, draw the player
        player.draw(screen)

        # causes screen buffer to be drawn
        pygame.display.flip()

        # Limit framerate to 60fps
        dt = game_clock.tick(60)/1000


if __name__ == "__main__":
    main()
