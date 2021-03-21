import pygame
import random
import copy
from constants import *

# Contains the Board class which consists of the
# framework used to keep track of the current state 
# of the board along with all the calculations used
# when playing the game

START_VALS = [MULTIPLIER, MULTIPLIER * MULTIPLIER]

class Board:

    # constructor
    def __init__(self, num_blocks: int = STARTING_BLOCKS) -> None:
        self.board = [[0 for j in range(COLS)] for i in range(ROWS)]
        for i in range(num_blocks):
            self.add_block()

    # draws the background of the game window
    def draw_bg(self, window: pygame.Surface, block_width: int, block_height: int) -> None:
        window.fill(COLORS['border'])
        for i in range(COLS):
            for j in range(ROWS):
                x_offset = i * block_width + i * W_BORDER_WEIGHT + W_BORDER_WEIGHT
                y_offset = j * block_height + j * H_BORDER_WEIGHT + H_BORDER_WEIGHT
                rect = (x_offset, y_offset, block_width, block_height)
                pygame.draw.rect(window, COLORS['bg'], rect, border_radius=BLOCK_RADIUS)

    # get the font size based on the value of the block
    def get_font_size(self, num: int) -> int:
        if num < 100:
            return 60
        if num < 1000:
            return 55
        elif num < 10000:
            return 40
        elif num < 100000:
            return 25
        return 10
    
    # get the font color based on the value of the block
    def get_font_color(self, num: int) -> tuple:
        if num <= MULTIPLIER ** 2:
            return COLORS['dark_text']
        return WHITE

    #draws the text of a block onto the screen
    def draw_text(self, window: pygame.Surface, rect: pygame.Rect, val: int):
        font_size = self.get_font_size(val)
        font_color = self.get_font_color(val)
        font = pygame.font.Font(FONT, font_size)
        text = font.render(str(val), True, font_color)
        text_x = rect.center[0] - text.get_rect().width // 2
        text_y = rect.center[1] - text.get_rect().height // 2 - 5
        text_placement = (text_x, text_y)
        window.blit(text, text_placement)

    # draw all the blocks on the board
    def draw_blocks(self, window: pygame.Surface, block_width: int, block_height: int) -> None:
        for i in range(COLS):
            for j in range(ROWS):
                val = self.board[j][i]
                if val != 0:
                    x_offset = i * block_width + i * W_BORDER_WEIGHT + W_BORDER_WEIGHT
                    y_offset = j * block_height + j * H_BORDER_WEIGHT + H_BORDER_WEIGHT
                    rect = pygame.Rect(x_offset, y_offset, block_width, block_height)
                    pygame.draw.rect(window, BLOCK_COLORS[val], rect, border_radius=BLOCK_RADIUS)
                    if B_TEXT == True: self.draw_text(window, rect, val)

    # draw the board on the game window
    def draw(self, window: pygame.Surface) -> None:
        block_width = (WIDTH - (W_BORDER_WEIGHT * (COLS+1))) / COLS
        block_height = (HEIGHT - (H_BORDER_WEIGHT * (ROWS+1))) / ROWS
        self.draw_bg(window, block_width, block_height)
        self.draw_blocks(window, block_width, block_height)
        
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

    #returns true if all the spaces on the board are occupied 
    def is_full(self) -> bool:
        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i][j] == 0:
                    return False
        return True

    # get the closest block to the left of a given block
    # returns the coordinates of the block found or the given block if no block found
    def get_closest_left(self, x: int, y: int, board: list) -> list:
        for i in reversed(range(y)):
            if board[x][i] != 0:
                return [x, i]
        return [x, y]

    # shift the contents of the board to the left combining blocks of the same value
    def shift_left(self) -> None:
        # print('shift left')
        new_board = copy.deepcopy(self.board)
        merged_points = []
        for i in range(ROWS):
            for j in range(1, COLS):
                point = self.get_closest_left(i, j, new_board)
                if point == [i, j]:
                    new_board[i][0] = new_board[i][j]
                    new_board[i][j] = 0
                else:
                    x, y = point[0], point[1]
                    if new_board[x][y] == new_board[i][j] and (x, y) not in merged_points:
                        new_board[x][y] *= MULTIPLIER
                        merged_points.append((x, y))
                        new_board[i][j] = 0
                    elif y+1 != j:
                        new_board[x][y+1] = new_board[i][j]
                        new_board[i][j] = 0
        if new_board != self.board:
            self.board = new_board
            return 1
        return 0

    # get the closest block to the right of a given block
    # returns the coordinates of the block found or the given block if no block found
    def get_closest_right(self, x: int, y: int, board: list) -> list:
        for i in range(y+1, COLS):
            if board[x][i] != 0:
                return [x, i]
        return [x, y]

    # shift the contents of the board to the right combining blocks of the same value
    def shift_right(self) -> None:
        # print('shift right')
        new_board = copy.deepcopy(self.board)
        merged_points = []
        for i in range(ROWS):
            for j in reversed(range(COLS-1)):
                point = self.get_closest_right(i, j, new_board)
                if point == [i, j]:
                    new_board[i][COLS-1] = new_board[i][j]
                    new_board[i][j] = 0
                else:
                    x, y = point[0], point[1]
                    if new_board[x][y] == new_board[i][j] and (x, y) not in merged_points:
                        new_board[x][y] *= MULTIPLIER
                        merged_points.append((x, y))
                        new_board[i][j] = 0
                    elif y-1 != j:
                        new_board[x][y-1] = new_board[i][j]
                        new_board[i][j] = 0
        
        if new_board != self.board:
            self.board = new_board
            return 1
        return 0
    
    # get the closest block closeset above of a given block
    # returns the coordinates of the block found or the given block if no block found
    def get_closest_up(self, x: int, y: int, board: list) -> list:
        for i in reversed(range(x)):
            if board[i][y] != 0:
                return [i, y]
        return [x, y]

    # shift the contents of the board up combining blocks of the same value
    def shift_up(self) -> int:
        # print('shift up')
        new_board = copy.deepcopy(self.board)
        merged_points = []
        for j in range(COLS):
            for i in range(1, ROWS):
                point = self.get_closest_up(i, j, new_board)
                if point == [i, j]:
                    new_board[0][j] = new_board[i][j]
                    new_board[i][j] = 0
                else:
                    x, y, = point[0], point[1]
                    if new_board[x][y] == new_board[i][j] and (x, y) not in merged_points:
                        new_board[x][y] *= MULTIPLIER
                        merged_points.append((x, y))
                        new_board[i][j] = 0
                    elif x+1 != i:
                        new_board[x+1][y] = new_board[i][j]
                        new_board[i][j] = 0

        if new_board != self.board:
            self.board = new_board
            return 1
        return 0

    # get the closest block closeset below of a given block
    # returns the coordinates of the block found or the given block if no block found
    def get_closest_down(self, x: int, y: int, board: list) -> list:
        for i in range(x+1, ROWS):
            if board[i][y] != 0:
                return [i, y]
        return [x, y]

    # shift the contents of the board down combining blocks of the same value
    def shift_down(self) -> None:
        # print('shift down')
        new_board = copy.deepcopy(self.board)
        merged_points = []
        for j in range(COLS):
            for i in reversed(range(ROWS-1)):
                point = self.get_closest_down(i, j, new_board)
                if point == [i, j]:
                    new_board[ROWS-1][j] = new_board[i][j]
                    new_board[i][j] = 0
                else:
                    x, y = point[0], point[1]
                    if new_board[x][y] == new_board[i][j] and (x, y) not in merged_points:
                        new_board[x][y] *= MULTIPLIER
                        merged_points.append((x, y))
                        new_board[i][j] = 0
                    elif x-1 != i:
                        new_board[x-1][y] = new_board[i][j]
                        new_board[i][j] = 0

        if new_board != self.board:
            self.board = new_board
            return 1
        return 0

    # add a new block to the board at a random free position
    def add_block(self) -> None:
        while True:
            i = random.randint(0, ROWS-1)
            j = random.randint(0, COLS-1)
            if self.board[i][j] == 0:
                break
        self.board[i][j] = random.choice(START_VALS)

    # clear the board and add 'num_blocks' to the newly cleared board
    def clear(self, num_blocks: int = STARTING_BLOCKS) -> None:
        self.board = [[0 for j in range(COLS)] for i in range(ROWS)]
        for i in range(num_blocks):
            self.add_block()
    
    # representation string for printing the Board object
    def __repr__(self) -> str:
        return '\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in self.board])

    # equal condition to check if two boards are eqaul
    def __eq__(self, board: list):
        return self.board == board
