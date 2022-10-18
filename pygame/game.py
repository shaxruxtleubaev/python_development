import pygame
import sys
from settings import Settings
from him import He

class App:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.scr_wdth = self.screen.get_rect().width
        self.settings.scr_hght = self.screen.get_rect().height
        pygame.display.set_caption('Begzad Invasion')
        self.bd = He(self)
        self.bg_color = self.settings.bg_color

    def run_game(self):
        while True:
            self.check_ev()
            self.bd.update()
            self._upd_screen()
    
    def check_ev(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.cke(event)
            elif event.type == pygame.KEYUP:
                self.direction(event)

    def cke(self, event):
        if event.key == pygame.K_d:
            self.bd.moving_right = True
        elif event.key == pygame.K_a:
            self.bd.moving_left = True
        elif event.key == pygame.K_w:
            self.bd.moving_top = True
        elif event.key == pygame.K_s:
            self.bd.moving_bottom = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def direction(self, event):
        if event.key == pygame.K_d:
            self.bd.moving_right = False
        elif event.key == pygame.K_a:
            self.bd.moving_left = False
        elif event.key == pygame.K_w:
            self.bd.moving_top = False
        elif event.key == pygame.K_s:
            self.bd.moving_bottom = False

    def _upd_screen(self):
        self.screen.fill(self.bg_color)
        self.bd.blithim()
        pygame.display.flip()

if __name__ == "__main__":
    game = App()
    game.run_game()