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
                        # box.rect.x = pers.rect.x + 30
                        # box.rect.y = pers.rect.y + 50
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

def colvo(containers, inventory):
    for box in containers:
        if inventory.rect.colliderect(box):
            containers.remove(box)

"""обновление экрна"""
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
    number_container = 8


    for container_number in range(number_container):
        container = Items(screen)
        container.rect.x = 10
        container.y = container_height + 1.4 * container_height * container_number
        container.rect.y = container.y
        containers.add(container)
        print(containers)

    for container_num in range(number_container):
        container = Items(screen)
        container.x = 120
        container.rect.x = container.x
        container.y = container_height + 1.4 * container_height * container_num
        container.rect.y = container.y
        containers.add(container)
        print(containers)