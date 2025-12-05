import pygame
from constants import SCREEN_HEIGHT , SCREEN_WIDTH
from logger import log_state

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print("Screen width: 1280 Screen height: 720")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        pygame.display.flip()



if __name__ == "__main__":
    main()

