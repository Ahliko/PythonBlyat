import pygame as pg
from CustomButton import Button
from CustomLabel import Label
from main_menu_gui import MainMenu


class SavesMenu:
    def __init__(self, previous_menu: MainMenu):
        self.main_menu = previous_menu
        self.settings_menu = None
        self.__first_choice = None
        self.__quit = False
        self.__widgets = None

    def __on_click_back(self):
        self.disable()

    def __on_click_save1(self):
        pass

    def __on_click_save2(self):
        pass

    def __on_click_save3(self):
        pass

    def update_screen(self, lst_widgets: list[Button, Label]):
        self.main_menu.ecran.blit(self.main_menu.background, (0, 0))
        for i in lst_widgets:
            i.draw(self.main_menu.ecran)

    def __widgets_init(self):
        bouton_save1 = Button((self.main_menu.largeur / 2) + 615, (self.main_menu.hauteur / 2) + 360, 130, 40,
                             self.main_menu.font, 'Next',
                             self.__on_click_save1, False, ('#2a75a1', '#666666', '#333333'))
        bouton_save2 = Button((self.main_menu.largeur / 2) - 745, (self.main_menu.hauteur / 2) + 360, 130, 40,
                             self.main_menu.font, 'Back',
                             self.__on_click_save2, False, ('#2a75a1', '#666666', '#333333'))
        bouton_save3 = Button((self.main_menu.largeur / 2) - 450, (self.main_menu.hauteur / 2), 130, 40,
                                self.main_menu.font, 'Choice1',
                                self.__on_click_save3, False, ('#2a75a1', '#666666', '#333333'))
        bouton_back = Button((self.main_menu.largeur / 2) - 60, (self.main_menu.hauteur / 2), 130, 40,
                                self.main_menu.font, 'Choice2',
                                self.__on_click_back, False, ('#2a75a1', '#666666', '#333333'))
        label_title = Label("PythonBlyat", 100, (0, 0, 0),
                            (self.main_menu.largeur / 2, self.main_menu.hauteur / 2 - 300), None, True)
        label_saves = Label("Saves", 50, (0, 0, 0),
                                (self.main_menu.largeur / 2, self.main_menu.hauteur / 2 - 150),
                                None, True)
        return [bouton_save1, bouton_save2, bouton_save3, bouton_back, label_title, label_saves]
    def run(self):
        pg.display.set_caption('PythonBlyat - Saves')
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
