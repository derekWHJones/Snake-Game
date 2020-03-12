import pygame as pg

pg.init()
win = pg.display.set_mode((500, 500))

pg.display.set_caption('Snake')

def main():
    
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
            x += vel
        if keys[pg.K_DOWN]:
            y += vel
        if keys[pg.K_UP]:
            y -= vel
        win.fill((0,0,0))
        pg.draw.rect(win, (255, 0, 0), (x, y, width, height))
        pg.display.update()

if __name__ == '__main__': main()
