import pygame as pg
from lib.game import Game
import pygame_widgets
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.slider import Slider
from widgets.CustomLabel import Label
from widgets.CustomButton import Button


class SettingsMenu:
    def __init__(self, game: Game):
        self.__apply = False
        self.__game = game
        self.__quit = False
        self.__widgets = self.__widgets_init()

    def change_framerate(self, value):
        self.__game.framerate = value

    def disable(self):
        self.__game.play_sound_button()
        self.__quit = True
    
    def apply(self):
        self.__game.play_sound_button()
        self.__apply = True

    def __widgets_pos_update(self) -> None:
        self.__widgets[0].update_pos((self.__game.largeur / 2), (self.__game.hauteur / 2) + 50)
        self.__widgets[1].update_pos(self.__game.largeur / 2, self.__game.hauteur / 2 - 50)
        self.__widgets[2].update_pos(self.__game.largeur / 2 - 350, self.__game.hauteur / 2 + 160)
        self.__widgets[3].update_pos((self.__game.largeur / 2) + 350, (self.__game.hauteur / 2) + 160)

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
        apply_button = Button((self.__game.largeur / 2) + 350, (self.__game.hauteur / 2) + 160, 100, 50,
                              self.__game.font,
                              'Apply', self.apply,
                              False, ('#2a75a1', '#666666', '#333333'), center=True)
        return [button, label, label_volume, apply_button]

    def change_resolution(self, value):
        match value:
            case "2560x1600":
                if self.__game.largeur != 2560 or self.__game.hauteur != 1600:
                    self.__game.change_resolution(2560, 1600)
            case "1920x1080":
                if self.__game.largeur != 1920 or self.__game.hauteur != 1080:
                    self.__game.change_resolution(1920, 1080)
            case "1280x720":
                if self.__game.largeur != 1280 or self.__game.hauteur != 720:
                    self.__game.change_resolution(1280, 720)
            case "640x480":
                if self.__game.largeur != 640 or self.__game.hauteur != 480:
                    self.__game.change_resolution(640, 480)
            case "320x240":
                if self.__game.largeur != 320 or self.__game.hauteur != 240:
                    self.__game.change_resolution(320, 240)
            case "160x120":
                if self.__game.largeur != 160 or self.__game.hauteur != 120:
                    self.__game.change_resolution(160, 120)

    def run(self):
        pg.display.set_caption('PythonBlyat - SettingsMenu')
        slider = Slider(self.__game.ecran, (self.__game.largeur // 2) - 100,
                        (self.__game.hauteur // 2) + 140,
                        200,
                        40, min=0, max=100, step=1, initial=self.__game.volume, colour=(255, 255, 255))
        dropdown = Dropdown(self.__game.ecran, (self.__game.largeur // 2) - 200,
                            (self.__game.hauteur // 2) + 140 + 80,
                            400, 80, f"{self.__game.largeur}x{self.__game.hauteur}",
                            ["2560x1600", "1920x1080", "1280x720", "640x480", "320x240", "160x120"],
                            colour=(255, 255, 255), selectionColour=(255, 255, 255), hoverColour=(255, 255, 255),
                            borderColour=(255, 255, 255), center=True)
        self.__game.update_screen(self.__widgets)
        pg.display.flip()
        self.__widgets = self.__widgets_init()
        while not self.__quit:
            self.__game.handle_fullscreen()
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
            dropdown.setX((self.__game.largeur // 2) - 200)
            dropdown.setY((self.__game.hauteur // 2) + 140 + 80)
            if self.__apply:
                self.__apply = False
                self.change_resolution(dropdown.getSelected())
            pygame_widgets.update(events)
            pg.display.update()
        slider.disable()
        slider.hide()
        dropdown.disable()
        dropdown.hide()
