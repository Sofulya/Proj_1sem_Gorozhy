import pygame, controlls, controlls2
from pers import Pers
from inventory import Inventory
from pygame.sprite import Group
from Score import Score

"""Первый уровень"""


def run():
    pygame.init()
    screen = pygame.display.set_mode((1400, 1000))
    pygame.display.set_caption("Грузчик")
    background_color = pygame.image.load('images/fon2.jpg').convert()
    pers = Pers(screen)
    inventory = Inventory(screen)
    containers = Group()
    score = Score()
    controlls.create_items(screen, containers)

    while True:
        controlls.events(pers, containers)
        controlls.colvo(containers, inventory, score)
        pers.update_pers()
        controlls.update(background_color, screen, pers, containers, inventory)


"""Второй уровень"""


def run2():
    pygame.init()
    screen = pygame.display.set_mode((1400, 1000))
    pygame.display.set_caption("ГРУЗЧИК")
    background_color = pygame.image.load('images/fon.jpg').convert()
    pers = Pers(screen)
    inventory = Inventory(screen)
    containers = Group()
    controlls2.create_items(screen, containers)

    while True:
        controlls2.events(pers, containers)
        controlls2.colvo(containers, inventory)
        pers.update_pers()
        controlls2.update(background_color, screen, pers, containers, inventory)


run()

""""(0, 0, 0)"""
