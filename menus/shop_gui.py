import pygame as pg
from widgets.CustomButton import Button
from widgets.CustomLabel import Label
from lib.game import Game


class ShopMenu:
    def __init__(self, game: Game):
        self.__game = game
        self.__quit = False
        self.__widgets = None
        self.__sound = pg.mixer.Sound("assets/shop.mp3")
        self.__background = pg.image.load("assets/Vendor.jpg")
        self.__sound.play(-1)

    def __on_click_buy(self):
        
        self.__game.play_sound_button()
        print("Pas chère, pas chère")

    def __on_click_sell(self):
        
        self.__game.play_sound_button()
        print("*tchip*")

    def __on_click_exit(self):
        
        self.__game.play_sound_button()
        self.__disable()

    def __disable(self):
        self.__sound.stop()
        self.__quit = True

    def __widgets_pos_update(self):
        self.__widgets[0].update_pos((self.__game.largeur / 2) + 615, (self.__game.hauteur / 2) + 360)
        self.__widgets[1].update_pos((self.__game.largeur / 2) - 745, (self.__game.hauteur / 2) + 360)
        self.__widgets[2].update_pos((self.__game.largeur / 2) - 450, (self.__game.hauteur / 2))
        self.__widgets[3].update_pos(self.__game.largeur / 2, self.__game.hauteur / 2 - 300)
        self.__widgets[4].update_pos(self.__game.largeur / 2, self.__game.hauteur / 2 - 200)

    def __widgets_init(self):
        bouton_buy = Button((self.__game.largeur / 2) + 615, (self.__game.hauteur / 2) + 360, 130, 40,
                            self.__game.font, 'Buy',
                            self.__on_click_buy, False, ('#2a75a1', '#666666', '#333333'))
        bouton_sell = Button((self.__game.largeur / 2) - 745, (self.__game.hauteur / 2) + 360, 130, 40,
                             self.__game.font, 'Sell',
                             self.__on_click_sell, False, ('#2a75a1', '#666666', '#333333'))
        bouton_exit = Button((self.__game.largeur / 2) - 450, (self.__game.hauteur / 2), 130, 40,
                             self.__game.font, 'Exit',
                             self.__on_click_exit, False, ('#2a75a1', '#666666', '#333333'))
        label_shop = Label("Welcome to my shop my frieennnd", 100, (255, 255, 255),
                           (self.__game.largeur / 2, self.__game.hauteur / 2 - 300), None, True)
        label_not_implemented = Label("Not implemented yet", 50, (255, 255, 255),
                                      (self.__game.largeur / 2, self.__game.hauteur / 2 - 200), None, True)
        return [bouton_buy, bouton_sell, bouton_exit, label_shop, label_not_implemented]

    def run(self):
        pg.display.set_caption('PythonBlyat - Shop')
        self.__widgets = self.__widgets_init()
        self.__game.update_screen(self.__widgets, self.__background)
        pg.display.flip()
        self.__widgets = self.__widgets_init()
        while not self.__quit:
            self.__game.handle_fullscreen()
            self.__widgets_pos_update()
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
            self.__game.update_screen(self.__widgets, self.__background)
            pg.display.update()
