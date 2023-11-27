import pygame as pg
from CustomButton import Button
from CustomLabel import Label
from main_menu_gui import MainMenu


class ShopMenu:
    def __init__(self, previous_menu: MainMenu):
        self.main_menu = previous_menu
        self.settings_menu = None
        self.__first_choice = None
        self.__quit = False
        self.__widgets = None
        self.__background = pg.image.load("Vendor.jpg")

    def __on_click_buy(self):
        print("Pas chère, pas chère")

    def __on_click_sell(self):
        print("*tchip*")

    def __on_click_exit(self):
        self.disable()
        print("Goodbye my lover, goodbye my frieeend...")

    def update_screen(self, lst_widgets: list[Button, Label]):
        self.main_menu.ecran.blit(self.main_menu.background, (0, 0))
        for i in lst_widgets:
            i.draw(self.main_menu.ecran)

    def __widgets_init(self):
        bouton_buy = Button((self.main_menu.largeur / 2) + 615, (self.main_menu.hauteur / 2) + 360, 130, 40,
                              self.main_menu.font, 'Buy',
                              self.__on_click_buy, False, ('#2a75a1', '#666666', '#333333'))
        bouton_sell = Button((self.main_menu.largeur / 2) - 745, (self.main_menu.hauteur / 2) + 360, 130, 40,
                              self.main_menu.font, 'Sell',
                              self.__on_click_sell, False, ('#2a75a1', '#666666', '#333333'))
        bouton_exit = Button((self.main_menu.largeur / 2) - 450, (self.main_menu.hauteur / 2), 130, 40,
                              self.main_menu.font, 'Exit',
                              self.__on_click_exit, False, ('#2a75a1', '#666666', '#333333'))
        label_shop = Label("Welcome to my shop my frieennnd", 100, (255, 255, 255),
                            (self.main_menu.largeur / 2, self.main_menu.hauteur / 2 - 300), None, True)
        return [bouton_buy, bouton_sell, bouton_exit, label_shop]
    def run(self):
        pg.display.set_caption('PythonBlyat - Shop')
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
