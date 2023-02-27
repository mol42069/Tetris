import pygame
from enum import Enum
from PIL import Image


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
    white = 27
    blank = 28

class Buttons(Enum):
    try_again = 2
    try_again_hover = 3
    try_again_clicked = 4
    quit = 5
    quit_hover = 6
    quit_clicked = 7
    start = 8
    start_hover = 9
    start_clicked = 10
    records = 11
    records_hover = 12
    records_clicked = 13
    home = 14
    home_hover = 15
    home_clicked = 16
    back = 20
    back_hover = 21
    back_clicked = 22
    submit = 24
    submit_hover = 25
    submit_clicked = 26

class Screens(Enum):
    game_over = 0
    starting = 1
    next_block = 17
    score = 18
    leaderboard = 19
    leaderboard_enter = 23

def get_img(image):
    if not isinstance(image, Screens) and not isinstance(image, Buttons)\
            and not isinstance(image, Tiles):
        raise TypeError('the given Enum isn´t in the Enums')

    return img[image.value]

def change_color(color, name):
    image = Image.open("./resources/Tiles/White_tile.png")
    image = image.convert('RGB')

    d = image.getdata()
    new_img = []
    for item in d:
        if item == (255, 255, 255):
            new_img.append(color)
        else:
            new_img.append(item)
    image.putdata(new_img)
    image.save('./resources/Tiles/ColoredTiled/' + str(name) + '.png')

    new_sprite = pygame.image.load('./resources/Tiles/ColoredTiled/' + str(name) + '.png')

    return new_sprite

def load():
    global img

    img = [
        pygame.image.load('./resources/Screens/Game_Over.png'),                 # 0
        pygame.image.load('./resources/Screens/starting_screen.png'),           # 1
        pygame.image.load('./resources/Buttons/Try_Again.png'),                 # 2
        pygame.image.load('./resources/Buttons/Try_Again_hover.png'),           # 3
        pygame.image.load('./resources/Buttons/Try_Again_clicked.png'),         # 4
        pygame.image.load('./resources/Buttons/QUIT.png'),                      # 5
        pygame.image.load('./resources/Buttons/QUIT_hover.png'),                # 6
        pygame.image.load('./resources/Buttons/QUIT_clicked.png'),              # 7
        pygame.image.load('./resources/Buttons/start_button.png'),              # 8
        pygame.image.load('./resources/Buttons/start_button_hover.png'),        # 9
        pygame.image.load('./resources/Buttons/start_button_clicked.png'),      # 10
        pygame.image.load('./resources/Buttons/records.png'),                   # 11
        pygame.image.load('./resources/Buttons/records_hover.png'),             # 12
        pygame.image.load('./resources/Buttons/records_clicked.png'),           # 13
        pygame.image.load('./resources/Buttons/home.png'),                      # 14
        pygame.image.load('./resources/Buttons/home_hover.png'),                # 15
        pygame.image.load('./resources/Buttons/home_clicked.png'),              # 16
        pygame.image.load('./resources/Screens/next_block_screen.png'),         # 17
        pygame.image.load('./resources/Screens/score_screen.png'),              # 18
        pygame.image.load('./resources/Screens/Leaderboard.png'),               # 19
        pygame.image.load('./resources/Buttons/back.png'),                      # 20
        pygame.image.load('./resources/Buttons/back_hover.png'),                # 21
        pygame.image.load('./resources/Buttons/back_clicked.png'),              # 22
        pygame.image.load('./resources/Screens/leaderboard_enter.png'),         # 23
        pygame.image.load('./resources/Buttons/submit.png'),                    # 24
        pygame.image.load('./resources/Buttons/submit_hover.png'),              # 25
        pygame.image.load('./resources/Buttons/submit_clicked.png'),            # 26
        pygame.image.load('./resources/Tiles/White_tile.png'),                  # 27
        pygame.image.load('./resources/Tiles/Blank_tile.png'),                  # 28

    ]
