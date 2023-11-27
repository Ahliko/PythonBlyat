import pygame as pg
from selectCharacter1_gui import CharacterMenu1
from CustomButton import Button
from CustomLabel import Label


class CharacterMenu2:
    def __init__(self, previous_menu: CharacterMenu1):
        self.first_character_menu = previous_menu
        self.main_menu = previous_menu.main_menu
        self.__quit = False
        self.__second_choice = None
        self.__widgets = None

    @property
    def second_choice(self):
        return self.__second_choice

    @second_choice.setter
    def second_choice(self, value):
        self.__second_choice = value

    def __disable(self):
        self.__quit = True
        pg.event.wait(self.main_menu.framerate * 100 // 6)

    def on_click_next(self):
        pg.event.wait(self.main_menu.framerate * 100 // 6)
        if self.__second_choice is None:
            print("You must choose a character")
            return
        from selectCharacter3_gui import CharacterMenu3
        character3_menu = CharacterMenu3(self)
        character3_menu.run()
        print("Return to back2")
        self.__widgets = self.__widgets_init()

    def __on_click_back(self):
        self.__disable()

    def __on_click_choice1(self):
        self.__second_choice = 1

    def __on_click_choice2(self):
        self.__second_choice = 2

    def __on_click_choice3(self):
        self.__second_choice = 3

    def __widgets_init(self) -> list[Button, Label]:
        bouton_next = Button((self.main_menu.largeur / 2) + 615,
                             (self.main_menu.hauteur / 2) + 360, 130, 40,
                             self.main_menu.font, 'Next',
                             self.on_click_next, False, ('#2a75a1', '#666666', '#333333'))
        bouton_back = Button((self.main_menu.largeur / 2) - 745,
                             (self.main_menu.hauteur / 2) + 360, 130, 40,
                             self.main_menu.font, 'Back',
                             self.__on_click_back, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice1 = Button((self.main_menu.largeur / 2) - 450,
                                (self.main_menu.hauteur / 2), 130, 40,
                                self.main_menu.font, 'Choice1',
                                self.__on_click_choice1, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice2 = Button((self.main_menu.largeur / 2) - 60,
                                (self.main_menu.hauteur / 2), 130, 40,
                                self.main_menu.font, 'Choice2',
                                self.__on_click_choice2, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice3 = Button((self.main_menu.largeur / 2) + 350,
                                (self.main_menu.hauteur / 2), 130, 40,
                                self.main_menu.font, 'Choice3',
                                self.__on_click_choice3, False, ('#2a75a1', '#666666', '#333333'))
        label_title = Label("PythonBlyat", 100, (0, 0, 0), (
            self.main_menu.largeur / 2, self.main_menu.hauteur / 2 - 300), None,
                            True)
        label_selection = Label("Choose your character 2", 50, (0, 0, 0), (
            self.main_menu.largeur / 2, self.main_menu.hauteur / 2 - 150),
                                None, True)
        return [bouton_next, bouton_back, bouton_choice1, bouton_choice2, bouton_choice3, label_title, label_selection]

    def run(self):
        pg.display.set_caption('PythonBlyat - Select Second Character')
        self.__widgets = self.__widgets_init()
        self.first_character_menu.update_screen(self.__widgets)
        pg.display.flip()
        while not self.__quit:
            self.main_menu.clock.tick(self.main_menu.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
            self.first_character_menu.update_screen(self.__widgets)
            pg.display.update()
