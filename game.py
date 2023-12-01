import pygame as pg
from CustomButton import Button
from CustomLabel import Label
from Environnement_ecran import EnvironnementEcran


class Game(EnvironnementEcran):
    def __init__(self):
        super().__init__(1920, 1080, (255, 255, 255), 60)
        pg.font.init()
        self.__font = None
        self.__background = pg.image.load("assets/mainmenu_background.jpg")
        self.__characters = {
            "character1": None,
            "character2": None,
            "character3": None
        }
        self.__monsters = []

    @property
    def characters(self):
        return self.__characters

    @characters.setter
    def characters(self, value):
        self.__characters = value

    @property
    def monsters(self):
        return self.__characters

    @monsters.setter
    def monsters(self, value):
        self.__characters = value

    @property
    def background(self) -> pg.Surface:
        return self.__background

    @background.setter
    def background(self, value: pg.Surface):
        self.__background = value

    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value):
        self.__font = value

    def change_font(self, font: str, taille: int):
        self.__font = pg.font.SysFont(font, taille)

    def update_screen(self, lst_widgets: list[Button, Label], background: pg.Surface = None):
        if background is None:
            self.ecran.blit(self.__background, (0, 0))
        else:
            self.ecran.blit(background, (0, 0))
        for i in lst_widgets:
            i.draw(self.ecran)

    def run(self):
        from main_menu_gui import MainMenu
        main_menu = MainMenu(self)
        main_menu.run()
