import pygame
from settings import Settings

class He:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load('image/bd.jpg')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left  = False
        self.moving_top = False
        self.moving_bottom = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.bd_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.bd_speed
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.bd_speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.bd_speed                
        
        self.rect.x = self.x
        self.rect.y = self.y

    def blithim(self):
        self.screen.blit(self.image, self.rect)