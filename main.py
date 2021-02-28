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
    icon = pygame.image.load('rsc/icon.png')
    pygame.display.set_icon(icon)
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

# clears and resets the board
def reset_board(board: list, window: pygame.Surface) -> None:
    board.clear()
    board.draw(window)

def draw_finish_screen(window: pygame.Surface) -> None:
    # faded background
    bg = pygame.Rect(0, 0, WIDTH, HEIGHT)
    s = pygame.Surface(pygame.Rect(bg).size, pygame.SRCALPHA)
    pygame.draw.rect(s, COLORS['start_screen'], s.get_rect())
    window.blit(s, (0, 0))
    # 'game over' text
    font = pygame.font.Font(FONT, 70)
    text = font.render("GAME OVER!", True, COLORS['dark_text'])
    text_x = GAME_OVER_POS_W - text.get_rect().width // 2
    text_y = GAME_OVER_POS_H - text.get_rect().height // 2
    text_placement = (text_x, text_y)
    window.blit(text, text_placement)

def over(window: pygame.Surface) -> None:
    draw_finish_screen(window)

def draw_button(window: pygame.Surface, mouse) -> None:
    if mouse_on_button(mouse):
        x_offset = RESTART_BUTTON_POS_W - RESTART_BUTTON_WIDTH // 2
        y_offset = RESTART_BUTTON_POS_H - RESTART_BUTTON_HEIGHT // 2
        button = pygame.Rect(x_offset, y_offset, RESTART_BUTTON_WIDTH, RESTART_BUTTON_HEIGHT)
        pygame.draw.rect(window, COLORS['dark_text'], button, border_radius=BLOCK_RADIUS)
    else:
        x_offset = RESTART_BUTTON_POS_W - RESTART_BUTTON_WIDTH // 2
        y_offset = RESTART_BUTTON_POS_H - RESTART_BUTTON_HEIGHT // 2
        button = pygame.Rect(x_offset, y_offset, RESTART_BUTTON_WIDTH, RESTART_BUTTON_HEIGHT)
        pygame.draw.rect(window, COLORS['dark_text'], button, border_radius=BLOCK_RADIUS)

def mouse_on_button(mouse):
    return RESTART_BUTTON_POS_W - RESTART_BUTTON_WIDTH // 2 <= mouse[0] <= RESTART_BUTTON_POS_W + RESTART_BUTTON_WIDTH // 2 and RESTART_BUTTON_POS_H - RESTART_BUTTON_HEIGHT // 2 <= mouse[1] <= RESTART_BUTTON_POS_H + RESTART_BUTTON_HEIGHT // 2

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
                        over(window)
                # C is pressed
                if event.key == pygame.K_c:
                    reset_board(board, window)
                    game_over = False
                # X is pressed
                if event.key == pygame.K_x:
                    running = False

            if game_over == True:
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    # 'new game' button pressed
                    if mouse_on_button(mouse)
                        reset_board(board, window)
                        game_over = False
        
        mouse = pygame.mouse.get_pos()

        if game_over == True:
            draw_button(window, mouse)

        pygame.display.update()

main()
