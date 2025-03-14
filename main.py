import pygame
from constants import *
from player import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH /2), (SCREEN_HEIGHT / 2))
    dt = 0
    
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()

