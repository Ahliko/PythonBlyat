import pygame as pg
from lib.game import Game
import pygame_widgets
from pygame_widgets.slider import Slider
from widgets.CustomLabel import Label
from widgets.CustomButton import Button


class SettingsMenu:
    def __init__(self, game: Game):
        self.__game = game
        self.__quit = False
        self.__widgets = self.__widgets_init()

    def change_framerate(self, value):
        self.__game.framerate = value

    def disable(self):
        self.__game.play_sound_button()
        self.__quit = True
        pg.event.wait(self.__game.framerate * 100 // 6)

    def __widgets_pos_update(self) -> None:
        self.__widgets[0].update_pos((self.__game.largeur / 2) - 100, self.__game.hauteur / 2)
        self.__widgets[1].update_pos((self.__game.largeur / 2) - 100, (self.__game.hauteur / 2) + 60)
        self.__widgets[2].update_pos((self.__game.largeur / 2) - 100, (self.__game.hauteur / 2) + 120)
        self.__widgets[3].update_pos(self.__game.largeur / 2, self.__game.hauteur / 2 - 50)

    def __widgets_init(self) -> list[Button, Label]:
        label = Label("Settings", self.__game.size, (0, 0, 0), (self.__game.largeur / 2, self.__game.hauteur / 2 - 50),
                      None, True)
        label_volume = Label(f"Volume {self.__game.volume}", self.__game.size, (0, 0, 0),
                             (self.__game.largeur / 2 - 350, self.__game.hauteur / 2 + 160),
                             None, True)
        button = Button((self.__game.largeur / 2), (self.__game.hauteur / 2) + 50, 400, 50,
                        self.__game.font,
                        'Return to main menu', self.disable,
                        False, ('#2a75a1', '#666666', '#333333'), center=True)
        return [button, label, label_volume]

    def run(self):
        pg.display.set_caption('PythonBlyat - SettingsMenu')
        slider = Slider(self.__game.ecran, (self.__game.largeur // 2) - 100,
                        (self.__game.hauteur // 2) + 140,
                        200,
                        40, min=0, max=100, step=1, initial=self.__game.volume, colour=(255, 255, 255))
        self.__game.update_screen(self.__widgets)
        pg.display.flip()
        self.__widgets = self.__widgets_init()
        while not self.__quit:
            self.__widgets_pos_update()
            self.__game.volume = slider.getValue()
            self.__widgets[2].text = f"Volume {self.__game.volume}"
            self.__game.clock.tick(self.__game.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    print("Touche Echap")
                    pg.quit()
                    exit()
                elif event.type == pg.QUIT:
                    pg.quit()
                    exit()
            self.__game.update_screen(self.__widgets)
            slider.setX((self.__game.largeur // 2) - 100)
            slider.setY((self.__game.hauteur // 2) + 140)
            pygame_widgets.update(events)
            pg.display.update()
        slider.disable()
        slider.hide()
