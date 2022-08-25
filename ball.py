import random
from math import *

import pygame.draw

from board import Board


class Ball:
    def __init__(self, r, color, game):
        self.r = r
        self.game = game
        self.screen_size = game.screen_size
        self.x = self.screen_size[0] // 2 - self.r
        self.y = self.screen_size[1] // 2 - self.r
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.r * 2, self.r * 2)

        self.angle = 0

    def move(self, v):
        self.x = self.x + cos(radians(self.angle)) * v
        self.y = self.y - sin(radians(self.angle)) * v
        self.collision_with_wall()
        self.collision_with_boards()

        res = self.check_loss()
        if res:
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

    def collision_with_boards(self):
        left_board: Board = self.game.left_player
        right_board: Board = self.game.right_player
        l_rect: pygame.Rect = left_board.get_rect()
        r_rect: pygame.Rect = right_board.get_rect()
        ball_rect: pygame.Rect = self.get_rect()
        if ball_rect.colliderect(l_rect):
            print(ball_rect.centery)
            touchpoint = ball_rect.centery - l_rect.y
            print(touchpoint)
            new_angle = (100 - touchpoint / l_rect.h * 100 - 50) % 360
            self.angle = new_angle
        elif ball_rect.colliderect(r_rect):
            touchpoint = ball_rect.centery - r_rect.y
            new_angle = touchpoint / r_rect.h * 100 + 120
            self.angle = new_angle

    def start(self):
        self.x = self.screen_size[0] // 2 - self.r
        self.y = self.screen_size[1] // 2 - self.r
        self.angle = random.choice(list(range(-60, 61)) + list(range(120, 241))) % 360
        # self.angle = random.choice(list(range(45, 136)) + list(range(225, 315))) % 360

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x + self.r, self.y + self.r), self.r)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.r * 2, self.r * 2)
