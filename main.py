import pygame
from ball import Ball
from board import Board
from score_board import ScoreBoard


class Game:
    def __init__(self):
        self.screen_size = self.W, self.H = 720, 480

        pygame.init()
        pygame.display.set_caption('Ping-Pong')
        self.screen = pygame.display.set_mode((self.W, self.H))

        self.left_player = Board(0, pygame.Color('red'), (self.W, self.H))
        self.right_player = Board(1, pygame.Color('blue'), (self.W, self.H))

        self.ball_r = self.H * 0.05
        self.ball = Ball(self.ball_r, pygame.Color('yellow'), self)

        self.score_board = ScoreBoard(pygame.Color('white'), (self.W, self.H))

        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.running = True
        self.started = False
        self.board_v = 3
        self.ball_v = 5
        self.left_boost = 1
        self.right_boost = 1

        while self.running:
            self.screen.fill(pygame.Color('dark green'))
            pygame.draw.line(self.screen, pygame.Color('white'), (self.W // 2, 0), (self.W // 2, self.H))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.started and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            self.ball.start()
                            self.started = True
                        elif not self.started:
                            self.started = True
                        else:
                            self.started = False
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    self.left_boost = 2
                else:
                    self.left_boost = 1

                if pygame.key.get_mods() & pygame.KMOD_RSHIFT:
                    self.right_boost = 2
                else:
                    self.right_boost = 1

            self.move_boards()
            self.move_ball()
            self.draw()

        self.exit()

    def move_boards(self):
        events = pygame.key.get_pressed()
        if events[pygame.K_w]:
            self.left_player.move(-self.board_v * self.left_boost)
        if events[pygame.K_s]:
            self.left_player.move(self.board_v * self.left_boost)
        if events[pygame.K_UP]:
            self.right_player.move(-self.board_v * self.right_boost)
        if events[pygame.K_DOWN]:
            self.right_player.move(self.board_v * self.right_boost)

    def move_ball(self):
        if self.started:
            res = self.ball.move(self.ball_v)
            if res == 'left':
                self.score_board.add_left()
            elif res == 'right':
                self.score_board.add_right()

    def draw(self):
        self.score_board.draw(self.screen)
        self.left_player.draw(self.screen)
        self.right_player.draw(self.screen)
        self.ball.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(self.FPS)

    def exit(self):
        pygame.quit()
        exit(0)


def main():
    game = Game()


if __name__ == '__main__':
    main()
