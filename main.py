import pygame
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

class Blocks(Enum):
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

    L_Block = (
        ((1, 0), (1, 1), (1, 2), (2, 2)),        # normal
        ((1, 1), (2, 1), (3, 1), (1, 2)),        # 1 x r | 3 x l
        ((1, 0), (2, 1), (3, 1), (1, 2)),        # 2 x r | 2 x l
        ((1, 1), (2, 1), (3, 1), (1, 2)),        # 3 x r | 1 x l
    )

# init:

pygame.init()

# LOAD IMAGES


# GLOBAL VARIABLES

screen_size = (1000, 1000)
game_rect = (600, 990)
borders = 5
# class


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


# MAIN


def main():
    root = pygame.display.set_mode(screen_size)                        # we make the window full screen
    root.fill(Color.Light_Grey.value)                                  # we make the background grey
    running = True
    layout_init(root)

    while running:

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                    return

                case _:
                    pass

        pygame.display.update()


if __name__ == '__main__':
    main()
