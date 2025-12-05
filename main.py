import pygame
from constants import SCREEN_HEIGHT , SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print("Screen width: 1280 Screen height: 720")

    # set up the drawing window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # variables for framerate management
    fps = pygame.time.Clock()
    delta_time = 0
    # creates a new player instance. Parameters are the starting x and y position
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        #log events
        log_state()
        # allows quitting the game without using CTRL+C
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # draw the GUI    
        screen.fill("black")
        # draw the player. Must be done before flipping the display.
        player.draw(screen)
        pygame.display.flip()

        # lmit to 60 FPS
        fps.tick(60)
        delta_time = fps.tick(60) / 1000.0

        
    

if __name__ == "__main__":
    main()

