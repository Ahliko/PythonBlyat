import pygame as pg
import pygame_menu as pm
from main_menu_gui import MainMenu


class SettingsMenu:
    def __init__(self, previous_menu: MainMenu):
        self.previous_menu = previous_menu
        self.settings_menu = None

    def change_framerate(self, value):
        self.previous_menu.framerate = value

    def run(self):
        pg.display.set_caption('PythonBlyat - SettingsMenu')
        self.settings_menu = pm.Menu('Settings', self.previous_menu.largeur, self.previous_menu.hauteur,
                                     theme=pm.themes.THEME_ORANGE)
        self.settings_menu.add.button('Return to main menu', self.settings_menu.disable)
        self.settings_menu.add.range_slider('Framerate', self.previous_menu.framerate, (10, 170), 10,
                                            onchange=self.change_framerate)
        pg.display.flip()
        while self.settings_menu.is_enabled():
            print(self.previous_menu.framerate)
            self.previous_menu.clock.tick(self.previous_menu.framerate)
            self.settings_menu.mainloop(self.previous_menu.ecran)
            events = pg.event.get()
            for event in events:
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    print("Touche Echap")
                    break
                elif event.type == pg.QUIT:
                    break
            if self.settings_menu.is_enabled():
                self.settings_menu.update(events)
                self.settings_menu.draw(self.previous_menu.ecran)
            pg.display.update()
        pg.quit()
        exit(0)
