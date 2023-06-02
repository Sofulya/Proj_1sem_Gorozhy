import pygame, sys
from container import Items

def events(pers, containers):
    """обработка событий"""

    """функция трекинга клавиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            """идет вверх"""
            if event.key == pygame.K_w:
                pers.mtop = True

            """идет вниз"""
            if event.key == pygame.K_s:
                pers.mdown = True

            """идет вправо"""
            if event.key == pygame.K_d:
                pers.mright = True

            """идет влево"""
            if event.key == pygame.K_a:
                pers.mleft = True

            """подбор объекта айтемс"""
            if event.key == pygame.K_SPACE:
                for box in containers:
                    if pers.rect.colliderect(box.rect):
                        # box.x = pers.rect.x + 30
                        # box.y = pers.rect.y + 50
                        box.upd(pers)

        elif event.type == pygame.KEYUP:

            """не идет вверх"""
            if event.key == pygame.K_w:
                pers.mtop = False

            """не идет вниз"""
            if event.key == pygame.K_s:
                pers.mdown = False

            """не идет вправо"""
            if event.key == pygame.K_d:
                pers.mright = False

            """не идет влево"""
            if event.key == pygame.K_a:
                pers.mleft = False

def colvo(containers, inventory, score):
    for box in containers:
        if inventory.rect.colliderect(box):
            containers.remove(box)
            score.score_upg()

"""обновление экрана"""
def update(background_color, screen, pers, containers, inventory):
    """screen.fill(background_color)"""
    screen.blit(background_color, (0, 0))
    inventory.rect.x = 1200
    inventory.rect.y = 300
    inventory.draw(screen)
    pers.output()
    containers.draw(screen)
    pygame.display.flip()

def create_items(screen, containers):
    """create items for screen"""
    container = Items(screen)
    container_height = container.rect.height
    number_container = int((800 - 2 * container_height) / container_height)


    for container_number in range(number_container):
        container = Items(screen)
        container.y = container_height + 1.4 * container_height * container_number
        container.rect.y = container.y
        containers.add(container)
        print(containers)