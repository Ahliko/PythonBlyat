import pygame as pg


class EnvironnementEcran:
    def __init__(self, w, h, fond=(0, 0, 0), framerate=60):
        pg.init()
        self.largeur = w
        self.hauteur = h
        self.fond = fond
        self.framerate = framerate
        self.ecran = pg.display.set_mode((w, h), pg.RESIZABLE, 32, )
        self.ecran.fill(fond)
        self.clock = pg.time.Clock()

    def change_couleur(self, fond):
        self.ecran.fill(fond)
        pg.display.update()

    def update_display(self):
        self.largeur, self.hauteur = pg.display.get_surface().get_size()
