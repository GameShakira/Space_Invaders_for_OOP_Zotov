import pygame
from hero import Character
import control
from enemy import Enemy
from stats import Stats


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
        control.events(screen, character, bullets)
        character.output()
        pygame.display.flip()
        character.moving(screen)

        control.update(screen, character, Enemy, bullets)
        control.update_bullets(screen, Enemy,bullets)
        control.update_enemys(Stats, screen, character, Enemy, bullets)

start_game()