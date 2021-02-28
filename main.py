import pygame

from time import sleep
from board import Board
from constants import *

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
    valid_move = False
    if key == pygame.K_LEFT:
        if board.shift_left() == 1:
            valid_move = True
    elif key == pygame.K_RIGHT:
        if board.shift_right() == 1:
            valid_move = True
    elif key == pygame.K_UP:
        if board.shift_up() == 1:
            valid_move = True
    elif key == pygame.K_DOWN:
        if board.shift_down() == 1:
            valid_move = True
    board.draw(window)
    pygame.display.update()
    if not board.is_full() and valid_move == True:
        sleep(NEW_BLOCK_DELAY)
        for i in range(NEW_BLOCKS_PER_MOVE):
            board.add_block()
        board.draw(window)
        pygame.display.update()

# clears and resets the board
def reset_board(board: list, window: pygame.Surface) -> None:
    board.clear()
    board.draw(window)
    pygame.display.update()

# def draw_finish_screen(window: pygame.Surface) -> None:
#     bg = pygame.Rect(0, 0, WIDTH, HEIGHT)
#     s = pygame.Surface(pygame.Rect(bg).size, pygame.SRCALPHA)
#     pygame.draw.rect(s, (255, 255, 255, 128), s.get_rect())
#     window.blit(s, (0, 0))

# def over(window: pygame.Surface) -> None:
#     draw_finish_screen(window)

# main function with event loop
def main() -> None:
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()

    window = set_window()

    board = Board()
    board.draw(window)
    pygame.display.update()

    game_over = False

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Arrow keys are pressed
                if not game_over and event.key in ARROW_KEYS:
                    make_move(board, event.key, window)
                    if board.no_moves() and game_over == False:
                        game_over = True
                        # over(window)
                # C is pressed
                if event.key == pygame.K_c:
                    reset_board(board, window)
                    game_over = False
                # X is pressed
                if event.key == pygame.K_x:
                    running = False

main()
