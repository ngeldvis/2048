import pygame

from block import Block
from board import Board
from constants import WIDTH, HEIGHT, WHITE

#
#
#
#
#

FPS = 60

def set_window():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('2048')
    window.fill(WHITE)
    return window

def main():
    pygame.init()
    clock = pygame.time.Clock()

    window = set_window()

    board = Board()
    board.draw(window)
    pygame.display.update()

    print(board.board)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.shift_left()
                if event.key == pygame.K_RIGHT:
                    board.shift_right()
                if event.key == pygame.K_UP:
                    board.shift_up()
                if event.key == pygame.K_DOWN:
                    board.shift_down()
        if board.no_moves():
            running = False
            print('No more moves\n')

main()