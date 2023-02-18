import pygame
from enum import Enum

img = []

class Colors(Enum):
    Black = (0, 0, 0)
    White = (255, 255, 255)
    Grey = (50, 50, 50)
    Light_Grey = (140, 140, 140)
    Dark_Grey = (15, 15, 15)
    Yellow = (255, 255, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)
    Red = (255, 0, 0)

class Tiles(Enum):
    blue = 0
    green = 1
    light_purple = 2
    light_blue = 3
    red = 4
    yellow = 5
    orange = 6
    blank = 7

class Buttons(Enum):
    try_again = 10
    try_again_hover = 11
    try_again_clicked = 12
    quit = 13
    quit_hover = 14
    quit_clicked = 15
    start = 16
    start_hover = 17
    start_clicked = 18
    records = 19
    records_hover = 20
    records_clicked = 21
    home = 22
    home_hover = 23
    home_clicked = 24

class Screens(Enum):
    game_over = 8
    starting = 9
    next_block = 25
    score = 26

def get_img(image):
    if not isinstance(image, Screens) and not isinstance(image, Buttons)\
            and not isinstance(image, Tiles):
        raise TypeError('the given Enum isn´t in the "Screens" Enum')

    return img[image.value]

def load():
    global img

    img = [
        pygame.image.load('./resources/Tiles/Blue_tile.png'),                   # 0
        pygame.image.load('./resources/Tiles/Green_tile.png'),                  # 1
        pygame.image.load('./resources/Tiles/light_purple_tile.png'),           # 2
        pygame.image.load('./resources/Tiles/light_Blue_tile.png'),             # 3
        pygame.image.load('./resources/Tiles/Red_tile.png'),                    # 4
        pygame.image.load('./resources/Tiles/Yellow_tile.png'),                 # 5
        pygame.image.load('./resources/Tiles/Orange_tile.png'),                 # 6
        pygame.image.load('./resources/Tiles/Blank_tile.png'),                  # 7
        pygame.image.load('./resources/Screens/Game_Over.png'),                 # 8
        pygame.image.load('./resources/Screens/starting_screen.png'),           # 9
        pygame.image.load('./resources/Buttons/Try_Again.png'),                 # 10
        pygame.image.load('./resources/Buttons/Try_Again_hover.png'),           # 11
        pygame.image.load('./resources/Buttons/Try_Again_clicked.png'),         # 12
        pygame.image.load('./resources/Buttons/QUIT.png'),                      # 13
        pygame.image.load('./resources/Buttons/QUIT_hover.png'),                # 14
        pygame.image.load('./resources/Buttons/QUIT_clicked.png'),              # 15
        pygame.image.load('./resources/Buttons/start_button.png'),              # 16
        pygame.image.load('./resources/Buttons/start_button_hover.png'),        # 17
        pygame.image.load('./resources/Buttons/start_button_clicked.png'),      # 18
        pygame.image.load('./resources/Buttons/records.png'),                   # 19
        pygame.image.load('./resources/Buttons/records_hover.png'),             # 20
        pygame.image.load('./resources/Buttons/records_clicked.png'),           # 21
        pygame.image.load('./resources/Buttons/home.png'),                      # 22
        pygame.image.load('./resources/Buttons/home_hover.png'),                # 23
        pygame.image.load('./resources/Buttons/home_clicked.png'),              # 24
        pygame.image.load('./resources/Screens/next_block_screen.png'),         # 25
        pygame.image.load('./resources/Screens/score_screen.png')               # 26

    ]
