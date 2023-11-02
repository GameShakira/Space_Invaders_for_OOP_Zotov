import pygame
from hero import Character
from control import controls
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
        controls.events(screen, character, bullets)
        character.output()
        pygame.display.flip()
        character.moving(screen)

        controls.update(screen, character, Enemy, bullets)
        controls.update_bullets(screen, Enemy,bullets)
        controls.update_enemys(Stats, screen, character, Enemy, bullets)

start_game()