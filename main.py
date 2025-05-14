import sys

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
    # Create a Game Clock
    game_clock = pygame.time.Clock()
    dt = 0

    # Create groups to manage objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add static class containers variable to classes
    # before creating any Player instances
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create a Player object
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    # Create AsteroidField object
    asteroidfield = AsteroidField()

    # Create Asteroid object group

    # Setup the Game Event Loop
    game_loop = True
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # blanking the screen??
        screen.fill("black")

        # use the sprite group to make an update call
        updatable.update(dt)

        # check for collisions with player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                # then ship was hit
                print("Game over!")
                sys.exit()
            # check for asteroid and shot collisions
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

        # lastly, draw the player
        for thing in drawable:
            thing.draw(screen)

        # causes screen buffer to be drawn
        pygame.display.flip()

        # Limit framerate to 60fps
        dt = game_clock.tick(60)/1000


if __name__ == "__main__":
    main()
