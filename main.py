import pygame, controls
from main_character import MainCharacter
from pygame.sprite import Group
from bullet import Bullet
from enemy import Enemy

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("SpaxeX by Pushkova")
    maincharacter = MainCharacter(screen)
    enemys = Group()
    bullets = Group()

    flag = True
    while flag:
        controls.events(screen, maincharacter, bullets)

        maincharacter.output()
        pygame.display.flip()
        maincharacter.moving(screen)

        controls.update(screen, enemys, maincharacter, bullets)
        controls.update_bullets(screen,bullets, enemys)

start_game()