import pygame

from board import Board
from constants import WIDTH, HEIGHT, WHITE

# Author: Nigel Davis
# Title: 2048 Game
# Version: v0.7a

ARROW_KEYS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
FPS = 60

# set the initial conditions of the game window
def set_window() -> pygame.Surface:
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('2048')
    window.fill(WHITE)
    return window

# execute move required based on user input
def make_move(board: Board, key: int, window: pygame.Surface) -> None:
    if key == pygame.K_LEFT:
        board.shift_left()
    elif key == pygame.K_RIGHT:
        board.shift_right()
    elif key == pygame.K_UP:
        board.shift_up()
    elif key == pygame.K_DOWN:
        board.shift_down()
    if not board.is_full():
        board.add_block()
    board.draw(window)
    pygame.display.update()

# main function with event loop
def main() -> None:
    pygame.init()
    clock = pygame.time.Clock()

    window = set_window()

    board = Board()
    board.draw(window)
    pygame.display.update()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key in ARROW_KEYS:
                    make_move(board, event.key, window)
                    print(board)
                    print('\n')

        if board.no_moves():
            running = False
            print('No more moves\n')

main()