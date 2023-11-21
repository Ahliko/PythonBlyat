import pygame as pg
import pygame_widgets as pw
from CustomButton import Button
import Environnement_ecran as ee


class MainMenu(ee.EnvironnementEcran):
    def __init__(self):
        super().__init__(800, 600, (255, 255, 255), 60)
        self.texte_rect = None
        self.texte = None
        self.font = None
        self.clock = pg.time.Clock()

    def change_font(self, font: str, taille: int):
        self.font = pg.font.SysFont(font, taille)

    def afficher_texte(self, texte: str, couleur: tuple[int, int, int], position: tuple[int, int],
                       border_thickness: int = 5, border_color: tuple[int, int, int] = (255, 0, 0)):
        self.texte = self.font.render(texte, True, couleur)
        self.texte_rect = self.texte.get_rect()
        self.texte_rect.center = position
        border_rect = pg.Rect(self.texte_rect.left - border_thickness,
                              self.texte_rect.top - border_thickness,
                              self.texte_rect.width + 2 * border_thickness,
                              self.texte_rect.height + 2 * border_thickness)
        self.ecran.fill(self.fond)
        pg.draw.rect(self.ecran, border_color, border_rect)
        self.ecran.blit(self.texte, self.texte_rect)
        pg.display.flip()

    def onClick(self):
        print("Button clicked")

    def run(self):
        pg.font.init()
        self.change_font("Arial", 30)
        pg.display.set_caption('PythonBlyat - MainMenu')
        button = Button(30, 30, 400, 100, self.font, 'Button One (onePress)', self.onClick)
        while True:
            self.clock.tick(self.framerate)
            # self.afficher_texte("PythonBlyat", (0, 0, 0), (self.largeur / 2, self.hauteur / 2), 10, (255, 0, 0))
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    print("Touche Echap")
                    pg.quit()
                    exit()

            button.process(self.ecran)

            pg.display.update()


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
