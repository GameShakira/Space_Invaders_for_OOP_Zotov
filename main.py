import pygame
import sys
from hero import Character


#██╗░░░░░░█████╗░██╗░░░██╗███████╗
#██║░░░░░██╔══██╗██║░░░██║██╔════╝
#██║░░░░░██║░░██║╚██╗░██╔╝█████╗░░
#██║░░░░░██║░░██║░╚████╔╝░██╔══╝░░
#███████╗╚█████╔╝░░╚██╔╝░░███████╗
#╚══════╝░╚════╝░░░░╚═╝░░░╚══════╝

RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
motion = STOP

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Space Y")
    character = Character(screen)
    

    flag = True 
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    character.move_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    character.move_right = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    character.move_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    character.move_left = False
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_w:
                  character.shoot()        

        character.output()
        pygame.display.flip()
        character.moving(screen)
        


start_game()