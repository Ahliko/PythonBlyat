import pygame as pg
from CustomButton import Button
from CustomLabel import Label
from game import Game


class MainMenu:
    def __init__(self, game: Game):
        self.__game = game
        self.__init_main_menu()
        self.__widgets = self.__widgets_init()
        self.__game.play_sound_menu()
        self.__quit = False

    def __on_click_play(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        from selectCharacter1_gui import CharacterMenu1
        character1_menu = CharacterMenu1(self.__game)
        character1_menu.run()

    def __on_click_settings(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        from settings_gui import SettingsMenu
        settings_menu = SettingsMenu(self.__game)
        settings_menu.run()

    def __on_click_exit(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        self.__quit = True

    def __init_main_menu(self) -> None:
        self.__game.change_font("Arial", 30)
        self.__game.play_sound_button()
        pg.display.set_caption('PythonBlyat - MainMenu')
        pg.display.flip()

    def __widgets_init(self) -> list[Button, Label]:
        bouton_play = Button((self.__game.largeur / 2) - 100, self.__game.hauteur / 2, 200, 50, self.__game.font,
                             'Play',
                             self.__on_click_play, False, ('#2a75a1', '#666666', '#333333'))
        bouton_settings = Button((self.__game.largeur / 2) - 100, (self.__game.hauteur / 2) + 60, 200, 50,
                                 self.__game.font,
                                 'Settings',
                                 self.__on_click_settings, False, ('#2a75a1', '#666666', '#333333'))
        bouton_exit = Button((self.__game.largeur / 2) - 100, (self.__game.hauteur / 2) + 120, 200, 50,
                             self.__game.font,
                             'Exit',
                             self.__on_click_exit, False, ('#2a75a1', '#666666', '#333333'))
        label_title = Label("PythonBlyat", self.__game.size, (0, 0, 0), (self.__game.largeur / 2, self.__game.hauteur / 2 - 50),
                            None,
                            True)
        return [bouton_play, bouton_settings, bouton_exit, label_title]

    def run(self):
        while not self.__quit:
            self.__widgets = self.__widgets_init()
            self.__game.clock.tick(self.__game.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.__quit = True
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.__quit = True
            self.__game.update_screen(self.__widgets)
            pg.display.update()
        pg.quit()
        exit()
