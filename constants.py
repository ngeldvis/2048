# Contains all the constants used in and by the game

WIDTH, HEIGHT = 500, 500 # default 500, 500
ROWS, COLS = 4, 4 # default 4, 4
MULTIPLIER = 2 # default 2
STARTING_BLOCKS = 2 # default 2
NEW_BLOCKS_PER_MOVE = 1 # default 1
NEW_BLOCK_DELAY = 0 # default 0.15 seconds

# GUI

BLOCK_RADIUS = 5 # default 5
BORDER_PERCENT = 3 # default 3
H_BORDER_WEIGHT = HEIGHT * BORDER_PERCENT / 100
W_BORDER_WEIGHT = WIDTH * BORDER_PERCENT / 100
B_TEXT = True # default True
FONT = 'rsc/ClearSans-Bold.ttf'

GAME_OVER_POS_W = WIDTH // 2
GAME_OVER_POS_H = HEIGHT // 3
FADE_TIME = 0.05 # seconds
FADE_ALPHA = 180

RESTART_BUTTON_POS_W = WIDTH // 2
RESTART_BUTTON_POS_H = HEIGHT * 2 // 3
RESTART_BUTTON_WIDTH = 200
RESTART_BUTTON_HEIGHT = 60


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
    'bg' : (205, 193, 180),
    'border' : (187, 173, 160),
    'dark_text' : (119, 110, 101),
    'start_screen' : (250, 248, 239, 180)
}

BLOCK_COLORS = {
    MULTIPLIER ** 1  : (238, 228, 218),
    MULTIPLIER ** 2  : (238, 225, 200),
    MULTIPLIER ** 3  : (243, 178, 122),
    MULTIPLIER ** 4  : (246, 150, 100),
    MULTIPLIER ** 5  : (247, 125,  97),
    MULTIPLIER ** 6  : (247,  98,  61),
    MULTIPLIER ** 7  : (237, 208, 115),
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
