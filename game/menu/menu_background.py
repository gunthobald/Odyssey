import pygame
pygame.init()
screen = pygame.display.set_mode([1280, 720])


class MovedObjects:
    def __init__(self, image_file, pos, speed):
        self.pos = pos
        self.speed = speed
        self.image = image_file

    def draw(self):
        screen.blit(self.image, self.pos)

    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        return self.pos


class Ship(MovedObjects):
    def __init__(self, image_file, pos, speed, speed_oar, t, oar_counter):
        MovedObjects.__init__(self, image_file, pos, speed)
        self.image = image_file[0]
        self.image_list = image_file
        self.speed_oar = speed_oar
        self.t = t
        self.oar_counter = oar_counter

    def draw(self):
        MovedObjects.draw(self)

    def change(self):
        self.image = self.image_list[self.oar_counter]
        self.oar_counter += 1
        return self.image, self.oar_counter

    def move(self):
        MovedObjects.move(self)
        self.t += 1
        if self.oar_counter == 3:
            self.oar_counter = 0
        if self.t % self.speed_oar == 0:
            self.image, self.oar_counter = self.change()
        if self.pos[0] <= -1280:
            self.pos[0] = 1280
        return self.pos, self.oar_counter, self.t, self.image


class Waves(MovedObjects):
    def __init__(self, image_file, pos, speed, wrapped_pos, wrap_pos, choice):
        MovedObjects.__init__(self, image_file, pos, speed)
        self.wrapped_pos = wrapped_pos
        self.wrap_pos = wrap_pos
        self.choice = choice

    def move(self):
        MovedObjects.move(self)
        if self.choice == "r":
            if self.pos[0] >= self.wrap_pos:
                self.pos[0] = self.wrapped_pos
        elif self.choice == "l":
            if self.pos[0] <= self.wrap_pos:
                self.pos[0] = self.wrapped_pos
                print(self.pos)
        return self.pos

    def draw(self):
        MovedObjects.draw(self)
