import pygame
pygame.init()
screen = pygame.display.set_mode([1280, 720])


def aabb(pos1, size1, pos2, size2):
    return pos1[0] + size1[0] >= pos2[0] + size2[0] >= pos1[0] and pos1[1] + size1[1] >= pos2[1] + size2[1] >= pos1[1] and pos2[1]


def mouse_drag():
    drag = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            drag = True
            if event.type == pygame.MOUSEBUTTONUP:
                drag = False
    return drag


def mouse_collision(pos1, size1, image_file):
    pos2 = pygame.mouse.get_pos()
    collision = aabb(pos1, size1, pos2, [0, 0])
    if collision:
        screen.blit(image_file, pos1)
    return collision


def mouse_click(pos1, size1, image_file):
    click = False
    if mouse_collision(pos1, size1, image_file):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
    return click
