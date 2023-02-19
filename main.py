import time
import copy
import pygame
from load import load_img
from load import ls_records as lsr
import random as rnd
from enum import Enum

# Blocks:

class Block(Enum):
    T_Block = [
        [[0, 4], [1, 4], [2, 0 + 4], [1, 1 + 4]],               # normal
        [[1, 4], [1, 5], [1, 2 + 4], [0, 1 + 4]],               # 1 x r | 2 x l
        [[1, 5], [0, 6], [1, 2 + 4], [2, 2 + 4]],               # 2 x r | 2 x l
        [[0, 4], [0, 5], [1, 1 + 4], [0, 2 + 4]]                # 3 x r | 1 x l
    ]

    I_Block = [
        [[0, 1 + 4], [1, 1 + 4], [2, 1 + 4], [3, 1 + 4]],        # normal
        [[2, 0 + 4], [2, 1 + 4], [2, 2 + 4], [2, 3 + 4]],        # 1 x r | 2 x l
        [[0, 2 + 4], [1, 2 + 4], [2, 2 + 4], [3, 2 + 4]],        # 2 x r | 2 x l
        [[1, 0 + 4], [1, 1 + 4], [1, 2 + 4], [1, 3 + 4]]         # 3 x r | 1 x l
    ]

    Z1_Block = [
        [[0, 1 + 4], [1, 0 + 4], [1, 1 + 4], [2, 0 + 4]],        # normal
        [[1, 0 + 4], [1, 1 + 4], [2, 1 + 4], [2, 2 + 4]],        # 1 x r | 3 x l
        [[0, 1 + 4], [1, 0 + 4], [1, 1 + 4], [2, 0 + 4]],        # 2 x r | 2 x l
        [[1, 0 + 4], [1, 1 + 4], [2, 1 + 4], [2, 2 + 4]]         # 3 x r | 1 x l
    ]

    Z2_Block = [
        [[0, 0 + 4], [1, 0 + 4], [1, 1 + 4], [2, 1 + 4]],        # normal
        [[2, 0 + 4], [1, 1 + 4], [2, 1 + 4], [1, 2 + 4]],        # 1 x r | 3 x l
        [[0, 0 + 4], [1, 0 + 4], [1, 1 + 4], [2, 1 + 4]],        # 2 x r | 2 x l
        [[2, 0 + 4], [1, 1 + 4], [2, 1 + 4], [1, 2 + 4]]         # 3 x r | 1 x l
    ]

    Q_Block = [
        [[0, 0 + 4], [0, 1 + 4], [1, 0 + 4], [1, 1 + 4]],        # normal
        [[0, 0 + 4], [0, 1 + 4], [1, 0 + 4], [1, 1 + 4]],        # 1 x r | 3 x l
        [[0, 0 + 4], [0, 1 + 4], [1, 0 + 4], [1, 1 + 4]],        # 2 x r | 2 x l
        [[0, 0 + 4], [0, 1 + 4], [1, 0 + 4], [1, 1 + 4]]         # 3 x r | 1 x l
    ]

    L1_Block = [
        [[1, 0 + 4], [1, 1 + 4], [1, 2 + 4], [2, 2 + 4]],        # normal
        [[1, 1 + 4], [2, 1 + 4], [3, 1 + 4], [1, 2 + 4]],        # 1 x r | 3 x l
        [[1, 1 + 4], [2, 1 + 4], [2, 2 + 4], [2, 3 + 4]],        # 2 x r | 2 x l
        [[0, 2 + 4], [1, 2 + 4], [2, 2 + 4], [2, 1 + 4]],        # 3 x r | 1 x l
    ]

    L2_Block = [
        [[2, 0 + 4], [2, 1 + 4], [2, 2 + 4], [1, 2 + 4]],        # normal
        [[1, 2 + 4], [2, 2 + 4], [3, 2 + 4], [1, 1 + 4]],        # 1 x r | 3 x l
        [[1, 1 + 4], [2, 1 + 4], [1, 2 + 4], [1, 3 + 4]],        # 2 x r | 2 x l
        [[0, 1 + 4], [1, 1 + 4], [2, 1 + 4], [2, 2 + 4]],        # 3 x r | 1 x l
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
        root.blit(load_img.get_img(load_img.Tiles.blank), self.rect)
        self.sprite = load_img.get_img(load_img.Tiles.yellow)

    def draw(self, root, sprite, clear=False, falling=True):
        if not self.is_full:
            if falling:
                root.blit(sprite, (self.x, self.y))
            else:
                if clear:
                    self.is_full = False
                    root.blit(load_img.get_img(load_img.Tiles.blank), self.rect)
                else:
                    self.is_full = True
                    root.blit(sprite, (self.x, self.y))
                    self.sprite = sprite
        return root

    def clear(self, root):
        self.is_full = False
        root.blit(load_img.get_img(load_img.Tiles.blank), self.rect)
        return root, self.sprite


class NextRectangle:
    def __init__(self, root, x, y):
        self.x = int(x * 60) + 5 + 635
        self.y = int(y * 60) + 5 + 137
        self.width = 60
        self.height = 60
        self.rect = (self.x, self.y, self.width, self.height)
        root.blit(load_img.get_img(load_img.Tiles.blank), self.rect)

    def draw(self, root, sprite):
        root.blit(sprite, self.rect)
        return root

    def clear(self, root):
        root.blit(load_img.get_img(load_img.Tiles.blank), self.rect)
        return root
# init:

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)

# LOAD IMAGES

load_img.load()

# GLOBAL VARIABLES

screen_size = (1000, 1030)
game_rect = (600, 1020)
borders = 5
running = True
recs = []
nb_disp = []
first_start = True
score = 0
last_score = 0
in_a_row = 0
delay = 0.3

# init for game layout


def layout_init(root):

    # Game Panel/middle Panel:
    global recs

    x = borders
    y = (screen_size[1] - game_rect[1]) / 2
    rect = pygame.Rect((x, y, game_rect[0], game_rect[1]))
    pygame.draw.rect(root, load_img.Colors.Dark_Grey.value, rect)

    # Right Grey Panel:

    y = borders
    width = (screen_size[0] - game_rect[0]) - (borders * 3)
    height = screen_size[1] - (borders * 2)
    x = game_rect[0] + (borders * 2)
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(root, load_img.Colors.Grey.value, rect)

    # we draw the rectangles in the Game Panel

    col = int(game_rect[0] / 60)
    row = int(game_rect[1] / 60)
    for y in range(row):
        line = []
        for x in range(col):
            line.append(Rectangle(root, x, y))
        recs.append(line)

    return root


def next_block(root):
    i = rnd.randint(0, 6)
    match i:
        case 0:
            block = copy.deepcopy(Block.Q_Block.value)
            color = load_img.get_img(load_img.Tiles.yellow)
        case 1:
            block = copy.deepcopy(Block.I_Block.value)
            color = load_img.get_img(load_img.Tiles.light_blue)
        case 2:
            block = copy.deepcopy(Block.T_Block.value)
            color = load_img.get_img(load_img.Tiles.green)
        case 3:
            block = copy.deepcopy(Block.L1_Block.value)
            color = load_img.get_img(load_img.Tiles.blue)
        case 4:
            block = copy.deepcopy(Block.L2_Block.value)
            color = load_img.get_img(load_img.Tiles.orange)
        case 5:
            block = copy.deepcopy(Block.Z1_Block.value)
            color = load_img.get_img(load_img.Tiles.red)
        case 6:
            block = copy.deepcopy(Block.Z2_Block.value)
            color = load_img.get_img(load_img.Tiles.light_purple)
        case _:
            block = copy.deepcopy(Block.Q_Block.value)
            color = load_img.get_img(load_img.Tiles.yellow)

    next_b = [block, color]

    root = next_block_display(root, next_b)

    return root, next_b


def check_possible(block, direction):
    global recs
    try:
        this = block[0][direction[0]]
    except IndexError:
        return True
    for tile in this:
        if tile[0] < 0 or tile[0] > 16 or tile[1] < 0 or tile[1] > 9:
            return True
        try:
            if recs[tile[0]][tile[1]].is_full:
                return True
        except IndexError:
            return True

    return False


def engine(root, block, prev, direction):
    global running, recs
    co_block = block[0][direction[0]]
    i = len(co_block)
    set_block = False
    for rec in recs:
        for r in rec:
            if not r.is_full:
                r.draw(root, load_img.get_img(load_img.Tiles.blank), True, False)

    for tile in co_block:
        if tile[0] > 16:
            set_block = True

    if set_block:
        for tile in prev:
            recs[tile[0]][tile[1]].draw(root, block[1], False, False)
        return True

    try:
        for tile in co_block:
            if not recs[tile[0]][tile[1]].is_full:                     # we check if the tile below is full
                i -= 1

    except IndexError:
        for t in prev:                                                 # we delete the previous block
            recs[t[0]][t[1]].draw(root, block[1], False, False)
        return True

    if prev is not None:
        if i == 0:                                                     # if so we make the block actually say 'full'
            for tile in prev:                                          # we delete the previous block
                recs[tile[0]][tile[1]].draw(root, block[1], True, False)
            for tile in co_block:
                recs[tile[0]][tile[1]].draw(root, block[1], False, True)
            return False

        else:                                                       # if it isn`t full we draw but not save the tile
            for tile in prev:                                       # we delete the previous block
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
                game_over_state(root)
                running = False
                return True


def move_block(block):
    bl = block[0]
    n_block = []
    for bn in bl:
        in_dir = []
        for tile in bn:                                                 # we move blocks downwards
            tile[0] += 1
            tile[1] += 0
            in_dir.append(tile)
        n_block.append(in_dir)
    block[0] = n_block
    return block


def lr_movement(block, left, direction):
    bl = copy.deepcopy(block[0])
    n_block = []
    for bn in bl:
        in_dir = []
        for tile in bn:
            if left:
                tile[1] -= 1
            else:
                tile[1] += 1
            in_dir.append(tile)
        n_block.append(in_dir)
    block_moved = [n_block, block[1]]
    if check_possible(block_moved, direction):
        return block
    else:
        return block_moved


def check_line():
    global recs

    for x, line in enumerate(reversed(recs)):
        i = 0
        for tile in line:
            if tile.is_full:
                i += 1
        if i == 10:
            return 16 - x

    return 99


def delete_ls(line, root):
    global recs, last_score, score, delay

    for tile in recs[line]:
        root, sprite = tile.clear(root)
    res = recs[:line]
    for x, lines in enumerate(reversed(res)):
        for y, tile in enumerate(lines):
            if tile.is_full:
                root, sprite = tile.clear(root)
                try:
                    root = recs[line - x][y].draw(root, sprite, False, False)
                except IndexError:
                    pass

    if score - last_score > 75000:
        delay -= 0.01
    return root


def save_record(root):
    global score

                                                                    # TODO: gui to ask for name and stuff...
    name = 'Mozl'


    lsr.save(score, name)

    return root


def see_records(root):

    root.blit(load_img.get_img(load_img.Screens.leaderboard), (0, 0))
    back_rect = load_img.get_img(load_img.Buttons.back).get_rect()
    back_rect.topleft = (912, 29)
    root.blit(load_img.get_img(load_img.Buttons.back), (back_rect.x, back_rect.y))
    placements = lsr.load()

    # draw the actual placement:

    for y, place in enumerate(placements):
        if y < 9:
            place[0] = ' ' + place[0]

        txt_surface = my_font.render(str(y + 1) + '. ' +(str(place[0])), True, load_img.Colors.Light_Grey.value)
        root.blit(txt_surface, (50, 122 + y * 51))

        txt_surface = my_font.render(str(place[1]), True, load_img.Colors.Light_Grey.value)
        root.blit(txt_surface, (515, 122 + y * 51))

    while True:
        if pygame.mouse.get_pressed()[0]:
            print(pygame.mouse.get_pos())
        pygame.display.update()

        for event in pygame.event.get():
            match event.type:
                case pygame.MOUSEBUTTONDOWN:    # we only check if the button is pressed
                    pos = pygame.mouse.get_pos()

                    if back_rect.collidepoint(pos):     # what to do if "quit" is pressed
                        root.blit(load_img.get_img(load_img.Buttons.back_clicked), (back_rect.x, back_rect.y))
                        pygame.display.update()
                        pygame.time.delay(100)
                        return root

                case pygame.MOUSEMOTION:    # we check for mouse movement
                    pos = pygame.mouse.get_pos()

                    if back_rect.collidepoint(pos):     # if mouse hovers over 'quit'
                        root.blit(load_img.get_img(load_img.Buttons.back_hover), (back_rect.x, back_rect.y))

                    else:
                        root.blit(load_img.get_img(load_img.Buttons.back), (back_rect.x, back_rect.y))

                case pygame.QUIT:
                    exit()


def game_over_state(root):
    global  first_start, score
    if lsr.in_tt(score):
        root = save_record(root)
    gos = True
    first_start = False
    root.blit(load_img.get_img(load_img.Screens.game_over), (0, 0))
    quit_rect = load_img.get_img(load_img.Buttons.quit).get_rect()
    quit_rect.topleft = (200, 600)
    try_rect = load_img.get_img(load_img.Buttons.try_again).get_rect()
    try_rect.topleft = (200, 400)
    home_rect = load_img.get_img(load_img.Buttons.home).get_rect()
    home_rect.topleft = (400, 850)
    root.blit(load_img.get_img(load_img.Buttons.quit), (quit_rect.x, quit_rect.y))
    root.blit(load_img.get_img(load_img.Buttons.try_again), (try_rect.x, try_rect.y))
    root.blit(load_img.get_img(load_img.Buttons.home), (home_rect.x, home_rect.y))

    while gos:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if quit_rect.collidepoint(pos):
                    root.blit(load_img.get_img(load_img.Buttons.quit_clicked), (quit_rect.x, quit_rect.y))
                    pygame.display.update()
                    pygame.time.delay(50)
                    exit(0)

                elif try_rect.collidepoint(pos):
                    root.blit(load_img.get_img(load_img.Buttons.try_again_clicked), (try_rect.x, try_rect.y))
                    pygame.display.update()
                    pygame.time.delay(25)
                    main()

                elif home_rect.collidepoint(pos):
                    root.blit(load_img.get_img(load_img.Buttons.home_clicked), (home_rect.x, home_rect.y))
                    pygame.display.update()
                    pygame.time.delay(25)
                    first_start = True
                    main()

            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()

                if quit_rect.collidepoint(pos):
                    root.blit(load_img.get_img(load_img.Buttons.quit_hover), (quit_rect.x, quit_rect.y))

                elif try_rect.collidepoint(pos):  # if mouse hovers over 'TryAgain'
                    root.blit(load_img.get_img(load_img.Buttons.try_again_hover), (try_rect.x, try_rect.y))

                elif home_rect.collidepoint(pos):  # if mouse hovers over 'TryAgain'
                    root.blit(load_img.get_img(load_img.Buttons.home_hover), (home_rect.x, home_rect.y))

                else:
                    root.blit(load_img.get_img(load_img.Buttons.try_again), (try_rect.x, try_rect.y))
                    root.blit(load_img.get_img(load_img.Buttons.quit), (quit_rect.x, quit_rect.y))
                    root.blit(load_img.get_img(load_img.Buttons.home), (home_rect.x, home_rect.y))

            elif event.type == pygame.QUIT:
                exit(101)


def starting_state(root):

    # we display the full starting screen
    root.blit(load_img.get_img(load_img.Screens.starting), (0, 0))

    # we define where and how big the buttons are
    quit_rect = load_img.get_img(load_img.Buttons.quit).get_rect()
    quit_rect.topleft = (200, 800)
    start_rect = load_img.get_img(load_img.Buttons.start).get_rect()
    start_rect.topleft = (200, 400)
    record_rect = load_img.get_img(load_img.Buttons.records).get_rect()
    record_rect.topleft = (200, 600)

    # we display the buttons
    root.blit(load_img.get_img(load_img.Buttons.quit), (quit_rect.x, quit_rect.y))
    root.blit(load_img.get_img(load_img.Buttons.start), (start_rect.x, start_rect.y))
    root.blit(load_img.get_img(load_img.Buttons.records), (record_rect.x, record_rect.y))
    while True:
        pygame.display.update() # each time we go through the loop we update the output

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:    # we only check if the button is pressed
                pos = pygame.mouse.get_pos()

                if quit_rect.collidepoint(pos):     # what to do if "quit" is pressed
                    root.blit(load_img.get_img(load_img.Buttons.quit_clicked), (quit_rect.x, quit_rect.y))
                    pygame.display.update()
                    pygame.time.delay(100)
                    exit(0)

                elif start_rect.collidepoint(pos):  # what to do if "start" is pressed
                    root.blit(load_img.get_img(load_img.Buttons.start_clicked), (start_rect.x, start_rect.y))
                    pygame.display.update()
                    pygame.time.delay(100)
                    return root

                elif record_rect.collidepoint(pos): # what to do if "records" is pressed
                    root.blit(load_img.get_img(load_img.Buttons.records_clicked), (record_rect.x, record_rect.y))
                    pygame.display.update()
                    pygame.time.delay(100)
                    root = see_records(root)
                    root.blit(load_img.get_img(load_img.Screens.starting), (0, 0))

            if event.type == pygame.MOUSEMOTION:    # we check for mouse movement
                pos = pygame.mouse.get_pos()

                if quit_rect.collidepoint(pos):     # if mouse hovers over 'quit'
                    root.blit(load_img.get_img(load_img.Buttons.quit_hover), (quit_rect.x, quit_rect.y))

                elif start_rect.collidepoint(pos):  # if mouse hovers over 'start'
                    root.blit(load_img.get_img(load_img.Buttons.start_hover), (start_rect.x, start_rect.y))

                elif record_rect.collidepoint(pos):  # if mouse hovers over 'record'
                    root.blit(load_img.get_img(load_img.Buttons.records_hover), (record_rect.x, record_rect.y))

                else:
                    root.blit(load_img.get_img(load_img.Buttons.start), (start_rect.x, start_rect.y))
                    root.blit(load_img.get_img(load_img.Buttons.quit), (quit_rect.x, quit_rect.y))
                    root.blit(load_img.get_img(load_img.Buttons.records), (record_rect.x, record_rect.y))

            elif event.type == pygame.QUIT:
                exit(101)


def next_block_display_init(root):
    global nb_disp
    root.blit(load_img.get_img(load_img.Screens.next_block), (615, 100))
    pygame.display.update()
    for x in range(0, 5):
        line = []
        for y in range(0, 5):
            line.append(NextRectangle(root, x, y))
        nb_disp.append(line)

    return root

def next_block_display(root, block):
    global nb_disp
    color = block[1]
    bl = copy.deepcopy(block[0])
    for x in nb_disp:
        for y in x:
            root = y.clear(root)

    for tile in bl[0]:
        tile[1] -= 3
        root = nb_disp[tile[1]][tile[0]].draw(root, color)

    return root

def score_disp(root):
    global score, my_font
    txt_surface = my_font.render(str(score), True, load_img.Colors.Light_Grey.value)

    root.blit(load_img.get_img(load_img.Screens.score), (615, 464))
    root.blit(txt_surface,(650, 518))
    return root

def init():                                                                 # added init so we can call main() again
    global screen_size, game_rect, borders, running, recs, score, delay, last_score
    screen_size = (1000, 1030)
    game_rect = (600, 1020)
    borders = 5
    running = True
    score = 0
    last_score = 0
    delay = 0.3
    recs = []


# MAIN


def main():
    global running, recs, in_a_row, score, delay
    init()
    current_delay = delay
    root = pygame.display.set_mode(screen_size)                         # we make the window full screen
    root.fill(load_img.Colors.Light_Grey.value)                                   # we make the background grey

    root = layout_init(root)

    start_time = time.time()
    direction = [0, 0]
    prev_block = None


    if first_start:
        root = starting_state(root)

    root = next_block_display_init(root)
    root, this_block = next_block(root)
    root, n_block = next_block(root)

    while running:
        root = score_disp(root)

        now_time = time.time()

        clear_line = check_line()
        if clear_line != 99:
            for line in recs:
                clear_line = check_line()
                if clear_line != 99:
                    in_a_row += 1
                    root = delete_ls(clear_line, root)
                    score += 1000
            if in_a_row == 4:
                score += 10000
            in_a_row = 0

        if now_time - start_time > delay:
            prev_block = copy.deepcopy(this_block[0][direction[0]])
            direction[1] = copy.deepcopy(direction[0])
            this_block = move_block(this_block)
            start_time = time.time()
            if engine(root, this_block, prev_block, direction):  # if the block is placed we swap the
                prev_block = None
                this_block = n_block
                root, n_block = next_block(root)
                score += 100
                if check_possible(this_block, direction):
                    running = False
                    game_over_state(root)

        last_dir = None

        for event in pygame.event.get():                                # we go over all events
            match event.type:                                           # and we use match|case on the events
                case pygame.QUIT:
                    return
                case pygame.KEYDOWN:                                    # we see if a key is pressed down

                    # MOVEMENT input

                    match event.key:
                        case pygame.K_a:                                # move left
                            is_possible = True
                            t = 0
                            for tile in this_block[0][direction[0]]:
                                if tile[1] - 1 < 10:
                                    t += 1
                            if t == 4:
                                is_possible = True
                            if is_possible:
                                this_block = lr_movement(this_block, True, direction)
                        case pygame.K_d:                               # move right
                            is_possible = True
                            t = 0
                            for tile in this_block[0][direction[0]]:
                                if tile[1] + 1 < 10:
                                    t += 1

                            if t == 4:
                                is_possible = True
                            if is_possible:
                                this_block = lr_movement(this_block, False, direction)
                        case pygame.K_w:                                # rotate right
                            last_dir = True
                            if direction[0] < 3:
                                direction[0] += 1
                            else:
                                direction[0] = 0
                        case pygame.K_s:                                # rotate left
                            last_dir = False
                            if direction[0] == 0:
                                direction[0] -= 1
                            else:
                                direction[0] = 3
                        case pygame.K_SPACE:                            # fast down
                            delay = 0.03

                case pygame.KEYUP:                                      # we see if a key is unpressed
                    if event.key == pygame.K_SPACE:
                        delay = current_delay
                case _:                                                 # default case
                    pass

        if check_possible(this_block, direction):
            if last_dir:
                if direction[0] == 0:
                    direction[0] = 3
                else:
                    direction[0] -= 1
            else:
                if direction[0] == 3:
                    direction[0] = 0
                else:
                    direction[0] += 1

        else:
            engine(root, this_block, prev_block, direction)

        pygame.display.update()


if __name__ == '__main__':
    main()
