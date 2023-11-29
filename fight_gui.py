import pygame as pg
from CustomButton import Button
from CustomLabel import Label
from game import Game
from main_menu_gui import MainMenu


class FightMenu:
    def __init__(self, game: Game):
        self.__game = game
        self.__quit = False
        self.__sound = pg.mixer.Sound("Testicular Tango.mp3")
        self.__widgets = None
        self.__background = pg.image.load("Fight.png")
        self.__sound.play(-1)

    def __on_click_attacks(self):
        print("choice 1 : Acid pee attack")
        print("choice 2 : 360 Attack of Death That Kills")
        print("choice 3 : Stinky fart attack")
        print("choice 4 : Just fart fat")

    def __on_click_items(self):
        print("What in baaaaag ?")

    def __on_click_escape(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__disable()
        print("You have activated the special ability \"To take one's heels\", you run away like a coward...")

    def __disable(self):
        self.__sound.stop()
        self.__quit = True
        self.__sound.stop()

    def __widgets_init(self):
        bouton_attack_de_base = Button((self.__game.largeur / 2) - 350, (self.__game.hauteur / 2) + 180, 200, 50,
                                       self.__game.font,
                                       'Attack de base',
                                       self.__on_click_attacks, False, ('#2a75a1', '#666666', '#333333'))
        bouton_competences = Button((self.__game.largeur / 2) - 350, (self.__game.hauteur / 2) + 240, 200, 50,
                                    self.__game.font,
                                    'Compétences',
                                    self.__on_click_items, False, ('#2a75a1', '#666666', '#333333'))
        bouton_ultime = Button((self.__game.largeur / 2) - 350, (self.__game.hauteur / 2) + 300, 200, 50,
                               self.__game.font,
                               'Ultime',
                               self.__on_click_escape, False, ('#2a75a1', '#666666', '#333333'))
        label_stats = Label("Stats", 100, (0, 0, 0), (self.__game.largeur / 2 + 50, self.__game.hauteur / 2 + 350),
                            None, True)
        label_ennemi_stats = Label("Stats_ennemi", 100, (0, 0, 0),
                                   (self.__game.largeur / 2 + 500, self.__game.hauteur / 2 - 250),
                                   None, True)
        return [bouton_attack_de_base, bouton_competences, bouton_ultime, label_stats, label_ennemi_stats]

    def run(self):
        pg.display.set_caption('PythonBlyat - Fight')
        self.__widgets = self.__widgets_init()
        self.__game.update_screen(self.__widgets, self.__background)
        pg.display.flip()
        # TODO: Init fight with character
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
            self.__game.update_screen(self.__widgets, self.__background)
            pg.display.update()
