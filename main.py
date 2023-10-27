import pygame, controls
from main_character import MainCharacter
from pygame.sprite import Group

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("SpaxeX by Pushkova")

    maincharacter = MainCharacter(screen)
    bullets = Group()

    flag = True
    while flag:
        controls.events(screen, maincharacter, bullets)
        maincharacter.output()
        pygame.display.flip()
        maincharacter.moving(screen)

        controls.update(screen, maincharacter, bullets)
        controls.update_bullets(screen,bullets)

start_game()