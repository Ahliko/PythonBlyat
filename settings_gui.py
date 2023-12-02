import pygame as pg
from game import Game
import pygame_widgets
from pygame_widgets.slider import Slider
from CustomLabel import Label
from CustomButton import Button


class SettingsMenu:
    def __init__(self, game: Game):
        self.__game = game
        self.__quit = False
        self.__widgets = self.__widgets_init()

    def change_framerate(self, value):
        self.__game.framerate = value

    def disable(self):
        self.__quit = True
        pg.event.wait(self.__game.framerate * 100 // 6)

    def __widgets_init(self) -> list[Button, Label]:
        label = Label("Settings", 100, (0, 0, 0), (self.__game.largeur / 2, self.__game.hauteur / 2 - 50),
                      None, True)
        button = Button((self.__game.largeur / 2), (self.__game.hauteur / 2) + 50, 400, 50,
                        self.__game.font,
                        'Return to main menu', self.disable,
                        False, ('#2a75a1', '#666666', '#333333'), center=True)
        return [button, label]

    def run(self):
        pg.display.set_caption('PythonBlyat - SettingsMenu')
        slider = Slider(self.__game.ecran, (self.__game.largeur // 2) - 100,
                        (self.__game.hauteur // 2) + 140,
                        200,
                        40, min=10, max=170, step=10, initial=self.__game.framerate, colour=(255, 255, 255))
        self.__game.update_screen(self.__widgets)
        pg.display.flip()
        while not self.__quit:
            self.__game.framerate = slider.getValue()
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
            pygame_widgets.update(events)
            pg.display.update()
        slider.disable()
