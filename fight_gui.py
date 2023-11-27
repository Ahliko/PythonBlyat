import pygame as pg
from CustomButton import Button
from CustomLabel import Label
from Environnement_ecran import EnvironnementEcran


class MainMenu(EnvironnementEcran):
    def __init__(self):
        super().__init__(1920, 1080, (255, 255, 255), 60)
        self.__quit = False
        self.texte_rect = None
        self.texte = None
        self.font = None
        self.__background = pg.image.load("../../Downloads/Zboulbizboulba.png")
        self.__surface = pg.Surface((200, 200))

    @property
    def background(self):
        return self.__background

    def change_font(self, font: str, taille: int):
        self.font = pg.font.SysFont(font, taille)

    def on_click_attacks(self):
        print("choice 1 : Acid pee attack")
        print("choice 2 : 360 Attack of Death That Kills")
        print("choice 3 : Stinky fart attack")
        print("choice 4 : Just fart fat")

    def on_click_items(self):
        print("What in baaaaag ?")

    def on_click_escape(self):
        print("You have activated the special ability \"To take one's heels\", you run away like a coward...")

    def update_screen(self, **kwargs):
        self.ecran.blit(self.background, (-50, 100))
        for i in kwargs:
            kwargs[i].draw(self.ecran)

    def run(self):
        pg.font.init()
        self.change_font("Arial", 30)
        pg.display.set_caption('PythonBlyat - Fight')
        bouton_attack_de_base = Button((self.largeur / 2) - 350, (self.hauteur / 2) + 180, 200, 50, self.font, 'Attack de base',
                                self.on_click_attacks, False, ('#2a75a1', '#666666', '#333333'))
        bouton_competences = Button((self.largeur / 2) - 350, (self.hauteur / 2) + 240, 200, 50, self.font, 'Compétences',
                              self.on_click_items, False, ('#2a75a1', '#666666', '#333333'))
        bouton_ultime = Button((self.largeur / 2) - 350, (self.hauteur / 2) + 300, 200, 50, self.font, 'Ultime',
                               self.on_click_escape, False, ('#2a75a1', '#666666', '#333333'))
        label_stats = Label("Stats", 100, (0, 0, 0), (self.largeur / 2 + 50, self.hauteur / 2 + 350), None, True)
        label_ennemi_stats = Label("Stats_ennemi", 100, (0, 0, 0), (self.largeur / 2 + 500, self.hauteur / 2 - 250), None, True)
        self.update_screen(attack=bouton_attack_de_base, competences=bouton_competences, ultime=bouton_ultime, stats=label_stats, ennemi_stats=label_ennemi_stats)
        pg.display.flip()
        while not self.__quit:
            self.clock.tick(self.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.__quit = True
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.__quit = True
            self.update_screen(attack=bouton_attack_de_base, competences=bouton_competences, ultime=bouton_ultime, stats=label_stats, ennemi_stats=label_ennemi_stats)
            pg.display.update()
        pg.quit()
        exit()


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
