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
    character = Character(screen, 0, 0)
    x = 0

    flag = True 
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                motion = LEFT
             if event.key == pygame.K_RIGHT:
                motion = RIGHT
            elif event.type == pygame.KEYUP:
             if event.key in [pygame.K_LEFT,
                         pygame.K_RIGHT]:
                motion = STOP
                

             if motion == LEFT:
              x -= 3
              print("a")
             elif motion == RIGHT:
              x += 3

        character.output()
        pygame.display.flip()
        
pygame.display.update()

start_game()