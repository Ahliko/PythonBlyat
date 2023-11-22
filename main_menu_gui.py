import pygame as pg
from CustomButton import Button
from CustomLabel import Label
from Environnement_ecran import EnvironnementEcran


class MainMenu(EnvironnementEcran):
    def __init__(self):
        super().__init__(1920, 1080, (255, 255, 255), 60)
        self.__quit = False
        self.texte_rect = None
        self.texte = None
        self.font = None
        self.__background = pg.image.load("mainmenu_background.jpg")
        self.__surface = pg.Surface((200, 200))

    @property
    def background(self):
        return self.__background

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
        pg.draw.rect(self.ecran, border_color, border_rect)
        self.ecran.blit(self.texte, self.texte_rect)
        pg.display.flip()

    def on_click_play(self):
        print("Button play clicked")

    def on_click_settings(self):
        from settings_gui import SettingsMenu
        settings_menu = SettingsMenu(self)
        settings_menu.run()

    def update_screen(self, **kwargs):
        self.ecran.blit(self.background, (0, 0))
        for i in kwargs:
            kwargs[i].draw(self.ecran)

    def run(self):
        pg.font.init()
        self.change_font("Arial", 30)
        pg.display.set_caption('PythonBlyat - MainMenu')
        bouton_play = Button((self.largeur / 2) - 100, self.hauteur / 2, 200, 100, self.font, 'Play',
                             self.on_click_play, False, ('#2a75a1', '#666666', '#333333'))
        bouton_settings = Button((self.largeur / 2) - 100, (self.hauteur / 2) + 150, 200, 100, self.font, 'Settings',
                                 self.on_click_settings, False, ('#2a75a1', '#666666', '#333333'))
        label_title = Label("PythonBlyat", 100, (0, 0, 0), (self.largeur / 2, self.hauteur / 2 - 50), None, True)
        self.update_screen(play=bouton_play, settings=bouton_settings, title=label_title)
        pg.display.flip()
        while not self.__quit:
            self.clock.tick(self.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.__quit = True
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.__quit = True
            self.update_screen(play=bouton_play, settings=bouton_settings, title=label_title)
            pg.display.update()
        pg.quit()
        exit()


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
