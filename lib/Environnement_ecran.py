import pygame as pg


class EnvironnementEcran:
    def __init__(self, w, h, fond=(0, 0, 0), framerate=60):
        pg.init()
        self.largeur = w
        self.hauteur = h
        self.fond = fond
        self.framerate = framerate
        self.ecran = pg.display.set_mode((w, h), pg.RESIZABLE, 32)
        self.ecran.fill(fond)
        self.clock = pg.time.Clock()
        self.fullscreen = False

    def change_couleur(self, fond):
        self.ecran.fill(fond)
        pg.display.update()

    def handle_fullscreen(self):
        pressed = pg.key.get_pressed()
        if pressed[pg.K_F11]:
            self.fullscreen = not self.fullscreen
            if self.fullscreen:
                pg.display.set_mode((self.largeur, self.hauteur), pg.FULLSCREEN, 32)
            else:
                pg.display.set_mode((self.largeur, self.hauteur), pg.RESIZABLE, 32)
            self.ecran.fill(self.fond)
            pg.display.update()

    def change_resolution(self, w, h):
        self.largeur = w
        self.hauteur = h
        if self.fullscreen:
            self.ecran = pg.display.set_mode((w, h), pg.FULLSCREEN, 32)
        else:
            self.ecran = pg.display.set_mode((w, h), pg.RESIZABLE, 32)
        self.ecran.fill(self.fond)
        pg.display.update()

    def update_display(self):
        self.largeur, self.hauteur = pg.display.get_surface().get_size()
