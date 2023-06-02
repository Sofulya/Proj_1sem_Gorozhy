import pygame

class Pers():

    def __init__(self, screen):
        """инициализация персонажа"""

        self.screen = screen
        self.image = pygame.image.load('images/pers.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.rect.bottom = self.screen_rect.bottom
        """для клавиш"""
        self.mtop = False
        self.mdown = False
        self.mright = False
        self.mleft = False

    def output(self):
        """отрисовка персонажа"""
        self.screen.blit(self.image, self.rect)


    def update_pers(self):
        """обновление позиции персонажа"""

        """обновление для движения вверх"""
        if self.mtop and self.rect.top > self.screen_rect.top:
            self.centery -= 0.6

        """обновление для движения вниз"""
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 0.6

        """обновление для движения влево"""
        if self.mleft and self.rect.left > 0:
            self.centerx -= 0.6

        """обновление для движения вправо"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.centerx += 0.6

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery




