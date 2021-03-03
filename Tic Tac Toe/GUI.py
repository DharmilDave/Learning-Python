import pygame as pg
import time
import sys
from pygame.locals import *

XO = "x"
winner = None
draw = None
width, height = 400, 400
white = (255, 255, 255)
line_color = (0, 0, 0)
board = [[None]*3, [None]*3, [None]*3]


# initializing pygame window
pg.init()
fps = 30

CLOCK = pg.time.Clock()
# * To set up our display window: pg.display.set_moded((tuple having width & height),depth,fps)
screen = pg.display.set_mode((width, height+100), 0, 32)
# to give name to our display
pg.display.set_caption("Tic Tac Toe Game")
# to load the background image to customize the display
# the problem is it takes img in its native size so we need to transformit
initializing_window = pg.image.load("img\cover.png")
x_img = pg.image.load("img\X.png")
o_img = pg.image.load("img\O.png")

# here we will transform the loaded images to our specific scale
# * pg.transform.scale(name of img,(width, height))
initializing_window = pg.transform.scale(
    initializing_window, (width, height+100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))


def game_initializing_winidow():
    # screen is the Python function and
    # blit is the method that enables pygame to display something over another thing
    screen.blit(initializing_window, (0, 0))
    pg.display.update()
    time.sleep(3)
    screen.fill(white)
    # * To draw line: pg.draw.line(display,line color,starting point, ending point,width)
    # drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, line_color, (0, height/3 * 2),
                 (width, height/3 * 2), 7)

    # drawing verical lines
    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_color, (width/3 * 2, 0),
                 (width/3 * 2, height), 7)
    draw_status()


def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + "Won :)"
    if draw:
        message = "Game Draw !"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, white)
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()
