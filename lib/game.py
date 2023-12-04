import pygame as pg
from widgets.CustomButton import Button
from widgets.CustomLabel import Label
from Environnement_ecran import EnvironnementEcran


class Game(EnvironnementEcran):
    def __init__(self):
        super().__init__(1920, 1080, (255, 255, 255), 60)
        pg.font.init()
        self.__font = None
        self.__background = pg.image.load("../assets/mainmenu_background.jpg")
        self.__history = []
        self.__size = int(self.largeur / self.hauteur * 100)
        self.__characters = {
            "character1": None,
            "character2": None,
            "character3": None
        }
        self.__monsters = []
        self.__all_characters = []
        self.__sound_button = pg.mixer.Sound("../assets/bouton_click.wav")
        self.__sound_menu = pg.mixer.Sound("../assets/menu.mp3")
        self.__sound_fight = pg.mixer.Sound("../assets/fight.mp3")
        self.__sound_win_fight = pg.mixer.Sound("../assets/win_fight.mp3")
        self.__sound_lose_fight = pg.mixer.Sound("../assets/lose_fight.mp3")
        self.__sound_bump = pg.mixer.Sound("../assets/bump.mp3")
        self.__sound_donjon = pg.mixer.Sound("../assets/donjon.mp3")
        self.__volume = 50
        self.__sound_menu.set_volume(self.__volume / 100)
        self.__sound_button.set_volume(self.__volume / 100)
        self.__sound_fight.set_volume(self.__volume / 100)
        self.__sound_win_fight.set_volume(self.__volume / 100)
        self.__sound_lose_fight.set_volume(self.__volume / 100)
        self.__sound_bump.set_volume(self.__volume / 100)
        self.__sound_donjon.set_volume(self.__volume / 100)

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value
        self.__sound_menu.set_volume(self.__volume / 100)
        self.__sound_button.set_volume(self.__volume / 100)
        self.__sound_fight.set_volume(self.__volume / 100)
        self.__sound_win_fight.set_volume(self.__volume / 100)
        self.__sound_lose_fight.set_volume(self.__volume / 100)
        self.__sound_bump.set_volume(self.__volume / 100)
        self.__sound_donjon.set_volume(self.__volume / 100)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def play_sound_donjon(self):
        self.__sound_donjon.play(-1)

    def stop_sound_donjon(self):
        self.__sound_donjon.stop()

    def play_sound_bump(self):
        self.__sound_bump.play()

    def play_sound_win_fight(self):
        self.__sound_win_fight.play()

    def stop_sound_win_fight(self):
        self.__sound_win_fight.stop()

    def play_sound_lose_fight(self):
        self.__sound_lose_fight.play()

    def stop_sound_lose_fight(self):
        self.__sound_lose_fight.stop()

    def play_sound_menu(self):
        self.__sound_menu.play(-1)

    def stop_sound_menu(self):
        self.__sound_menu.stop()

    def play_sound_fight(self):
        self.__sound_fight.play(-1)

    def stop_sound_fight(self):
        self.__sound_fight.stop()

    def play_sound_button(self):
        self.__sound_button.play()

    def widgets_init_characters(self, nb, __on_click_next, __on_click_back, __on_click_choice1, __on_click_choice2,
                                __on_click_choice3, __on_click_choice4):
        bouton_next = Button((self.largeur / 8) * 7, self.hauteur / 4 * 3, 130, 40,
                             self.font, 'Next',
                             __on_click_next, False, ('#2a75a1', '#666666', '#333333'), center=True)
        bouton_back = Button((self.largeur / 8), self.hauteur / 4 * 3, 200, 40,
                             self.font, 'Back',
                             __on_click_back, False, ('#2a75a1', '#666666', '#333333'), center=True)
        bouton_choice1 = Button((self.largeur / 5), (self.hauteur / 2), 200, 40,
                                self.font, 'Hunt',
                                __on_click_choice1, False, ('#2a75a1', '#666666', '#333333'), center=True)
        bouton_choice2 = Button((self.largeur / 5) * 2, (self.hauteur / 2), 200, 40,
                                self.font, 'Harmony',
                                __on_click_choice2, False, ('#2a75a1', '#666666', '#333333'), center=True)
        bouton_choice3 = Button((self.largeur / 5) * 3, (self.hauteur / 2), 200, 40,
                                self.font, 'Abundance',
                                __on_click_choice3, False, ('#2a75a1', '#666666', '#333333'), center=True)
        bouton_choice4 = Button((self.largeur / 5) * 4, (self.hauteur / 2), 200, 40,
                                self.font, 'Preservation',
                                __on_click_choice4, False, ('#2a75a1', '#666666', '#333333'), center=True)
        label_title = Label("PythonBlyat", self.__size, (0, 0, 0),
                            (self.largeur / 2, self.hauteur / 2 - 300), None, True)
        label_name = Label("Choose your character's name :", self.__size // 2, (0, 0, 0),
                           (self.largeur / 2, self.hauteur / 4 * 3 - 50), None, True)
        label_selection = Label(f"Choose your character {nb}", self.__size // 2, (0, 0, 0),
                                (self.largeur / 2, self.hauteur / 2 - 150),
                                None, True)
        return [bouton_next, bouton_back, bouton_choice1, bouton_choice2, bouton_choice3, bouton_choice4, label_title,
                label_selection, label_name]

    @property
    def characters(self):
        return self.__characters

    @characters.setter
    def characters(self, value):
        self.__characters = value

    @property
    def monsters(self):
        return self.__monsters

    @monsters.setter
    def monsters(self, value):
        self.__monsters = value

    @property
    def all_characters(self):
        return self.__all_characters

    @all_characters.setter
    def all_characters(self, value):
        self.__all_characters = value

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

    @property
    def history(self):
        return self.__history

    @history.setter
    def history(self, value):
        self.__history = value

    def change_font(self, font: str, taille: int):
        self.__font = pg.font.SysFont(font, taille)

    def update_screen(self, lst_widgets: list[Button, Label], background: pg.Surface = None):
        self.update_display()
        self.__size = int(self.largeur / self.hauteur * 50)
        if background is None:
            self.ecran.blit(pg.transform.scale(self.__background, (self.largeur, self.hauteur)), (0, 0))
        else:
            self.ecran.blit(pg.transform.scale(background, (self.largeur, self.hauteur)), (0, 0))
        for i in lst_widgets:
            i.draw(self.ecran)

    def run(self):
        from menus.main_menu_gui import MainMenu
        main_menu = MainMenu(self)
        main_menu.run()
