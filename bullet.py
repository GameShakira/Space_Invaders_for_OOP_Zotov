import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, character):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 12)
        self.image = pygame.image.load("images/img2.png")
        self.speed = 4.5
        self.rect.centerx = character.rect.centerx
        self.rect.top = character.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)