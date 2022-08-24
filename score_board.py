import pygame.font


class ScoreBoard:
    def __init__(self, color, screen_size):
        self.left = 0
        self.right = 0
        self.color = color

        self.w = 0.2 * screen_size[0]
        self.h = 0.1 * screen_size[1]
        self.y = 0.05 * screen_size[1]
        self.x = screen_size[0] // 2 - self.w // 2

    def add_left(self):
        self.left += 1

    def add_right(self):
        self.right += 1

    def draw(self, screen):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        left_num_text = font.render(str(self.left), False, self.color)
        right_num_text = font.render(str(self.right), False, self.color)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), width=1)
        screen.blit(left_num_text, (self.x + self.w * 0.25 - left_num_text.get_width() // 2,
                                    self.y + self.h * 0.5 - left_num_text.get_height() // 2))
        screen.blit(right_num_text, (self.x + self.w * 0.75 - right_num_text.get_width() // 2,
                                     self.y + self.h * 0.5 - right_num_text.get_height() // 2))
