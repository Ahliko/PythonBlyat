import pygame as pg

from game import Game
from CustomButton import Button
from CustomLabel import Label


class CharacterMenu1:
    def __init__(self, game: Game):
        self.__game = game
        self.__quit = False
        self.__widgets = None

    def __disable(self):
        self.__quit = True
        pg.event.wait(self.__game.framerate * 100 // 6)

    def __on_click_next(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        if self.__game.characters.get("character1") is None:
            print("You must choose a character")
            return
        from selectCharacter2_gui import CharacterMenu2
        character2_menu = CharacterMenu2(self.__game)
        character2_menu.run()
        print("Return to back1")
        self.__widgets = self.__widgets_init()

    def __on_click_back(self):
        self.__disable()

    def __on_click_choice1(self):
        self.__game.characters.update({"character1": 1})

    def __on_click_choice2(self):
        self.__game.characters.update({"character1": 2})

    def __on_click_choice3(self):
        self.__game.characters.update({"character1": 3})

    def __widgets_init(self):
        bouton_next = Button((self.__game.largeur / 2) + 615, (self.__game.hauteur / 2) + 360, 130, 40,
                             self.__game.font, 'Next',
                             self.__on_click_next, False, ('#2a75a1', '#666666', '#333333'))
        bouton_back = Button((self.__game.largeur / 2) - 745, (self.__game.hauteur / 2) + 360, 130, 40,
                             self.__game.font, 'Back',
                             self.__on_click_back, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice1 = Button((self.__game.largeur / 2) - 450, (self.__game.hauteur / 2), 130, 40,
                                self.__game.font, 'Choice1',
                                self.__on_click_choice1, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice2 = Button((self.__game.largeur / 2) - 60, (self.__game.hauteur / 2), 130, 40,
                                self.__game.font, 'Choice2',
                                self.__on_click_choice2, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice3 = Button((self.__game.largeur / 2) + 350, (self.__game.hauteur / 2), 130, 40,
                                self.__game.font, 'Choice3',
                                self.__on_click_choice3, False, ('#2a75a1', '#666666', '#333333'))
        label_title = Label("PythonBlyat", 100, (0, 0, 0),
                            (self.__game.largeur / 2, self.__game.hauteur / 2 - 300), None, True)
        label_selection = Label("Choose your character 1", 50, (0, 0, 0),
                                (self.__game.largeur / 2, self.__game.hauteur / 2 - 150),
                                None, True)
        return [bouton_next, bouton_back, bouton_choice1, bouton_choice2, bouton_choice3, label_title, label_selection]

    def run(self):
        pg.display.set_caption('PythonBlyat - Select First Character')
        self.__widgets = self.__widgets_init()
        self.__game.update_screen(self.__widgets)
        pg.display.flip()
        while not self.__quit:
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
            pg.display.update()
