import pygame

from board import Board
from constants import WIDTH, HEIGHT, WHITE

ARROW_KEYS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
FPS = 60

def set_window() -> pygame.Surface:
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('2048')
    window.fill(WHITE)
    return window

def make_move(board: Board, key: int) -> None:
    if key == pygame.K_LEFT:
        board.shift_left()
    elif key == pygame.K_RIGHT:
        board.shift_right()
    elif key == pygame.K_UP:
        board.shift_up()
    elif key == pygame.K_DOWN:
        board.shift_down()

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
                    make_move(board, event.key)
                    if not board.is_full():
                        board.add_block()
                    print(board)
                    print('\n')

        if board.no_moves():
            running = False
            print('No more moves\n')

main()