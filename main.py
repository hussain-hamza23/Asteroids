import pygame
import sys
from constants import SCREEN_HEIGHT , SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print("Screen width: 1280 Screen height: 720")
    # set up sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # set up the drawing window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # variables for framerate management
    fps = pygame.time.Clock()
    delta_time = 0
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable) 
    Shot.containers = (shots, updatable, drawable)
    # creates a new player instance. Parameters are the starting x and y position
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # generrate the asteroid field
    asteroid_field = AsteroidField()

    while True:
        #log events
        log_state()
        # allows quitting the game without using CTRL+C
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # update all updatable sprites
        updatable.update(delta_time)    
        # draw the GUI    
        screen.fill("black")
        # draw the player. Must be done before flipping the display.
        # Must iterate through drawable group to access the draw method in each sprite
        for sprite in drawable:  
            sprite.draw(screen)
        # check collision between player and asteroids. End the game if collision occurs    
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
                return
            # check collision with shots. If collision occurs, split the asteroid and remove the shot
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        # lmit to 60 FPS
        delta_time = fps.tick(60) / 1000.0
       

        
    

if __name__ == "__main__":
    main()

