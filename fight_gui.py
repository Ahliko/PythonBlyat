from random import randint

import pygame as pg
from CustomButton import Button
from CustomLabel import Label
from game import Game
from engine import Engine


class FightMenu:
    def __init__(self, game: Game):
        self.__turn_fin = True
        self.__game = game
        self.__engine = Engine(self.__game)
        self.__quit = False
        self.__sound = pg.mixer.Sound("assets/Testicular Tango.mp3")
        self.__widgets = None
        self.__fin = False
        self.__win = False
        self.__lose = False
        self.__background = pg.image.load("assets/Fight.png")
        self.__sound.play(-1)

    def __on_click_attacks(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        next_carac = self.__engine.next_character(self.__game.all_characters)
        if self.get_character(next_carac) in self.__game.characters.values():
            while True:
                target_monster = self.__game.all_characters[randint(0, len(self.__game.monsters) - 1)]
                if target_monster in self.__game.monsters and target_monster.is_alive():
                    self.__game.all_characters[self.__game.all_characters.index(self.get_character(next_carac))].attack(
                        target_monster, self.__game)
                    break

    def __on_click_ability(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        next_carac = self.__engine.next_character(self.__game.all_characters)
        if self.get_character(next_carac) in self.__game.characters.values():
            while True:
                target_monster = self.__game.all_characters[randint(0, len(self.__game.monsters) - 1)]
                if target_monster in self.__game.monsters and target_monster.is_alive():
                    self.__game.all_characters[
                        self.__game.all_characters.index(self.get_character(next_carac))].ability(target_monster,
                                                                                                  self.__game)
                    break

    def __on_click_ultime(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        next_carac = self.__engine.next_character(self.__game.all_characters)
        if self.get_character(next_carac) in self.__game.characters.values():
            while True:
                target_monster = self.__game.all_characters[randint(0, len(self.__game.monsters) - 1)]
                if target_monster in self.__game.monsters and target_monster.is_alive():
                    self.__game.all_characters[self.__game.all_characters.index(self.get_character(next_carac))].ultime(
                        target_monster, self.__game)
                    break

    def __on_click_next(self):
        if self.__turn_fin:
            self.__engine.next_turn(self.__game.all_characters)
            self.__turn_fin = False

    def __disable(self):
        self.__sound.stop()
        if self.__engine.is_win([i for i in self.__game.characters.values()]):
            self.__win = True
        elif self.__engine.is_win(self.__game.monsters):
            self.__lose = True
        self.__sound.stop()

    def __widgets_init(self):
        bouton_attack_de_base = Button((self.__game.largeur / 2) - 350, (self.__game.hauteur / 2) + 180, 300, 50,
                                       self.__game.font,
                                       'Attack de base',
                                       self.__on_click_attacks, False, ('#2a75a1', '#666666', '#333333'))
        bouton_competences = Button((self.__game.largeur / 2) - 350, (self.__game.hauteur / 2) + 240, 300, 50,
                                    self.__game.font,
                                    'Compétences',
                                    self.__on_click_ability, False, ('#2a75a1', '#666666', '#333333'))
        bouton_ultime = Button((self.__game.largeur / 2) - 350, (self.__game.hauteur / 2) + 300, 300, 50,
                               self.__game.font,
                               'Ultime',
                               self.__on_click_ultime, False, ('#2a75a1', '#666666', '#333333'))
        label_stats = Label("Stats", 50, (0, 0, 0), (self.__game.largeur / 2, self.__game.hauteur / 2 + 350),
                            None, True)
        label_stats2 = Label("Stats", 50, (0, 0, 0), (self.__game.largeur / 2 + 150, self.__game.hauteur / 2 + 400),
                             None, True)
        label_stats3 = Label("Stats", 50, (0, 0, 0), (self.__game.largeur / 2 + 300, self.__game.hauteur / 2 + 450),
                             None, True)
        label_monster_stats = Label("Stats_ennemi", 50, (0, 0, 0),
                                    (self.__game.largeur / 2 + 300, self.__game.hauteur / 2 - 250),
                                    None, True)
        label_monster_stats2 = Label("Stats_ennemi", 50, (0, 0, 0),
                                     (self.__game.largeur / 2 + 450, self.__game.hauteur / 2 - 200),
                                     None, True)
        label_monster_stats3 = Label("Stats_ennemi", 50, (0, 0, 0),
                                     (self.__game.largeur / 2 + 600, self.__game.hauteur / 2 - 150),
                                     None, True)
        label_status = Label("Status", 50, (0, 0, 0), (self.__game.largeur / 2 - 300, self.__game.hauteur / 2 - 350),
                             None, True)

        return [bouton_attack_de_base, bouton_competences, bouton_ultime, label_stats, label_stats2, label_stats3,
                label_monster_stats,
                label_monster_stats2, label_monster_stats3, label_status]

    def get_character(self, id):
        for i in range(len(self.__game.all_characters)):
            if self.__game.all_characters[i].id == id:
                return self.__game.all_characters[i]

    def update_stats(self):
        for i in range(len(self.__game.all_characters)):
            self.__widgets[
                i + 3].text = f"{self.get_character(i + 1).name} : {self.get_character(i + 1).hp}/{self.get_character(i + 1).maxhp} HP | {self.get_character(i + 1).ultpts}/{self.get_character(i + 1).maxultpts} ULTPTS | {self.get_character(i + 1).cooldown} CD"

    def update_status(self):
        if self.__engine.is_win([i for i in self.__game.characters.values()]):
            self.__fin = True
            self.__widgets[-1].text = f"Vous avez gagné !"
        elif self.__engine.is_win([i for i in self.__game.monsters]):
            self.__fin = True
            self.__widgets[-1].text = f"Vous avez perdu !"
        else:
            self.__fin = False
            try:
                self.__widgets[
                    -1].text = f"It's {self.get_character(self.__engine.next_character(self.__game.all_characters)).name} to play !"
            except AttributeError:
                self.__widgets[
                    -1].text = f"Next turn !"

    def update_game(self):
        if self.get_character(self.__engine.next_character(self.__game.all_characters)) in self.__game.monsters:
            self.get_character(self.__engine.next_character(self.__game.all_characters)).choice(
                [i for i in self.__game.characters.values()])

    def run(self):
        pg.display.set_caption('PythonBlyat - Fight')
        self.__widgets = self.__widgets_init()
        self.__game.update_screen(self.__widgets, self.__background)
        pg.display.flip()
        self.__engine.final_list()
        widgets_fin = [self.__widgets[-1],
                       Button((self.__game.largeur / 2), (self.__game.hauteur / 2) + 50, 400, 50, self.__game.font,
                              'Terminate Fight', self.__disable, False, ('#2a75a1', '#666666', '#333333'),
                              center=True)]
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
            self.update_status()
            if not self.__fin:
                self.update_stats()
                self.update_game()
                self.__game.update_screen(self.__widgets, self.__background)
            else:
                if self.__win:
                    return True
                elif self.__lose:
                    return False
                self.__game.update_screen(widgets_fin)
            pg.display.update()
