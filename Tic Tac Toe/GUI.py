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
initializing_window = pg.image.load(
    "D:\Learning Python\Tic Tac Toe\img\cover.png")
x_img = pg.image.load("D:\Learning Python\Tic Tac Toe\img\X.png")
o_img = pg.image.load("D:\Learning Python\Tic Tac Toe\img\O.png")

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
        message = winner.upper() + " Won :)"
    if draw:
        message = "Game Draw !"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()


def check_win():
    global board, winner, draw

    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0), (0, (row+1)*height/3 - height/6),
                         (width, (row+1)*height/3 - height / 6), 4)
            break

    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),
                         ((col + 1) * width / 3 - width / 6, height), 4)
            break

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):

        # game won diagonally left to right
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):

        # game won diagonally right to left
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

    if(all([all(row) for row in board]) and winner is None):
        draw = True

    draw_status()


def drawXO(row, col):
    global board, XO
    if row == 1:
        posx = 30
    if row == 2:
        posx = width/3 + 30
    if row == 3:
        posx = width/3*2 + 30

    if col == 1:
        posy = 30
    if col == 2:
        posy = height/3 + 30
    if col == 3:
        posy = height/3*2 + 30
    board[row-1][col-1] = XO
    if(XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()


def userClick():
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()

    # get column of mouse click (1-3)
    if(x < width/3):
        col = 1
    elif (x < width/3*2):
        col = 2
    elif(x < width):
        col = 3
    else:
        col = None

    # get row of mouse click (1-3)
    if(y < height/3):
        row = 1
    elif (y < height/3*2):
        row = 2
    elif(y < height):
        row = 3
    else:
        row = None
    # print(row,col)

    if(row and col and board[row-1][col-1] is None):
        global XO

        # draw the x or o on screen
        drawXO(row, col)
        check_win()


def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = "x"
    draw = False
    game_initializing_winidow()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]


game_initializing_winidow()

while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            # print(event)
            userClick()
            if (winner or draw):
                reset_game()

    pg.display.update()
    CLOCK.tick(fps)
