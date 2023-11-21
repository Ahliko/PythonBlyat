import pygame as pg


class EnvironnementEcran:
    def __init__(self, w, h, fond=(0, 0, 0), framerate=60):
        self.largeur = w
        self.hauteur = h
        self.fond = fond
        self.framerate = framerate
        self.ecran = pg.display.set_mode((w, h), 0, 32)
        self.ecran.fill(fond)

    def change_couleur(self, fond):
        self.ecran.fill(fond)
        pg.display.update()


if __name__ == "__main__":
    clock = pg.time.Clock()
    e = EnvironnementEcran(800, 600, (255, 255, 255))
    clock.tick(e.framerate)
    pg.init()
    pg.display.update()
    while True:
        e.change_couleur((255, 255, 255))
        pg.time.delay(2000)
        e.change_couleur((0, 0, 0))
        pg.time.delay(2000)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                print("Touche Echap")
                pg.quit()
                exit()
