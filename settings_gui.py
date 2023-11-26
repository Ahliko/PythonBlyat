import pygame as pg
from main_menu_gui import MainMenu
import pygame_widgets
from pygame_widgets.slider import Slider
from CustomLabel import Label
from CustomButton import Button


class SettingsMenu:
    def __init__(self, previous_menu: MainMenu):
        self.previous_menu = previous_menu
        self.settings_menu = None
        self.__quit = False

    def change_framerate(self, value):
        self.previous_menu.framerate = value

    def disable(self):
        self.__quit = True
        pg.event.wait(self.previous_menu.framerate // 6)

    def update_screen(self, **kwargs):
        self.previous_menu.ecran.blit(self.previous_menu.background, (0, 0))
        for i in kwargs:
            kwargs[i].draw(self.previous_menu.ecran)

    def run(self):
        pg.display.set_caption('PythonBlyat - SettingsMenu')
        slider = Slider(self.previous_menu.ecran, (self.previous_menu.largeur // 2) - 100,
                        (self.previous_menu.hauteur // 2) + 140,
                        200,
                        40, min=10, max=170, step=10, initial=self.previous_menu.framerate, colour=(255, 255, 255))
        label = Label("Settings", 100, (0, 0, 0), (self.previous_menu.largeur / 2, self.previous_menu.hauteur / 2 - 50),
                      None, True)
        button = Button((self.previous_menu.largeur / 2), (self.previous_menu.hauteur / 2) + 50, 400, 50,
                        self.previous_menu.font,
                        'Return to main menu', self.disable,
                        False, ('#2a75a1', '#666666', '#333333'), center=True)
        self.update_screen(return_button=button, title=label)
        pg.display.flip()
        while not self.__quit:
            self.previous_menu.framerate = slider.getValue()
            self.previous_menu.clock.tick(self.previous_menu.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    print("Touche Echap")
                    pg.quit()
                    exit()
                elif event.type == pg.QUIT:
                    pg.quit()
                    exit()
            self.update_screen(return_button=button, title=label)
            pygame_widgets.update(events)
            pg.display.update()
