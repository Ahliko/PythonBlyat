import pygame as pg
import pygame_widgets
from pygame_widgets.textbox import TextBox
from game import Game
from CustomButton import Button
from CustomLabel import Label


class CharacterMenu1:
    def __init__(self, game: Game):
        self.__game = game
        self.__quit = False
        self.__widgets = None
        self.__textbox_text = ""

    def __disable(self):
        self.__quit = True
        pg.event.wait(self.__game.framerate * 100 // 6)

    def __on_click_next(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        if self.__game.characters.get("character1") is None or self.__game.characters.get("character1")[1] == "":
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
        self.__game.characters.update({"character1": [1, self.__textbox_text]})

    def __on_click_choice2(self):
        self.__game.characters.update({"character1": [2, self.__textbox_text]})

    def __on_click_choice3(self):
        self.__game.characters.update({"character1": [3, self.__textbox_text]})

    def __on_click_choice4(self):
        self.__game.characters.update({"character1": [4, self.__textbox_text]})

    def __widgets_init(self):
        bouton_next = Button((self.__game.largeur / 2) + 615, (self.__game.hauteur / 2) + 360, 130, 40,
                             self.__game.font, 'Next',
                             self.__on_click_next, False, ('#2a75a1', '#666666', '#333333'))
        bouton_back = Button((self.__game.largeur / 2) - 745, (self.__game.hauteur / 2) + 360, 200, 40,
                             self.__game.font, 'Back',
                             self.__on_click_back, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice1 = Button(150, (self.__game.hauteur / 2), 200, 40,
                                self.__game.font, 'Hunt',
                                self.__on_click_choice1, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice2 = Button((self.__game.largeur / 4) + 150, (self.__game.hauteur / 2), 200, 40,
                                self.__game.font, 'Harmony',
                                self.__on_click_choice2, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice3 = Button((self.__game.largeur / 4) * 2 + 150, (self.__game.hauteur / 2), 200, 40,
                                self.__game.font, 'Abundance',
                                self.__on_click_choice3, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice4 = Button((self.__game.largeur / 4) * 3 + 150, (self.__game.hauteur / 2), 200, 40,
                                self.__game.font, 'Preservation',
                                self.__on_click_choice4, False, ('#2a75a1', '#666666', '#333333'))
        label_title = Label("PythonBlyat", 100, (0, 0, 0),
                            (self.__game.largeur / 2, self.__game.hauteur / 2 - 300), None, True)
        label_name = Label("Choose your character's name :", 50, (0, 0, 0),
                           (self.__game.largeur / 2, self.__game.hauteur / 4 * 3 - 50), None, True)
        label_selection = Label("Choose your character 1", 50, (0, 0, 0),
                                (self.__game.largeur / 2, self.__game.hauteur / 2 - 150),
                                None, True)
        return [bouton_next, bouton_back, bouton_choice1, bouton_choice2, bouton_choice3, bouton_choice4, label_title,
                label_selection, label_name]

    def run(self):
        pg.display.set_caption('PythonBlyat - Select First Character')
        textbox = TextBox(self.__game.ecran, self.__game.largeur / 2 - 250,
                          self.__game.hauteur / 4 * 3, 500, 50, font=self.__game.font, textColour=(0, 0, 0),
                          borderColour=(255, 255, 255), onSubmit=lambda: print(textbox.getText()))
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
            self.__textbox_text = textbox.getText()
            pygame_widgets.update(events)
            pg.display.update()
