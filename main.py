import pygame
import sys
from hero import Character


#██╗░░░░░░█████╗░██╗░░░██╗███████╗
#██║░░░░░██╔══██╗██║░░░██║██╔════╝
#██║░░░░░██║░░██║╚██╗░██╔╝█████╗░░
#██║░░░░░██║░░██║░╚████╔╝░██╔══╝░░
#███████╗╚█████╔╝░░╚██╔╝░░███████╗
#╚══════╝░╚════╝░░░░╚═╝░░░╚══════╝



def start_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Space Y")
    character = Character(screen, 100, -410)

    flag = True 
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                right = True
            if event.type == pygame.KEYUP and event.key == pygame.K_d:
                right = False
            if event.type == pygame.KEYUP and event.key == pygame.K_a:
                left = False
               

        character.output()
        pygame.display.flip()
        



start_game()