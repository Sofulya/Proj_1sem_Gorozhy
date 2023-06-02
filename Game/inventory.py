import pygame

class Inventory():
    """инициализация инвентаря"""
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/inv3.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.width = 200
        self.rect.height = 400


    def draw(self, screen):
        """рисование склада"""
        self.screen.blit(self.image, self.rect)