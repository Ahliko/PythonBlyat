import pygame as pg
from widgets.CustomListLabel import ListLabel

pg.init()
screen = pg.display.set_mode((400, 400), pg.RESIZABLE)
clock = pg.time.Clock()
font = pg.font.SysFont('Arial', 30)


def on_click_play():
    print('Play')


listlabel = ListLabel('Title', ['Play', 'Options', 'Quit'], 30, (0, 0, 0), (200, 200))
while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    screen.fill((255, 255, 255))
    listlabel.update_pos_all(screen.get_width() / 2, screen.get_height() / 2)
    listlabel.draw(screen)
    pg.display.flip()
