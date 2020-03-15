import pygame as pg
import random

pg.init()

win = pg.display.set_mode((501, 501))
head_x = 251
head_y = 251
body_pos = []

def setup():
    pg.display.set_caption('Snake')
    for i in range(21):
        pg.draw.line(win, (128, 128, 128), (25*i,0), (25*i, 500), 1)
    
    for i in range(21):
        pg.draw.line(win, (128, 128, 128), (0,25*i), (500,25*i), 1)

    make_food()
    draw_snake()

def make_food():
    x = random.randint(0, 20)*25 + 1
    y = random.randint(0, 20)*25 + 1
    while x == 251 and y == 251:
        x = random.randint(0, 20)*25 + 1 
        y = random.randint(0, 20)*25 + 1 
    pg.draw.rect(win, (255, 0, 0), (x, y, 24, 24))


def draw_snake():
    pg.draw.rect(win, (0, 255, 0), (head_x, head_y, 24, 24))
    for i in body_pos:
        pg.draw.rect(win, (0, 255, 0), (i[0], i[1], 24, 24))

def move_snake(direction):
    if direction == 'R':
        if len(body_pos) > 1:
            for i in range(len(body_pos)-1, -1, -1):
                body_pos[i] = body_pos[i-1]
        if len(body_pos) != 0:
            body_pos[0] = [head_x, head_y] 
        print(head_x)
        head_x += 25
       


def main():
    setup()
    x = 50
    y = 50
    width = 40
    height = 50
    vel = 5
    running = True
    while running:
        pg.time.delay(100)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            x -= vel
        if keys[pg.K_RIGHT]:
            move_snake('R')
        if keys[pg.K_DOWN]:
            y += vel
        if keys[pg.K_UP]:
            y -= vel
        pg.display.update()

if __name__ == '__main__': main()
