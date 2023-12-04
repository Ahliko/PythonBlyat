from lib.game import Game
from widgets.CustomLabel import Label
from widgets.CustomButton import Button
import pygame as pg


class Lose:
    def __init__(self, game: Game):
        self.__game = game
        self.__quit = False

    def __on_click_return(self):
        self.__game.play_sound_button()
        
        self.__quit = True

    def run(self):
        pg.display.set_caption('PythonBlyat - Lose')
        widgets = [Button((self.__game.largeur / 2), (self.__game.hauteur / 2) + 50, 400, 50, self.__game.font,
                          'Return to main menu', self.__on_click_return, False, ('#2a75a1', '#666666', '#333333'),
                          center=True),
                   Label("You lose", 100, (0, 0, 0), (self.__game.largeur / 2, self.__game.hauteur / 2 - 50), None,
                         True)]
        while not self.__quit:
            self.__game.handle_fullscreen()
            widgets[0].update_pos((self.__game.largeur / 2), (self.__game.hauteur / 2) + 50)
            widgets[1].update_pos((self.__game.largeur / 2), self.__game.hauteur / 2 - 50)
            self.__game.clock.tick(self.__game.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
                elif event.type == pg.QUIT:
                    pg.quit()
                    exit()
            self.__game.update_screen(widgets)
            pg.display.update()
        pg.quit()
        exit()
