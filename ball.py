import random
from math import *

import pygame.draw


class Ball:
    def __init__(self, r, color, screen_size):
        self.r = r
        self.screen_size = screen_size
        self.x = self.screen_size[0] // 2 - self.r
        self.y = self.screen_size[1] // 2 - self.r
        self.color = color

        self.angle = 0

    def move(self, v):
        self.x = self.x + cos(radians(self.angle)) * v
        self.y = self.y - sin(radians(self.angle)) * v
        self.collision_with_wall()

        res = self.check_loss()
        if res:
            print(res)
            self.start()
        return res

    def check_loss(self):
        if self.x <= 0:
            return 'left'
        elif self.x + 2 * self.r >= self.screen_size[0]:
            return 'right'
        else:
            return False

    def collision_with_wall(self):
        if self.y <= 0 and self.angle < 180:
            self.angle = (self.angle + abs(2 * (180 - self.angle))) % 360
        if self.y >= self.screen_size[1] - 2 * self.r and self.angle >= 270:
            self.angle = 360 - self.angle
        if self.y >= self.screen_size[1] - 2 * self.r and 180 <= self.angle < 270:
            self.angle = self.angle - 2 * (self.angle - 180)

    def start(self):
        self.x = self.screen_size[0] // 2 - self.r
        self.y = self.screen_size[1] // 2 - self.r
        self.angle = random.choice(list(range(-60, 61)) + list(range(120, 241))) % 360
        # self.angle = random.choice(list(range(45, 136)) + list(range(225, 315))) % 360

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x + self.r, self.y + self.r), self.r)
