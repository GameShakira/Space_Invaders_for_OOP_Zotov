import pygame

MOVE_SPEED = 3


class Character():
   def __init__(self, screen, x, y):
      self.xvel = 0  
      self.startX = x
      self.screen = screen
      self.image =  pygame.image.load("images/hero1.png")
      self.rect = self.image.get_rect()
      self.screen_rect = screen.get_rect()
      self.rect.centerx = self.screen_rect.centerx
      self.rect.bottom = self.screen_rect.bottom

   def update(self,  left, right):
        if left:
            self.xvel = -MOVE_SPEED 
 
        if right:
            self.xvel = MOVE_SPEED 
         
        if not(left or right): 
            self.xvel = 0

        self.rect.x += self.xvel




   def output(self):
      self.screen.blit(self.image, (self.rect.x,self.rect.y))