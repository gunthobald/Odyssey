import pygame
import commons
import sys
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([1280, 720])


class ButtonClass:
    def __init__(self, image_file, pos):
        self.image = pygame.image.load(image_file)
        self.pos = pos
        self.size = [self.image.get_rect()[2], self.image.get_rect()[3]]

    def click(self):
        click = commons.mouse_click(self.pos, self.size, self.image)
        return click


class QuitGame(ButtonClass):
    def __init__(self, image_file, pos):
        ButtonClass.__init__(self, image_file, pos)

    def click(self):
        global run
        click = ButtonClass.click(self)
        if click:
            sys.exit(1)
