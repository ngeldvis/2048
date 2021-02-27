import pygame
import random
from constants import *
# Contains the Board class which consists of the
# framework used to keep track of the current state 
# of the board along with all the calculations used
# when playing the game

START_VALS = [MULTIPLIER, MULTIPLIER * MULTIPLIER]

class Board:

    def __init__(self, num_blocks=STARTING_BLOCKS) -> None:
        self.board = [[0 for j in range(COLS)] for i in range(ROWS)]
        for i in range(num_blocks):
            self.add_block()

    def get_font_size(self, num) -> int:
        if num < 1000:
            return 70
        elif num < 10000:
            return 50
        elif num < 100000:
            return 25
        else:
            return 10

    def draw(self, window) -> None:
        block_width = (WIDTH - (W_BORDER_WEIGHT * (COLS+1))) / COLS
        block_height = (HEIGHT - (H_BORDER_WEIGHT * (ROWS+1))) / ROWS
        window.fill(COLORS['border'])

        for i in range(COLS):
            for j in range(ROWS):
                pygame.draw.rect(window, COLORS['bg'],
                    (i * block_width + i * W_BORDER_WEIGHT + W_BORDER_WEIGHT, j * block_height + j * H_BORDER_WEIGHT + H_BORDER_WEIGHT, block_width, block_height), border_radius=BLOCK_RADIUS)

        for i in range(COLS):
            for j in range(ROWS):
                val = self.board[j][i]
                if val != 0:


                    font_size = self.get_font_size(val)

                    font = pygame.font.SysFont(FONT, font_size)
                    text = font.render(str(val), True, WHITE)

                    x_offset = i * block_width + i * W_BORDER_WEIGHT + W_BORDER_WEIGHT
                    y_offset = j * block_height + j * H_BORDER_WEIGHT + H_BORDER_WEIGHT

                    rect = pygame.Rect(x_offset, y_offset, block_width, block_height)

                    pygame.draw.rect(window, BLOCK_COLORS[val], rect, border_radius=BLOCK_RADIUS)

                    text_placement = (
                        rect.width // 2 - text.get_rect().width // 2 + x_offset, 
                        rect.height // 2 - text.get_rect().height // 2 + y_offset
                    )

                    window.blit(text, text_placement)
    
    # returns true if there are no possible moves to make
    def no_moves(self) -> bool:
        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i][j] == 0:
                    return False
                if i > 0:
                    if self.board[i-1][j] == self.board[i][j]:
                        return False
                if i < ROWS-1:
                    if self.board[i+1][j] == self.board[i][j]:
                        return False
                if j > 0:
                    if self.board[i][j-1] == self.board[i][j]:
                        return False
                if j < COLS-1:
                    if self.board[i][j+1] == self.board[i][j]:
                        return False
        return True

    # returns true if all the spaces on the board are occupied
    def is_full(self) -> bool:
        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i][j] == 0:
                    return False
        return True

    def get_closest_left(self, x: int, y: int) -> list:
        for i in reversed(range(y)):
            if self.board[x][i] != 0:
                return [x, i]
        return [x, y]

    def shift_left(self) -> None:
        # print('shift left')
        for i in range(ROWS):
            for j in range(1, COLS):
                point = self.get_closest_left(i, j)
                if point == [i, j]:
                    self.board[i][0] = self.board[i][j]
                    self.board[i][j] = 0
                else:
                    x, y = point[0], point[1]
                    if self.board[x][y] == self.board[i][j]:
                        self.board[x][y] *= MULTIPLIER
                        self.board[i][j] = 0
                    elif y+1 != j:
                        self.board[x][y+1] = self.board[i][j]
                        self.board[i][j] = 0

    def get_closest_right(self, x: int, y: int) -> list:
        for i in range(y+1, COLS):
            if self.board[x][i] != 0:
                return [x, i]
        return [x, y]

    def shift_right(self) -> None:
        # print('shift right')
        for i in range(ROWS):
            for j in reversed(range(COLS-1)):
                point = self.get_closest_right(i, j)
                if point == [i, j]:
                    self.board[i][COLS-1] = self.board[i][j]
                    self.board[i][j] = 0
                else:
                    x, y = point[0], point[1]
                    if self.board[x][y] == self.board[i][j]:
                        self.board[x][y] *= MULTIPLIER
                        self.board[i][j] = 0
                    elif y-1 != j:
                        self.board[x][y-1] = self.board[i][j]
                        self.board[i][j] = 0
    
    def get_closest_up(self, x: int, y: int) -> list:
        for i in reversed(range(x)):
            if self.board[i][y] != 0:
                return [i, y]
        return [x, y]

    def shift_up(self) -> None:
        # print('shift up')
        for j in range(COLS):
            for i in range(1, ROWS):
                point = self.get_closest_up(i, j)
                if point == [i, j]:
                    self.board[0][j] = self.board[i][j]
                    self.board[i][j] = 0
                else:
                    x, y, = point[0], point[1]
                    if self.board[x][y] == self.board[i][j]:
                        self.board[x][y] *= MULTIPLIER
                        self.board[i][j] = 0
                    elif x+1 != i:
                        self.board[x+1][y] = self.board[i][j]
                        self.board[i][j] = 0

    def get_closest_down(self, x: int, y: int) -> list:
        for i in range(x+1, ROWS):
            if self.board[i][y] != 0:
                return [i, y]
        return [x, y]


    def shift_down(self) -> None:
        # print('shift down')
        for j in range(COLS):
            for i in reversed(range(ROWS-1)):
                point = self.get_closest_down(i, j)
                if point == [i, j]:
                    self.board[ROWS-1][j] = self.board[i][j]
                    self.board[i][j] = 0
                else:
                    x, y = point[0], point[1]
                    if self.board[x][y] == self.board[i][j]:
                        self.board[x][y] *= MULTIPLIER
                        self.board[i][j] = 0
                    elif x-1 != i:
                        self.board[x-1][y] = self.board[i][j]
                        self.board[i][j] = 0

    def add_block(self) -> None:
        while True:
            i = random.randint(0, ROWS-1)
            j = random.randint(0, COLS-1)
            if self.board[i][j] == 0:
                break
        self.board[i][j] = random.choice(START_VALS)
    
    def __repr__(self) -> str:
        return '\n'.join([''.join(['{:5}'.format(item) for item in row]) 
      for row in self.board])
