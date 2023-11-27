import pygame as pg
from main_menu_gui import MainMenu
import pygame_widgets
from pygame_widgets.slider import Slider
from CustomLabel import Label
from CustomButton import Button


class SettingsMenu:
    def __init__(self, previous_menu: MainMenu):
        self.main_menu = previous_menu
        self.settings_menu = None
        self.__quit = False

    def change_framerate(self, value):
        self.main_menu.framerate = value

    def disable(self):
        self.__quit = True
        pg.event.wait(self.main_menu.framerate * 100 // 6)

    def update_screen(self, **kwargs):
        self.main_menu.ecran.blit(self.main_menu.background, (0, 0))
        for i in kwargs:
            kwargs[i].draw(self.main_menu.ecran)

    def run(self):
        pg.display.set_caption('PythonBlyat - SettingsMenu')
        slider = Slider(self.main_menu.ecran, (self.main_menu.largeur // 2) - 100,
                        (self.main_menu.hauteur // 2) + 140,
                        200,
                        40, min=10, max=170, step=10, initial=self.main_menu.framerate, colour=(255, 255, 255))
        label = Label("Settings", 100, (0, 0, 0), (self.main_menu.largeur / 2, self.main_menu.hauteur / 2 - 50),
                      None, True)
        button = Button((self.main_menu.largeur / 2), (self.main_menu.hauteur / 2) + 50, 400, 50,
                        self.main_menu.font,
                        'Return to main menu', self.disable,
                        False, ('#2a75a1', '#666666', '#333333'), center=True)
        self.update_screen(return_button=button, title=label)
        pg.display.flip()
        while not self.__quit:
            self.main_menu.framerate = slider.getValue()
            self.main_menu.clock.tick(self.main_menu.framerate)
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
