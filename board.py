import pygame
import random
from constants import ROWS, COLS

START_VALS = [2, 4]

class Board:

    def __init__(self) -> None:
        self.board = [[0 for j in range(COLS)] for i in range(ROWS)]

    def draw(self, window: pygame.Surface) -> None:
        window.fill((255, 255, 255))
        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i][j] != 0:
                    pass
    
    def no_moves(self) -> bool:
        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i][j] == 0:
                    return False
                if i > 0:
                    if self.board[i-1][j] == self.board[i][j]:
                        return False
                if i < COLS-1:
                    if self.board[i+1][j] == self.board[i][j]:
                        return False
                if j > 0:
                    if self.board[i][j-1] == self.board[i][j]:
                        return False
                if j < ROWS-1:
                    if self.board[i][j+1] == self.board[i][j]:
                        return False

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
                        self.board[x][y] *= 2
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
                        self.board[x][y] *= 2
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
                        self.board[x][y] *= 2
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
                point = get_closest_down(i, j)
                if point == [i, j]:
                    self.board[ROWS-1][j] = self.board[i][j]
                    self.board[i][j] = 0
                else:
                    x, y = point[0], point[1]
                    if self.board[x][y] == self.board[i][j]:
                        self.board[x][y] *= 2
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
