# Contains all the constants used in and by the game

WIDTH, HEIGHT = 500, 500
ROWS, COLS = 4, 4
MULTIPLIER = 2
STARTING_BLOCKS = 2

# GUI

BLOCK_RADIUS = 5
BORDER_PERCENT = 3
H_BORDER_WEIGHT = HEIGHT * BORDER_PERCENT / 100
W_BORDER_WEIGHT = WIDTH * BORDER_PERCENT / 100
FONT = 'JetBrains Mono'

#COLORS

WHITE   = (255, 255, 255)
BLACK   = (  0,   0,   0)
RED     = (255, 255, 255)
ORANGE  = (255, 128,   0)
YELLOW  = (255, 255,   0)
LIME    = (128, 255,   0)
GREEN   = (  0, 255,   0)
TEAL    = (  0, 255, 128)
CYAN    = (  0, 255, 255)
L_BLUE  = (  0, 128, 255)
BLUE    = (  0,   0, 255)
PURPLE  = (128,   0, 255)
MAGENTA = (255,   0, 255)
P_RED   = (255,   0, 128)

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
