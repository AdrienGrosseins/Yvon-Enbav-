import pygame

class Ball():
    def __init__(self):
        self.x = 600
        self.y = 325
        self.change_x = 1
        self.change_y = 0
        self.size = 12
        self.color = [51, 25, 0]

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

    def contact_mur(self):
        if self.x + self.size > 1052 or self.x - self.size < 148:
            self.change_x = -self.change_x
        if self.y + self.size > 550 or self.y - self.size < 100:
            self.change_y = -self.change_y




