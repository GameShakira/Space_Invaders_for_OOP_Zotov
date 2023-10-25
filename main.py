import pygame
import sys
from Hero import MainCharacter

def start_game ():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("SpaceX by Andrei")

    flag = True
    hero = MainCharacter(screen)
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    hero.move_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    hero.move_right = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.move_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    hero.move_left = False

        hero.output()
        pygame.display.flip()
        hero.moving(screen)

start_game()