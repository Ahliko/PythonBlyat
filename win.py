from game import Game
from CustomLabel import Label
from CustomButton import Button
import pygame as pg


class Win:
    def __init__(self, game: Game):
        self.__game = game
        self.__quit = False

    def __on_click_return(self):
        self.__quit = True

    def run(self):
        pg.display.set_caption('PythonBlyat - Win')
        widgets = [Button((self.__game.largeur / 2), (self.__game.hauteur / 2) + 50, 400, 50, self.__game.font,
                          'Return to main menu', self.__on_click_return, False, ('#2a75a1', '#666666', '#333333'),
                          center=True),
                   Label("You win", 100, (0, 0, 0), (self.__game.largeur / 2, self.__game.hauteur / 2 - 50), None,
                         True)]
        self.__game.update_screen(widgets)
        while not self.__quit:
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
