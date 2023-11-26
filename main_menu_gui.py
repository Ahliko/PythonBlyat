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

    def on_click_play(self):
        pg.event.wait(self.framerate // 6)
        from selectCharacter1_gui import CharacterMenu1
        character1_menu = CharacterMenu1(self)
        character1_menu.run()

    def on_click_settings(self):
        pg.event.wait(self.framerate // 6)
        from settings_gui import SettingsMenu
        settings_menu = SettingsMenu(self)
        settings_menu.run()

    def on_click_exit(self):
        self.__quit = True

    def update_screen(self, **kwargs):
        self.ecran.blit(self.background, (0, 0))
        for i in kwargs:
            kwargs[i].draw(self.ecran)

    def run(self):
        pg.font.init()
        self.change_font("Arial", 30)
        pg.display.set_caption('PythonBlyat - MainMenu')
        bouton_play = Button((self.largeur / 2) - 100, self.hauteur / 2, 200, 50, self.font, 'Play',
                             self.on_click_play, False, ('#2a75a1', '#666666', '#333333'))
        bouton_settings = Button((self.largeur / 2) - 100, (self.hauteur / 2) + 60, 200, 50, self.font, 'Settings',
                                 self.on_click_settings, False, ('#2a75a1', '#666666', '#333333'))
        bouton_exit = Button((self.largeur / 2) - 100, (self.hauteur / 2) + 120, 200, 50, self.font, 'Exit',
                             self.on_click_exit, False, ('#2a75a1', '#666666', '#333333'))
        label_title = Label("PythonBlyat", 100, (0, 0, 0), (self.largeur / 2, self.hauteur / 2 - 50), None, True)
        self.update_screen(play=bouton_play, settings=bouton_settings, quit=bouton_exit, title=label_title)
        pg.display.flip()
        while not self.__quit:
            self.clock.tick(self.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.__quit = True
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.__quit = True
            self.update_screen(play=bouton_play, settings=bouton_settings, quit=bouton_exit, title=label_title)
            pg.display.update()
        pg.quit()
        exit()


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
