import pygame
from ball import Ball
from board import Board
from score_board import ScoreBoard

W, H = 720, 480
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Ping-Pong')

left_player = Board(0, pygame.Color('red'), (W, H))
right_player = Board(1, pygame.Color('blue'), (W, H))

ball_r = H * 0.05
ball = Ball(ball_r, pygame.Color('yellow'), (W, H))

score_board = ScoreBoard(pygame.Color('white'), (W, H))

FPS = 60
clock = pygame.time.Clock()
running = True
started = False
board_v = 3
ball_v = 5
left_boost = 1
right_boost = 1

while running:
    screen.fill(pygame.Color('dark green'))
    pygame.draw.line(screen, pygame.Color('white'), (W//2, 0), (W//2, H))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not started:
                    ball.start()
                    started = True
        if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
            left_boost = 2
        else:
            left_boost = 1

        if pygame.key.get_mods() & pygame.KMOD_RSHIFT:
            right_boost = 2
        else:
            right_boost = 1

    events = pygame.key.get_pressed()
    if events[pygame.K_w]:
        left_player.move(-board_v * left_boost)
    if events[pygame.K_s]:
        left_player.move(board_v * left_boost)
    if events[pygame.K_UP]:
        right_player.move(-board_v * right_boost)
    if events[pygame.K_DOWN]:
        right_player.move(board_v * right_boost)

    if started:
        res = ball.move(ball_v)
        if res == 'left':
            score_board.add_left()
        elif res == 'right':
            score_board.add_right()

    score_board.draw(screen)
    left_player.draw(screen)
    right_player.draw(screen)
    ball.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
exit(0)
