import pygame, sys
from bullet import Bullet
from enemy import Enemy
from hero import Character
import time


def events(screen, maincharacter, bullets):
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


def update(screen, hero, enemy, bullets):
    screen.fill(0)
    for bullets in bullets.sprites():
        print("Иди нахуй")
    hero.output()
    enemy.draw(screen)
    pygame.display.flip()


def update_bullets(screen, enemys, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)
    if len(enemys) == 0:
        bullets.empty()
        create_army(screen, enemys)
def update_enemys(stats, screen, maincharacter, enemys, bullets):
    enemys.update()
    if pygame.sprite.spritecollideany(maincharacter, enemys):
        #print("!!!!!!!!!!!!")
        maincharacter_kill(stats, screen, maincharacter, enemys, bullets)
        enemys_check(stats, screen, maincharacter, enemys, bullets)

def create_army(screen, enemys):
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((600 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((900 - 500 - 2 * enemy_height) / enemy_height)
    for row_num in range(number_enemy_y):
        for enemy_num in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + enemy_width * enemy_num
            enemy.y = enemy_height + enemy_height * row_num
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + enemy.rect.height * row_num
            enemys.add(enemy)

def maincharacter_kill(stats, screen, maincharacter, enemys, bullets):
    if stats.maincharacter_hp > 0:
        stats.maincharacter_hp -= 1
        enemys.empty()
        bullets.empty()
        create_army(screen, enemys)
        maincharacter.create_maincharacter_again()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def enemys_check(stats, screen, maincharacter, enemys, bullets):
    screen_rect = screen.get_rect()
    for enemy in enemys.sprites():
        if enemy.rect.bottom > screen_rect.bottom:
            maincharacter_kill(stats, screen, maincharacter, enemys, bullets)
            break