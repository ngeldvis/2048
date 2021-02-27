# Contains all the constants used in and by the game

WIDTH, HEIGHT = 700, 700
ROWS, COLS = 4, 4
MULTIPLIER = 2
WIDTH_PERCENT = 1.5
BLOCK_RADIUS = 15
H_BORDER_WEIGHT = HEIGHT * WIDTH_PERCENT / 100
W_BORDER_WEIGHT = WIDTH * WIDTH_PERCENT / 100
STARTING_BLOCKS = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

COLORS = {
    'bg' : (204, 192, 179),
    'border' : (187, 173, 160)
}

BLOCK_COLORS = {
    MULTIPLIER ** 1  : (238, 228, 218),
    MULTIPLIER ** 2  : (237, 224, 200),
    MULTIPLIER ** 3  : (242, 177, 121),
    MULTIPLIER ** 4  : (245, 149,  99),
    MULTIPLIER ** 5  : (246, 124,  95),
    MULTIPLIER ** 6  : (246,  94,  59),
    MULTIPLIER ** 7  : (237, 207, 114),
    MULTIPLIER ** 8  : (237, 204,  97),
    MULTIPLIER ** 9  : (237, 200,  80),
    MULTIPLIER ** 10 : (237, 197,  63),
    MULTIPLIER ** 11 : (237, 194,  46),
    MULTIPLIER ** 12 : ( 62,  57,  51),
    MULTIPLIER ** 13 : (123, 235, 110),
    MULTIPLIER ** 14 : ( 86, 222,  95),
    MULTIPLIER ** 15 : ( 63, 222, 166),
    MULTIPLIER ** 16 : ( 51, 222, 214),
    MULTIPLIER ** 17 : ( 43, 200, 227),
    MULTIPLIER ** 18 : ( 39, 177, 245),
    MULTIPLIER ** 19 : ( 29, 112, 245),
    MULTIPLIER ** 20 : ( 63,  95, 245)
}