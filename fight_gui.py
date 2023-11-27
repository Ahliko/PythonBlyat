import pygame as pg
from CustomButton import Button
from CustomLabel import Label
from main_menu_gui import MainMenu


class FightMenu:
    def __init__(self, previous_menu: MainMenu):
        self.main_menu = previous_menu
        self.settings_menu = None
        self.__first_choice = None
        self.__quit = False
        self.__widgets = None
        self.__background = pg.image.load("Fight.png")

    def __on_click_attacks(self):
        print("choice 1 : Acid pee attack")
        print("choice 2 : 360 Attack of Death That Kills")
        print("choice 3 : Stinky fart attack")
        print("choice 4 : Just fart fat")

    def __on_click_items(self):
        print("What in baaaaag ?")

    def __on_click_escape(self):
        print("You have activated the special ability \"To take one's heels\", you run away like a coward...")

    def update_screen(self, lst_widgets: list[Button, Label]):
        self.main_menu.ecran.blit(self.main_menu.background, (0, 0))
        for i in lst_widgets:
            i.draw(self.main_menu.ecran)

    def __widgets_init(self):
        bouton_attack_de_base = Button((self.main_menu.largeur / 2) - 350, (self.main_menu.hauteur / 2) + 180, 200, 50, self.main_menu.font,
                                       'Attack de base',
                                       self.__on_click_attacks, False, ('#2a75a1', '#666666', '#333333'))
        bouton_competences = Button((self.main_menu.largeur / 2) - 350, (self.main_menu.hauteur / 2) + 240, 200, 50, self.main_menu.font,
                                    'Compétences',
                                    self.__on_click_items, False, ('#2a75a1', '#666666', '#333333'))
        bouton_ultime = Button((self.main_menu.largeur / 2) - 350, (self.main_menu.hauteur / 2) + 300, 200, 50, self.main_menu.font,
                               'Ultime',
                               self.__on_click_escape, False, ('#2a75a1', '#666666', '#333333'))
        label_stats = Label("Stats", 100, (0, 0, 0), (self.main_menu.largeur / 2 + 50, self.main_menu.hauteur / 2 + 350), None, True)
        label_ennemi_stats = Label("Stats_ennemi", 100, (0, 0, 0), (self.main_menu.largeur / 2 + 500, self.main_menu.hauteur / 2 - 250),
                                   None, True)
        return [bouton_attack_de_base, bouton_competences, bouton_ultime, label_stats, label_ennemi_stats]
    def run(self):
        pg.display.set_caption('PythonBlyat - Fight')
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
