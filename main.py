import time
import copy
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
    T_Block = [
        [[0, 0], [1, 0], [2, 0], [1, 1]],        # normal
        [[1, 0], [1, 1], [1, 2], [2, 2]],        # 1 x r | 2 x l
        [[1, 1], [0, 2], [1, 2], [2, 2]],        # 2 x r | 2 x l
        [[0, 0], [0, 1], [1, 1], [0, 2]]         # 3 x r | 1 x l
    ]

    I_Block = [
        [[0, 1], [1, 1], [2, 1], [3, 1]],        # normal
        [[2, 0], [2, 1], [2, 2], [2, 3]],        # 1 x r | 2 x l
        [[0, 2], [1, 2], [2, 2], [3, 2]],        # 2 x r | 2 x l
        [[1, 0], [1, 1], [1, 2], [1, 3]]         # 3 x r | 1 x l
    ]

    Z1_Block = [
        [[0, 1], [1, 0], [1, 1], [2, 0]],        # normal
        [[1, 0], [1, 1], [2, 1], [2, 3]],        # 1 x r | 3 x l
        [[0, 1], [1, 0], [1, 1], [2, 0]],        # 2 x r | 2 x l
        [[1, 0], [1, 1], [2, 1], [2, 3]]         # 3 x r | 1 x l
    ]

    Z2_Block = [
        [[0, 0], [1, 0], [1, 1], [2, 1]],        # normal
        [[2, 0], [1, 1], [2, 1], [1, 3]],        # 1 x r | 3 x l
        [[0, 0], [1, 0], [1, 1], [2, 1]],        # 2 x r | 2 x l
        [[2, 0], [1, 1], [2, 1], [1, 3]]         # 3 x r | 1 x l
    ]

    Q_Block = [
        [[0, 0], [0, 1], [1, 0], [1, 1]],        # normal
        [[0, 0], [0, 1], [1, 0], [1, 1]],        # 1 x r | 3 x l
        [[0, 0], [0, 1], [1, 0], [1, 1]],        # 2 x r | 2 x l
        [[0, 0], [0, 1], [1, 0], [1, 1]]         # 3 x r | 1 x l
    ]

    L1_Block = [
        [[1, 0], [1, 1], [1, 2], [2, 2]],        # normal
        [[1, 1], [2, 1], [3, 1], [1, 2]],        # 1 x r | 3 x l
        [[1, 1], [2, 1], [2, 2], [2, 3]],        # 2 x r | 2 x l
        [[0, 2], [1, 2], [2, 2], [2, 1]],        # 3 x r | 1 x l
    ]

    L2_Block = [
        [[2, 0], [2, 1], [2, 2], [1, 2]],        # normal
        [[1, 2], [2, 2], [3, 2], [1, 1]],        # 1 x r | 3 x l
        [[1, 1], [2, 1], [1, 2], [1, 3]],        # 2 x r | 2 x l
        [[0, 1], [1, 1], [2, 1], [2, 2]],        # 3 x r | 1 x l
    ]


# Class of the Rectangles

class Rectangle:
    def __init__(self, root, x, y):
        self.is_full = False
        self.x = int(x * 60) + 5
        self.y = int(y * 60) + 5
        self.width = 60
        self.height = 60
        self.rect = (self.x, self.y, self.width, self.height)
        root.blit(blank_tile, self.rect)

    def draw(self, root, sprite, clear=False, falling=True):
        if falling:
            root.blit(sprite, (self.x, self.y))

        else:
            if clear:
                self.is_full = False
                root.blit(blank_tile, self.rect)
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
blank_tile = pygame.image.load('./resources/Blank_tile.png')

# GLOBAL VARIABLES

screen_size = (1000, 1030)
game_rect = (600, 1020)
borders = 5
running = True


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
    i = rnd.randint(0, 6)
    middle = [
        [[3, 0], [3, 0], [3, 0], [3, 0]],
        [[3, 0], [3, 0], [3, 0], [3, 0]],
        [[3, 0], [3, 0], [3, 0], [3, 0]],
        [[3, 0], [3, 0], [3, 0], [3, 0]]
    ]

    match i:
        case 0:
            block = copy.deepcopy(Block.Q_Block.value)
            color = yellow_tile
        case 1:
            block = copy.deepcopy(Block.I_Block.value)
            color = light_blue_tile
        case 2:
            block = copy.deepcopy(Block.T_Block.value)
            color = green_tile
        case 3:
            block = copy.deepcopy(Block.L1_Block.value)
            color = blue_tile
        case 4:
            block = copy.deepcopy(Block.L2_Block.value)
            color = orange_tile
        case 5:
            block = copy.deepcopy(Block.Z1_Block.value)
            color = red_tile
        case 6:
            block = copy.deepcopy(Block.Z2_Block.value)
            color = light_purple_tile
        case _:
            block = copy.deepcopy(Block.Q_Block.value)
            color = yellow_tile

    next_b = [block, color]
    return next_b


def engine(root, block, prev, recs, direction):
    global running
    co_block = block[0][direction[0]]
    i = len(co_block)
    try:
        for tile in co_block:
            if not recs[tile[0]][tile[1]].is_full:                      # we check if the tile below is full
                i -= 1
    except IndexError:
        for t in prev:                                             # we delete the previous block
            recs[t[0]][t[1]].draw(root, block[1], False, False)
        return True

    if prev is not None:
        if i == 0:                                                      # if so we make the block actually say 'full'
            for tile in prev:                                           # we delete the previous block
                recs[tile[0]][tile[1]].draw(root, block[1], True, False)
            for tile in co_block:
                recs[tile[0]][tile[1]].draw(root, block[1], False, True)
            return False

        else:                                                           # if it isn`t full we draw but not save the tile
            for tile in prev:                                           # we delete the previous block
                recs[tile[0]][tile[1]].draw(root, block[1], False, False)
            return True

    else:
        if i == 0:
            for tile in co_block:                                       # we draw every tile
                recs[tile[0]][tile[1]].draw(root, block[1], False, True)
            return False

        else:
            for tile in co_block:                                       # and draw the new block
                recs[tile[0]][tile[1]].draw(root, block[1], False, False)
                print('GAME OVER!!!')
                running = False
                return True


def move_block(block):
    bl = block[0]
    n_block = []
    for bn in bl:
        in_dir = []
        for tile in bn:
            tile[0] += 1
            tile[1] += 0
            in_dir.append(tile)
        n_block.append(in_dir)
    block[0] = n_block
    return block

# MAIN


def main():
    global running
    delay = 50
    root = pygame.display.set_mode(screen_size)                         # we make the window full screen
    root.fill(Color.Light_Grey.value)                                   # we make the background grey

    root, recs = layout_init(root)
    this_block = next_block()
    start_time = time.time()
    direction = [0, 0]
    prev_block = None
    n_block = next_block()
    while running:
        now_time = time.time()
        print(now_time - start_time)

        if now_time - start_time > 0.05:
            prev_block = copy.deepcopy(this_block[0][direction[1]])
            this_block = move_block(this_block)
            start_time = time.time()

        if engine(root, this_block, prev_block, recs, direction):       # if the block is placed we swap the
            prev_block = None
            direction[0] = direction[1]                                 # blocks ...
            this_block = n_block
            n_block = next_block()                                      # we get the next block

        # dsa

        for event in pygame.event.get():                                # we go over all events
            match event.type:                                           # and we use match|case on the events
                case pygame.QUIT:
                    return
                case pygame.KEYDOWN:                                    # we see if a key is pressed down
                    pass

                case _:                                                 # default case
                    pass

        pygame.display.update()


if __name__ == '__main__':
    main()
