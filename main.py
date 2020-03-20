import pygame as pg
import random

pg.init()

win = pg.display.set_mode((501, 501))
#first position is x second position is y
body_pos = [[251, 251]]

def draw_board():
    win.fill((0,0,0))
    for i in range(21):
        pg.draw.line(win, (128, 128, 128), (25*i,0), (25*i, 500), 1)
    
    for i in range(21):
        pg.draw.line(win, (128, 128, 128), (0,25*i), (500,25*i), 1)

    draw_snake()

def setup():
    pg.display.set_caption('Snake')
    draw_board() 
    return make_food()

def make_food():
    x = random.randint(0, 19)*25 + 1
    y = random.randint(0, 19)*25 + 1
    return [x, y]

def draw_food(x, y):
    pg.draw.rect(win, (255, 0, 0), (x, y, 24, 24))

def draw_snake():
    for i in body_pos:
        pg.draw.rect(win, (0, 255, 0), (i[0], i[1], 24, 24))

def move_snake(direction):
    if direction == 'R':
        for i in range(len(body_pos)-1, 0, -1):
                body_pos[i][0] = body_pos[i-1][0]
                body_pos[i][1] = body_pos[i-1][1]
        body_pos[0][0] += 25
    if direction == 'L':
        for i in range(len(body_pos)-1, 0, -1):
                body_pos[i][0] = body_pos[i-1][0]
                body_pos[i][1] = body_pos[i-1][1]
        body_pos[0][0] -= 25
    if direction == 'D':
        for i in range(len(body_pos)-1, 0, -1):
                body_pos[i][0] = body_pos[i-1][0]
                body_pos[i][1] = body_pos[i-1][1]
        body_pos[0][1] += 25
    if direction == 'U':
        for i in range(len(body_pos)-1, 0, -1):
                body_pos[i][0] = body_pos[i-1][0]
                body_pos[i][1] = body_pos[i-1][1]
        body_pos[0][1] -= 25


def main():
    food_xy = setup()
    running = True
    directions = 'R'
    while running:
        pg.time.delay(100)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            directions = 'L'
        if keys[pg.K_RIGHT]:
            directions = 'R'
        if keys[pg.K_DOWN]:
            directions = 'D'
        if keys[pg.K_UP]:
            directions = 'U'
        if body_pos[0][0] == food_xy[0] and body_pos[0][1] == food_xy[1]:
            food_xy = make_food()
        move_snake(directions)
        draw_board()
        draw_food(food_xy[0], food_xy[1])
        pg.display.update()

if __name__ == '__main__': main()
