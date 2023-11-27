import pygame as pg
from main_menu_gui import MainMenu
from CustomButton import Button
from CustomLabel import Label


class CharacterMenu1:
    def __init__(self, previous_menu: MainMenu):
        self.main_menu = previous_menu
        self.settings_menu = None
        self.__first_choice = None
        self.__quit = False
        self.__widgets = None

    def __disable(self):
        self.__quit = True
        pg.event.wait(self.main_menu.framerate * 100 // 6)

    def update_screen(self, lst_widgets: list[Button, Label]):
        self.main_menu.ecran.blit(self.main_menu.background, (0, 0))
        for i in lst_widgets:
            i.draw(self.main_menu.ecran)

    def on_click_next(self):
        pg.event.wait(self.main_menu.framerate * 100 // 6)
        if self.__first_choice is None:
            print("You must choose a character")
            return
        from selectCharacter2_gui import CharacterMenu2
        character2_menu = CharacterMenu2(self)
        character2_menu.run()
        print("Return to back1")
        self.__widgets = self.__widgets_init()

    def __on_click_back(self):
        self.__disable()

    def __on_click_choice1(self):
        self.first_choice = 1

    def __on_click_choice2(self):
        self.first_choice = 2

    def __on_click_choice3(self):
        self.first_choice = 3

    @property
    def first_choice(self):
        return self.__first_choice

    @first_choice.setter
    def first_choice(self, value):
        self.__first_choice = value

    def __widgets_init(self):
        bouton_next = Button((self.main_menu.largeur / 2) + 615, (self.main_menu.hauteur / 2) + 360, 130, 40,
                             self.main_menu.font, 'Next',
                             self.on_click_next, False, ('#2a75a1', '#666666', '#333333'))
        bouton_back = Button((self.main_menu.largeur / 2) - 745, (self.main_menu.hauteur / 2) + 360, 130, 40,
                             self.main_menu.font, 'Back',
                             self.__on_click_back, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice1 = Button((self.main_menu.largeur / 2) - 450, (self.main_menu.hauteur / 2), 130, 40,
                                self.main_menu.font, 'Choice1',
                                self.__on_click_choice1, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice2 = Button((self.main_menu.largeur / 2) - 60, (self.main_menu.hauteur / 2), 130, 40,
                                self.main_menu.font, 'Choice2',
                                self.__on_click_choice2, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice3 = Button((self.main_menu.largeur / 2) + 350, (self.main_menu.hauteur / 2), 130, 40,
                                self.main_menu.font, 'Choice3',
                                self.__on_click_choice3, False, ('#2a75a1', '#666666', '#333333'))
        label_title = Label("PythonBlyat", 100, (0, 0, 0),
                            (self.main_menu.largeur / 2, self.main_menu.hauteur / 2 - 300), None, True)
        label_selection = Label("Choose your character 1", 50, (0, 0, 0),
                                (self.main_menu.largeur / 2, self.main_menu.hauteur / 2 - 150),
                                None, True)
        return [bouton_next, bouton_back, bouton_choice1, bouton_choice2, bouton_choice3, label_title, label_selection]

    def run(self):
        pg.display.set_caption('PythonBlyat - Select First Character')
        self.__widgets = self.__widgets_init()
        self.update_screen(self.__widgets)
        pg.display.flip()
        while not self.__quit:
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
            self.update_screen(self.__widgets)
            pg.display.update()
