import pygame as pg
import pygame_widgets
from pygame_widgets.textbox import TextBox
from lib.game import Game


class CharacterMenu1:
    def __init__(self, game: Game):
        self.__game = game
        self.__quit = False
        self.__widgets = None
        self.__textbox_text = ""
        self.textbox = None

    def __disable(self):
        self.__quit = True
        pg.event.wait(self.__game.framerate * 100 // 6)

    def __on_click_next(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        if self.__game.characters.get("character1") is None or self.__game.characters.get("character1")[1] == "":
            print("You must choose a character")
            return

        from menus.selectCharacter2_gui import CharacterMenu2
        character2_menu = CharacterMenu2(self.__game)
        character2_menu.run()
        print("Return to back1")
        self.textbox.enable()
        self.textbox.show()
        self.__widgets = self.__game.widgets_init_characters(1, self.__on_click_next, self.__on_click_back,
                                                             self.__on_click_choice1, self.__on_click_choice2,
                                                             self.__on_click_choice3, self.__on_click_choice4)

    def __on_click_back(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        self.__disable()

    def __on_click_choice1(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        self.__game.characters.update({"character1": [1, self.__textbox_text]})

    def __on_click_choice2(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        self.__game.characters.update({"character1": [2, self.__textbox_text]})

    def __on_click_choice3(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        self.__game.characters.update({"character1": [3, self.__textbox_text]})

    def __on_click_choice4(self):
        self.__game.play_sound_button()
        self.__game.characters.update({"character1": [4, self.__textbox_text]})

    def run(self):
        pg.display.set_caption('PythonBlyat - Select First Character')
        self.__widgets = self.__game.widgets_init_characters(1, self.__on_click_next, self.__on_click_back,
                                                             self.__on_click_choice1, self.__on_click_choice2,
                                                             self.__on_click_choice3, self.__on_click_choice4)
        self.textbox = TextBox(self.__game.ecran, (self.__game.largeur / 8) * 4 - 250,
                               self.__game.hauteur / 4 * 3, 500, 50, font=self.__game.font, textColour=(0, 0, 0),
                               borderColour=(255, 255, 255), onSubmit=lambda: print(self.textbox.getText()))
        self.__game.update_screen(self.__widgets)
        pg.display.flip()
        self.__widgets = self.__game.widgets_init_characters(1, self.__on_click_next, self.__on_click_back,
                                                             self.__on_click_choice1, self.__on_click_choice2,
                                                             self.__on_click_choice3, self.__on_click_choice4)
        while not self.__quit:
            self.__game.widgets_pos_update(self.__widgets)
            self.textbox.setX(self.__game.largeur / 8 * 4 - 250)
            self.textbox.setY(self.__game.hauteur / 4 * 3)
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
            self.__textbox_text = self.textbox.getText()
            pygame_widgets.update(events)
            pg.display.update()
        self.textbox.disable()
        self.textbox.hide()
