import pygame
import random as rnd
from enum import Enum


# Colors:
class Color(Enum):
    Black = (0, 0, 0)
    White = (255, 255, 255)
    Grey = (50, 50, 50)
    Light_Grey = (140, 140, 140)
    Dark_Grey = (15, 15, 15)
    Yellow = (255, 255, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)
    Red = (255, 0, 0)


# Blocks:

class Block(Enum):
    T_Block = (
        ((0, 0), (1, 0), (2, 0), (1, 1)),        # normal
        ((1, 0), (1, 1), (1, 2), (2, 2)),        # 1 x r | 2 x l
        ((1, 1), (0, 2), (1, 2), (2, 2)),        # 2 x r | 2 x l
        ((0, 0), (0, 1), (1, 1), (0, 2))         # 3 x r | 1 x l
    )

    I_Block = (
        ((0, 1), (1, 1), (2, 1), (3, 1)),        # normal
        ((2, 0), (2, 1), (2, 2), (2, 3)),        # 1 x r | 2 x l
        ((0, 2), (1, 2), (2, 2), (3, 2)),        # 2 x r | 2 x l
        ((1, 0), (1, 1), (1, 2), (1, 3))         # 3 x r | 1 x l
    )

    Z1_Block = (
        ((0, 1), (1, 0), (1, 1), (2, 0)),        # normal
        ((1, 0), (1, 1), (2, 1), (2, 3)),        # 1 x r | 3 x l
        ((0, 1), (1, 0), (1, 1), (2, 0)),        # 2 x r | 2 x l
        ((1, 0), (1, 1), (2, 1), (2, 3))         # 3 x r | 1 x l
    )

    Z2_Block = (
        ((0, 0), (1, 0), (1, 1), (2, 1)),        # normal
        ((2, 0), (1, 1), (2, 1), (1, 3)),        # 1 x r | 3 x l
        ((0, 0), (1, 0), (1, 1), (2, 1)),        # 2 x r | 2 x l
        ((2, 0), (1, 1), (2, 1), (1, 3))         # 3 x r | 1 x l
    )

    Q_Block = (
        ((0, 0), (0, 1), (1, 0), (1, 1)),        # normal
        ((0, 0), (0, 1), (1, 0), (1, 1)),        # 1 x r | 3 x l
        ((0, 0), (0, 1), (1, 0), (1, 1)),        # 2 x r | 2 x l
        ((0, 0), (0, 1), (1, 0), (1, 1))         # 3 x r | 1 x l
    )

    L1_Block = (
        ((1, 0), (1, 1), (1, 2), (2, 2)),        # normal
        ((1, 1), (2, 1), (3, 1), (1, 2)),        # 1 x r | 3 x l
        ((1, 1), (2, 1), (2, 2), (2, 3)),        # 2 x r | 2 x l
        ((0, 2), (1, 2), (2, 2), (2, 1)),        # 3 x r | 1 x l
    )

    L2_Block = (
        ((2, 0), (2, 1), (2, 2), (1, 2)),        # normal
        ((1, 2), (2, 2), (3, 2), (1, 1)),        # 1 x r | 3 x l
        ((1, 1), (2, 1), (1, 2), (1, 3)),        # 2 x r | 2 x l
        ((0, 1), (1, 1), (2, 1), (2, 2)),        # 3 x r | 1 x l
    )


# Class of the Rectangles

class Rectangle:
    def __init__(self, root, x, y):
        self.is_full = False
        self.x = int(x * 60 + 1) + 5
        self.y = int(y * 60 + 1) + 5
        self.width = 58
        self.height = 58
        self.rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(root, Color.Black.value, self.rect)

    def draw(self, root, sprite, clear=False, falling=True):
        if falling:
            root.blit(sprite, (self.x, self.y))

        else:
            if clear:
                self.is_full = False
                pygame.draw.rect(root, Color.Black.value, self.rect)
            else:
                self.is_full = True


# init:

pygame.init()

# LOAD IMAGES

blue_tile = pygame.image.load('./resources/Blue_tile.png')
green_tile = pygame.image.load('./resources/Green_tile.png')
light_purple_tile = pygame.image.load('./resources/light_purple_tile.png')
light_blue_tile = pygame.image.load('./resources/light_Blue_tile.png')
red_tile = pygame.image.load('./resources/Red_tile.png')
yellow_tile = pygame.image.load('./resources/Yellow_tile.png')
orange_tile = pygame.image.load('./resources/Orange_tile.png')

# GLOBAL VARIABLES

screen_size = (1000, 1030)
game_rect = (600, 1020)
borders = 5


# init for game layout

def layout_init(root):

    # Game Panel/middle Panel:

    x = borders
    y = (screen_size[1] - game_rect[1]) / 2
    rect = pygame.Rect((x, y, game_rect[0], game_rect[1]))
    pygame.draw.rect(root, Color.Dark_Grey.value, rect)

    # Right Grey Panel:

    y = borders
    width = (screen_size[0] - game_rect[0]) - (borders * 3)
    height = screen_size[1] - (borders * 2)
    x = game_rect[0] + (borders * 2)
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(root, Color.Grey.value, rect)

    # we draw the rectangles in the Game Panel

    col = int(game_rect[0] / 60)
    row = int(game_rect[1] / 60)
    recs = []
    for y in range(row):
        line = []
        for x in range(col):
            line.append(Rectangle(root, x, y))
        recs.append(line)

    return root, recs


def next_block():
    i = rnd.randint(0, 7)

    match i:
        case 0:
            block = Block.Q_Block
            color = yellow_tile
        case 1:
            block = Block.I_Block
            color = light_blue_tile
        case 2:
            block = Block.T_Block
            color = green_tile
        case 3:
            block = Block.L1_Block
            color = blue_tile
        case 4:
            block = Block.L2_Block
            color = orange_tile
        case 5:
            block = Block.Z1_Block
            color = red_tile
        case 6:
            block = Block.Z2_Block
            color = light_purple_tile
        case _:
            block = Block.Q_Block
            color = yellow_tile
    next_b = [block, color]
    return next_b


def engine(root, block, prev, recs, direction):
    co_block = block[0][direction[0]]
    if recs[co_block[1]][co_block[0]].is_full:
        co_block = prev[0][direction[1]]
        for tile in co_block:
            recs[tile[0]][tile[1]].draw(root, block[1], False, False)

    else:
        for tile in prev[0][direction[1]]:
            recs[tile[0]][tile[1]].draw(root, block[1], True)
        for tile in co_block:
            recs[tile[0]][tile[1]].draw(root, block[1], False, True)

    return

# MAIN


def main():
    delay = 50
    root = pygame.display.set_mode(screen_size)                         # we make the window full screen
    root.fill(Color.Light_Grey.value)                                   # we make the background grey
    running = True
    root, recs = layout_init(root)
    this_block = next_block()

    while running:
        n_block = next_block()                                          # we get the next block
        pygame.time.delay(delay)

        # dsa

        for event in pygame.event.get():                                # we go over all events
            match event.type:                                           # and we use match|case on the events
                case pygame.QUIT:
                    return
                case pygame.KEYDOWN:                                    # we see if a key is pressed down
                    pass

                case _:                                                 # default case
                    pass

        this_block = n_block
        pygame.display.update()


if __name__ == '__main__':
    main()
