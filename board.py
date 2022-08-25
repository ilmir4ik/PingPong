import pygame.draw


class Board:
    def __init__(self, side, color, screen_size):
        self.color = color
        self.screen_size = screen_size
        self.side = side
        self.w = self.screen_size[0] * 0.03
        self.h = self.screen_size[1] * 0.2
        self.x = self.screen_size[0] - self.w if self.side else 0
        self.y = self.screen_size[1] // 2 - self.h // 2
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def move(self, y_delta):
        self.y += y_delta
        if self.y < 0:
            self.y = 0
        elif self.y > self.screen_size[1] - self.h:
            self.y = self.screen_size[1] - self.h

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h])

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)
