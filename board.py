import pygame
from constants import ROWS, COLS

class Board:

    def __init__(self) -> None:
        self.board = [[0 for j in range(COLS)] for i in range(ROWS)]

    def draw(self, window) -> None:
        window.fill((255, 255, 255))
        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i][j] != 0:
                    pass
    
    def no_moves() -> bool:
        for i in range(ROWS):
            for j in range(COLS):
                if(i > 0) {
                    if self.board[i-1][j] == self.board[i][j]:
                        return False
                }
                if(i < COLS-1) {
                    if self.board[i+1][j] == self.board[i][j]:
                        return False
                }
                if(j > 0) {
                    if self.board[j-1][j] == self.board[i][j]:
                        return False
                }
                if(j < ROWS-1) {
                    if self.board[j+1][j] == self.board[i][j]:
                        return False
                }
        return True

    def shift_left() -> None:
        pass

    def shift_right() -> None:
        pass
    
    def shift_up() -> None:
        pass
    
    def shift_down() -> None:
        pass