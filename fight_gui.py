from random import randint

import threading
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
        self.__sound = pg.mixer.Sound("assets/fight.mp3")
        self.__widgets = None
        self.__fin = False
        self.__win = False
        self.__lose = False
        self.__choice = None
        self.__threads = []
        self.__func = None
        self.__running = False
        self.__background = pg.image.load("assets/Fight.png")
        self.__sound.play(-1)

    def show(self):
        for i in self.__widgets[:3]:
            i.hide()
        self.__widgets[9].show()
        self.__widgets[10].show()
        self.__widgets[11].show()
        self.__widgets[-1].text = f"Choose your target !"

    def hide(self):
        for i in self.__widgets[:3]:
            i.show()
        self.__widgets[9].hide()
        self.__widgets[10].hide()
        self.__widgets[11].hide()

    def on_attack(self):
        self.__running = True
        next_carac = self.__engine.next_character(self.__game.all_characters)
        if self.get_character(next_carac) in self.__game.characters.values():
            self.show()
            if self.__choice is not None:
                target_monster = self.__game.monsters[self.__choice]
                if target_monster.is_alive():
                    self.__game.all_characters[self.__game.all_characters.index(self.get_character(next_carac))].attack(
                        target_monster, self.__game)
                self.__choice = None
                self.hide()
                self.__func = None
        self.__running = False

    def on_ability(self):
        self.__running = True
        next_carac = self.get_character(self.__engine.next_character(self.__game.all_characters))
        if next_carac in self.__game.characters.values():
            self.show()
            if self.__choice is not None:
                if type(next_carac).__name__ == "Hunt":
                    print("hunt")
                    target = self.__game.monsters[self.__choice]
                else:
                    print("not hunt")
                    target = [i for i in self.__game.characters.values()][self.__choice]
                if target.is_alive():
                    print("target is alive")
                    self.__game.all_characters[
                        self.__game.all_characters.index(next_carac)].ability(target,
                                                                              self.__game)
                self.__choice = None
                self.hide()
                self.__func = None
        self.__running = False

    def on_ultime(self):
        self.__running = True
        next_carac = self.get_character(self.__engine.next_character(self.__game.all_characters))
        if next_carac in self.__game.characters.values():
            if type(next_carac).__name__ == "Hunt":
                self.show()
                if self.__choice is None:
                    return
                target = [i for i in self.__game.monsters][self.__choice]
                self.__choice = None
                self.hide()
                self.__func = None
            else:
                target = [i for i in self.__game.characters.values() if i.is_alive()]
            self.__game.all_characters[self.__game.all_characters.index(next_carac)].ultime(
                target, self.__game)
        self.__running = False

    def __on_click_attacks(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        self.__func = self.on_attack
        self.on_attack()

    def __on_click_ability(self):
        pg.event.wait(self.__game.framerate * 100)
        self.__game.play_sound_button()
        self.__func = self.on_ability
        self.on_ability()

    def __on_click_ultime(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        self.__func = self.on_ultime
        self.on_ultime()

    def __on_click_next(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        if self.__turn_fin:
            self.__engine.next_turn(self.__game.all_characters)
            self.__turn_fin = False

    def __disable(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        self.__sound.stop()
        if self.__engine.is_win([i for i in self.__game.characters.values()]):
            self.__win = True
        elif self.__engine.is_win(self.__game.monsters):
            self.__lose = True
        self.__sound.stop()

    def __on_click_one(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        self.__choice = 0

    def __on_click_two(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        self.__choice = 1

    def __on_click_three(self):
        pg.event.wait(self.__game.framerate * 100 // 6)
        self.__game.play_sound_button()
        self.__choice = 2

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
        bouton_1 = Button((self.__game.largeur / 2) - 350, (self.__game.hauteur / 2) + 180, 300, 50,
                          self.__game.font,
                          'Target 1',
                          self.__on_click_one, False, ('#2a75a1', '#666666', '#333333'), hide=True)
        bouton_2 = Button((self.__game.largeur / 2) - 350, (self.__game.hauteur / 2) + 240, 300, 50,
                          self.__game.font,
                          'Target 2',
                          self.__on_click_two, False, ('#2a75a1', '#666666', '#333333'), hide=True)
        bouton_3 = Button((self.__game.largeur / 2) - 350, (self.__game.hauteur / 2) + 300, 300, 50,
                          self.__game.font,
                          'Target 3',
                          self.__on_click_three, False, ('#2a75a1', '#666666', '#333333'), hide=True)
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
                label_monster_stats2, label_monster_stats3, bouton_1, bouton_2, bouton_3, label_status]

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
            self.__sound.stop()
            self.__sound = pg.mixer.Sound("assets/lose.mp3")
            self.__sound.play()
            self.__widgets[-1].text = f"Vous avez perdu !"
        elif self.__engine.is_win([i for i in self.__game.monsters]):
            self.__fin = True
            self.__sound.stop()
            self.__sound = pg.mixer.Sound("assets/victory.mp3")
            self.__sound.play()
            self.__widgets[-1].text = f"Vous avez gagné !"
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
                [i for i in self.__game.characters.values()], self.__game)

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
            if self.__func is not None:
                self.__func()
            self.__game.clock.tick(self.__game.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    print("Touche Echap")
                    for i in self.__threads:
                        i.join()
                    pg.quit()
                    exit()
                elif event.type == pg.QUIT:
                    for i in self.__threads:
                        i.join()
                    pg.quit()
                    exit()

            self.update_status()
            if not self.__fin:
                self.update_stats()
                if not self.__running:
                    self.update_game()
                self.__game.update_screen(self.__widgets, self.__background)
            else:
                if self.__win:
                    self.__sound.stop()
                    return False
                elif self.__lose:
                    self.__sound.stop()
                    return True
                self.__game.update_screen(widgets_fin, self.__background)

            pg.display.update()
