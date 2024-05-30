# 28/05/2024
# Experimenting with sorting algorithms

import pygame as py
import random
import time

py.init()
py.font.init()

# set screen size
DISPLAY_H = 600
DISPLAY_W = 800


SCREEN = py.display.set_mode((DISPLAY_W, DISPLAY_H))
FONT = py.font.SysFont('Calibri', 24)
py.display.set_caption('Sorting Algorithms')

# text
gen1_text = FONT.render('100', True, 'black')
gen2_text = FONT.render('1000', True, 'black')
gen3_text = FONT.render('10000', True, 'black')
sort_text = FONT.render('Pick Algo', True, 'black')

bubble_sort_text = FONT.render('Bubble', True, 'black')
selection_sort_text = FONT.render('Selection', True, 'black')
bogo_sort_text = FONT.render('Bogo', True, 'black')
merge_sort_text = FONT.render('Merge', True, 'black')

# button rects
gen1_rect = py.draw.rect(SCREEN, 'white', [100, 500, 100, 30])
gen2_rect = py.draw.rect(SCREEN, 'white', [250, 500, 100, 30])
gen3_rect = py.draw.rect(SCREEN, 'white', [400, 500, 100, 30])
sort_rect = py.draw.rect(SCREEN, 'red', [550, 500, 100, 30])
bubble_sort_rect = py.draw.rect(SCREEN, 'red', [550, 460, 100, 30])
selection_sort_rect = py.draw.rect(SCREEN, 'red', [550, 420, 100, 30])
bogo_sort_rect = py.draw.rect(SCREEN, 'red', [550, 380, 100, 30])
merge_sort_rect = py.draw.rect(SCREEN, 'red', [550, 340, 100, 30])

# background rects
button_ui_rects = py.draw.rect(SCREEN, 'dim grey', [0, 480, DISPLAY_W, DISPLAY_H - 480])

data_set1 = []
open_menu = False


def generate(num):
    data_set1.clear()
    for i in range(num):
        data_set1.append(random.randint(1, num))


def bubble_sort():
    start = time.process_time()
    loop = True

    while loop:
        # switches the places of two numbers, moving the bigger number to the right
        for i in range(1, len(data_set1)):
            if data_set1[i - 1] > data_set1[i]:
                temp = data_set1[i - 1]
                data_set1[i - 1] = data_set1[i]
                data_set1[i] = temp
        draw_screen(num)
        py.display.update()
        # final check
        if is_sorted():
            loop = False
            end = time.process_time()
            print("Run Time: ", end - start)


def bogo_sort():
    start = time.process_time()
    loop = True

    while loop:
        random.shuffle(data_set1)
        draw_screen(num)
        py.display.update()
        if is_sorted():
            loop = False
            end = time.process_time()
            print("Run Time: ", end - start)


def selection_sort():
    start = time.process_time()
    loop = True
    while loop:
        for i in range(0, len(data_set1) - 1):
            min = data_set1[i]
            for j in range(i, (len(data_set1) - 1)):
                if data_set1[1 + j] < min:
                    min = data_set1[1 + j]
                    saved_pos = 1 + j
            temp = data_set1[i]
            data_set1[i] = min
            data_set1[saved_pos] = temp
            draw_screen(num)
            py.display.update()

        if is_sorted():
            loop = False
            end = time.process_time()
            print("Run Time: ", end - start)


def merge_sort(list):
    partition = int(len(list)/2)
    part1 = list[:partition]
    part2 = list[partition:]
    if len(part1) > 1:
        merge_sort(part1)
    else:
        return part1
    if len(part2) > 1:
        merge_sort(part2)
    else:
        return part2


""" def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result """


""" def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev1 = fibonacci(n - 1)
    prev2 = fibonacci(n - 2)

    return prev1 + prev2 """


def is_sorted():
    for i in range(1, len(data_set1)):
        if data_set1[i - 1] > data_set1[i]:
            return False
    return True


def draw_screen(num):
    SCREEN.fill('black')

    py.draw.rect(SCREEN, 'dim grey', button_ui_rects)

    # draw buttons
    py.draw.rect(SCREEN, 'white', gen1_rect)
    py.draw.rect(SCREEN, 'white', gen2_rect)
    py.draw.rect(SCREEN, 'white', gen3_rect)
    py.draw.rect(SCREEN, 'red', sort_rect)

    # draw button outlines
    py.draw.rect(SCREEN, 'black', gen1_rect, 1)
    py.draw.rect(SCREEN, 'black', gen2_rect, 1)
    py.draw.rect(SCREEN, 'black', gen3_rect, 1)
    py.draw.rect(SCREEN, 'black', sort_rect, 1)

    # draw button text
    SCREEN.blit(gen1_text, [gen1_rect.center[0] - gen1_text.get_width()/2, gen1_rect.center[1] - gen1_text.get_height()/2])
    SCREEN.blit(gen2_text, [gen2_rect.center[0] - gen2_text.get_width()/2, gen3_rect.center[1] - gen2_text.get_height()/2])
    SCREEN.blit(gen3_text, [gen3_rect.center[0] - gen3_text.get_width()/2, gen3_rect.center[1] - gen3_text.get_height()/2])
    SCREEN.blit(sort_text, [sort_rect.center[0] - sort_text.get_width()/2, sort_rect.center[1] - sort_text.get_height()/2])

    """ if num == 10:
        for i in range(len(data_set1)):
            py.draw.rect(SCREEN, 'white', [20 + 10*i, 400 - 10*data_set1[i], 10, 10*data_set1[i]]) """
    if num == 100:
        for i in range(len(data_set1)):
            py.draw.rect(SCREEN, 'white', [40 + 7*i, 400 - data_set1[i]*3, 6, data_set1[i]*3])
    elif num == 1000:
        for i in range(len(data_set1)):
            py.draw.rect(SCREEN, 'white', [40 + 0.7*i, 400 - (data_set1[i]/5), 1, data_set1[i]/5])
    elif num == 7000:
        for i in range(len(data_set1)):
            py.draw.rect(SCREEN, 'white', [40 + 0.1*i, 400 - (data_set1[i]/25), 1, data_set1[i]/25])

    if open_menu:
        # draw sorting menu buttons
        py.draw.rect(SCREEN, 'red', bubble_sort_rect)
        py.draw.rect(SCREEN, 'red', selection_sort_rect)
        py.draw.rect(SCREEN, 'red', bogo_sort_rect)
        py.draw.rect(SCREEN, 'red', merge_sort_rect)

        # draw outlines for buttons
        py.draw.rect(SCREEN, 'black', bubble_sort_rect, 1)
        py.draw.rect(SCREEN, 'black', selection_sort_rect, 1)
        py.draw.rect(SCREEN, 'black', bogo_sort_rect, 1)
        py.draw.rect(SCREEN, 'black', merge_sort_rect, 1)

        # draw text for menu buttons
        SCREEN.blit(bubble_sort_text, [bubble_sort_rect.center[0] - bubble_sort_text.get_width()/2, bubble_sort_rect.center[1] - bubble_sort_text.get_height()/2])
        SCREEN.blit(selection_sort_text, [selection_sort_rect.center[0] - selection_sort_text.get_width()/2, selection_sort_rect.center[1] - selection_sort_text.get_height()/2])
        SCREEN.blit(bogo_sort_text, [bogo_sort_rect.center[0] - bogo_sort_text.get_width()/2, bogo_sort_rect.center[1] - bogo_sort_text.get_height()/2])
        SCREEN.blit(merge_sort_text, [merge_sort_rect.center[0] - merge_sort_text.get_width()/2, merge_sort_rect.center[1] - merge_sort_text.get_height()/2])


num = 0
run = True
while run:
    algo_picked = 0
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        # open/close sorting menu
        if event.type == py.MOUSEBUTTONDOWN and sort_rect.collidepoint(event.pos):
            if not open_menu:
                open_menu = True
            else:
                open_menu = False

        # buttons for generating data sets
        if event.type == py.MOUSEBUTTONDOWN and gen1_rect.collidepoint(event.pos):
            num = 100
            generate(num)
        elif event.type == py.MOUSEBUTTONDOWN and gen2_rect.collidepoint(event.pos):
            num = 1000
            generate(num)
        elif event.type == py.MOUSEBUTTONDOWN and gen3_rect.collidepoint(event.pos):
            num = 7000
            generate(num)

        # buttons for picking alog
        if event.type == py.MOUSEBUTTONDOWN and bubble_sort_rect.collidepoint(event.pos):
            open_menu = False
            bubble_sort()
        elif event.type == py.MOUSEBUTTONDOWN and selection_sort_rect.collidepoint(event.pos):
            open_menu = False
            selection_sort()
        elif event.type == py.MOUSEBUTTONDOWN and bogo_sort_rect.collidepoint(event.pos):
            open_menu = False
            bogo_sort()
        elif event.type == py.MOUSEBUTTONDOWN and merge_sort_rect.collidepoint(event.pos):
            start = time.process_time()
            merge_sort(data_set1)
            end = time.process_time()
            print("Run Time: ", end - start)

            # print("\n\nRecursion Example Results")
            # tri_recursion(6)

    draw_screen(num)
    py.display.update()
