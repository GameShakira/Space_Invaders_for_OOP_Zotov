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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        character.events()
            

        character.output()
        pygame.display.flip()
        character.moving(screen)
        
        screen.fill(0)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        
        character.output()
        pygame.display.flip()

        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullet.remove(bullet)





start_game()