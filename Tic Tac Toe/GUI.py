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

# * To draw line: pg.draw.line(display,line color,starting point, ending point,width)


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
