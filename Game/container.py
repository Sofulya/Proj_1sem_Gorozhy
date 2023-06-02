import pygame

"""один ящик"""


class Items(pygame.sprite.Sprite):

    def __init__(self, screen):
        """инициализация"""
        super(Items, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/items.png')
        self.rect = self.image.get_rect()
        self.rect.width = 80
        self.rect.height = 80
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """отрисовка ящика"""
        self.screen.blit(self.image, self.rect)

    """перемещение ящика"""

    def upd(self, pers):
        self.rect.x, self.rect.y = pers.rect.x + 30, pers.rect.y + 50
