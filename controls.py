import pygame, sys
from bullet import Bullet
from enemy import Enemy

def events(screen, maincharacter, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                maincharacter.move_right = True
            if event.key == pygame.K_LEFT:
                maincharacter.move_left = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, maincharacter)
                bullets.add(new_bullet)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                maincharacter.move_left = False
            if event.key == pygame.K_RIGHT:
                maincharacter.move_right = False

def update(screen, maincharacter, bullets):
    screen.fill(0)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    maincharacter.output()
    pygame.display.flip()

def update_bullets(screen, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_army():
    enemy = Enemy(screen)
    enemy_widht = enemy.rect.width
    number_enemy_x = int(1000 - 2 * enemy_widht) / enemy_widht

    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 400 - 2 * enemy_height) / enemy_height)

    for i in range(number_enemy_y):
        for j in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_widht + enemy_widht * j
            enemy.y = enemy_height + enemy_height * i
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.y
            
