import pygame
import sys
from hero import Character
from pygame.sprite import Group
from bullet import Bullet
from control import events


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
    character = Character(screen)
    bullets = pygame.sprite.Group

    flag = True 
    while flag:
        controls.events(screen, maincharacter, bullets)
        maincharacter.output()
        pygame.display.flip()
        maincharacter.moving(screen)

        controls.update(screen, maincharacter, enemys, bullets)
        controls.update_bullets(screen, enemys,bullets)
        controls.update_enemys(stats, screen, maincharacter, enemys, bullets)

start_game()