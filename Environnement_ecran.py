import pygame as pg


class EnvironnementEcran:
    def __init__(self, w, h, fond=(0, 0, 0)):
        self.largeur = w
        self.hauteur = h
        self.fond = fond
        self.ecran = pg.display.set_mode((w, h), 0, 32)
        self.ecran.fill(fond)

    def change_couleur(self, fond):
        self.ecran.fill(fond)
        pg.display.update()
