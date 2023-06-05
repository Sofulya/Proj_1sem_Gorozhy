import pygame, sys, controlls, controlls2
from pers import Pers
from inventory import Inventory
from pygame.sprite import Group

pygame.font.init()
screen = pygame.display.set_mode((1400, 1000))
pygame.font.init()
class Menu:

    def __init__(self, punkts = [120, 140, u'Punkt', (250, 250, 30), (250, 30, 250)]):

        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):

        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        done = True
        b_c = pygame.image.load('images/menu_fon.jpg').convert()
        screen.blit(b_c, (0, 0))
        font_menu = pygame.font.Font('fonts/ArialRegular.ttf', 50)
        punkt = 0
        while done:

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0]  and mp[0] < i[0]+155 and mp[1] > i[1] and mp[1] < i[1]+50:
                    punkt = i[5]
                self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) -1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()
            pygame.display.flip()

"""создание меню"""
punkts = [(600, 400, u'ИГРАТЬ', (250, 250, 30), (255, 20, 0), 0),
          (600, 500, u'ВЫЙТИ', (250, 250, 30), (255, 20, 0), 1)]

game = Menu(punkts)
game.menu()
"""Первый уровень"""
def run():

    pygame.init()
    screen = pygame.display.set_mode((1400, 1000))
    pygame.display.set_caption("Грузчик")
    background_color = pygame.image.load('images/fon2.jpg').convert()
    pers = Pers(screen)
    inventory = Inventory(screen)
    containers = Group()
    controlls.create_items(screen, containers)
    i = 0

    while True:
        """подсчет занесенных контейнеров, переход на следующий уровень"""
        for box in containers:
            if inventory.rect.colliderect(box):
                containers.remove(box)
                i += 1
                if i == 8:
                    run2()
                print(i)
        controlls.events(pers, containers)
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
    a = 0

    while True:
        """подсчет занесенных контейнеров, переход в меню"""
        for box in containers:
            if inventory.rect.colliderect(box):
                containers.remove(box)
                a += 1
                if a == 16:
                    game.menu()
                print(a)
        controlls2.events(pers, containers)
        pers.update_pers()
        controlls2.update(background_color, screen, pers, containers, inventory)

run()


""""(0, 0, 0)"""