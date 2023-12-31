import pygame as pg
from widgets.CustomButton import Button
from widgets.CustomLabel import Label
from widgets.CustomListLabel import ListLabel
from lib.game import Game
from lib.engine import Engine


class FightMenu:
    def __init__(self, game: Game):
        self.__sound_run = False
        self.__turn_fin = True
        self.__game = game
        self.__engine = Engine(self.__game)
        self.__quit = False
        self.__widgets = None
        self.__fin = False
        self.__win = False
        self.__lose = False
        self.__choice = None
        self.__func = None
        self.__running = False
        self.__background = pg.image.load("assets/Fight.png")
        self.__game.play_sound_fight()

    def show(self, carac, enable=False):
        if type(carac).__name__ == "Hunt" or not enable:
            self.__widgets[9].text = self.__game.monsters[0].name
            self.__widgets[10].text = self.__game.monsters[1].name
            self.__widgets[11].text = self.__game.monsters[2].name
        else:
            self.__widgets[9].text = [i for i in self.__game.characters.values()][0].name
            self.__widgets[10].text = [i for i in self.__game.characters.values()][1].name
            self.__widgets[11].text = [i for i in self.__game.characters.values()][2].name
        for i in self.__widgets[:3]:
            i.hide()
        self.__widgets[9].show()
        self.__widgets[10].show()
        self.__widgets[11].show()
        self.__widgets[12].show()
        self.__widgets[-1].text = f"Choose your target !"
        pg.display.update()

    def hide(self):
        for i in self.__widgets[:3]:
            i.show()
        self.__widgets[9].hide()
        self.__widgets[10].hide()
        self.__widgets[11].hide()
        self.__widgets[12].hide()

    def on_attack(self):
        self.__running = True
        next_carac = self.get_character(self.__engine.next_character(self.__game.all_characters))
        if next_carac in self.__game.characters.values():
            self.show(next_carac)
            if self.__choice is not None:
                target_monster = self.__game.monsters[self.__choice]
                if target_monster.is_alive():
                    self.__game.all_characters[self.__game.all_characters.index(next_carac)].attack(
                        target_monster, self.__game)
                self.__choice = None
                self.hide()
                self.__func = None
        self.__running = False

    def on_ability(self):
        self.__running = True
        next_carac = self.get_character(self.__engine.next_character(self.__game.all_characters))
        if next_carac in self.__game.characters.values():
            self.show(next_carac, True)
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
                self.show(next_carac, True)
                if self.__choice is None:
                    return
                target = [i for i in self.__game.monsters][self.__choice]
                self.__choice = None
                self.hide()
                self.__func = None
            else:
                target = [i for i in self.__game.characters.values() if i.is_alive()]
                self.__func = None
            self.__game.all_characters[self.__game.all_characters.index(next_carac)].ultime(
                target, self.__game)
        self.__running = False

    def __on_click_attacks(self):
        self.__game.play_sound_button()
        self.__func = self.on_attack
        self.on_attack()

    def __on_click_ability(self):
        self.__game.play_sound_button()
        self.__func = self.on_ability
        self.on_ability()

    def __on_click_ultime(self):
        self.__game.play_sound_button()
        self.__func = self.on_ultime
        self.on_ultime()

    def __on_click_back_action(self):
        self.__game.play_sound_button()
        self.__func = None
        self.__choice = None
        self.hide()

    def __on_click_next(self):
        self.__game.play_sound_button()
        if self.__engine.next_character(self.__game.all_characters) is None:
            self.__engine.next_turn(self.__game.all_characters)
        self.__widgets[-2].hide()
        for i in self.__widgets[:3]:
            i.show()

    def __disable(self):
        self.__game.play_sound_button()
        self.__game.stop_sound_fight()
        if self.__engine.is_win([i for i in self.__game.characters.values()]):
            self.__win = True
        elif self.__engine.is_win(self.__game.monsters):
            self.__lose = True

    def __on_click_one(self):
        self.__game.play_sound_button()
        self.__choice = 0

    def __on_click_two(self):
        self.__game.play_sound_button()
        self.__choice = 1

    def __on_click_three(self):
        self.__game.play_sound_button()
        self.__choice = 2

    def __widgets_init(self):
        bouton_attack_de_base_width = (self.__game.largeur / 2)
        bouton_attack_de_base_height = (self.__game.hauteur / 2)
        bouton_competences_width = (self.__game.largeur / 2)
        bouton_competences_height = (self.__game.hauteur / 2) + 60
        bouton_ultime_width = (self.__game.largeur / 2)
        bouton_ultime_height = (self.__game.hauteur / 2) + 120
        bouton_attack_de_base = Button(bouton_attack_de_base_width, bouton_attack_de_base_height, 300, 50,
                                       self.__game.font,
                                       'Attack de base',
                                       self.__on_click_attacks, False, ('#2a75a1', '#666666', '#333333'), center=True)
        bouton_competences = Button(bouton_competences_width, bouton_competences_height, 300, 50,
                                    self.__game.font,
                                    'Compétences',
                                    self.__on_click_ability, False, ('#2a75a1', '#666666', '#333333'), center=True)
        bouton_ultime = Button(bouton_ultime_width, bouton_ultime_height, 300, 50,
                               self.__game.font,
                               'Ultime',
                               self.__on_click_ultime, False, ('#2a75a1', '#666666', '#333333'), center=True)
        bouton_1 = Button(bouton_attack_de_base_width, bouton_attack_de_base_height, 300, 50,
                          self.__game.font,
                          'Target 1',
                          self.__on_click_one, False, ('#2a75a1', '#666666', '#333333'), hide=True, center=True)
        bouton_2 = Button(bouton_competences_width, bouton_competences_height, 300, 50,
                          self.__game.font,
                          'Target 2',
                          self.__on_click_two, False, ('#2a75a1', '#666666', '#333333'), hide=True, center=True)
        bouton_3 = Button(bouton_ultime_width, bouton_ultime_height, 300, 50,
                          self.__game.font,
                          'Target 3',
                          self.__on_click_three, False, ('#2a75a1', '#666666', '#333333'), hide=True, center=True)
        label_stats = Label("Stats", int(self.__game.largeur / self.__game.hauteur * 20), (0, 0, 0),
                            (self.__game.largeur / 5 * 2, self.__game.hauteur / 2 + 350),
                            None, False)
        label_stats2 = Label("Stats", int(self.__game.largeur / self.__game.hauteur * 20), (0, 0, 0),
                             (self.__game.largeur / 5 * 2, self.__game.hauteur / 2 + 400),
                             None, False)
        label_stats3 = Label("Stats", int(self.__game.largeur / self.__game.hauteur * 20), (0, 0, 0),
                             (self.__game.largeur / 5 * 2, self.__game.hauteur / 2 + 450),
                             None, False)
        label_monster_stats = Label("Stats_ennemi", int(self.__game.largeur / self.__game.hauteur * 20), (0, 0, 0),
                                    (self.__game.largeur / 3 * 2, self.__game.hauteur / 10),
                                    None, False)
        label_monster_stats2 = Label("Stats_ennemi", int(self.__game.largeur / self.__game.hauteur * 20), (0, 0, 0),
                                     (self.__game.largeur / 3 * 2, self.__game.hauteur / 10 + 50),
                                     None, False)
        label_monster_stats3 = Label("Stats_ennemi", int(self.__game.largeur / self.__game.hauteur * 20), (0, 0, 0),
                                     (self.__game.largeur / 3 * 2, self.__game.hauteur / 10 + 100),
                                     None, False)
        label_status = Label("Status", int(self.__game.largeur / self.__game.hauteur * 20), (0, 0, 0),
                             (bouton_attack_de_base_width - int(self.__game.largeur / self.__game.hauteur * 20),
                              bouton_attack_de_base_height - 100),
                             None, False)
        back_action = Button(bouton_ultime_width, bouton_ultime_height + 60, 200, 40, self.__game.font, 'Back',
                             self.__on_click_back_action, False, ('#2a75a1', '#666666', '#333333'), center=True,
                             hide=True)

        next_turn = Button(self.__game.largeur / 2, self.__game.hauteur / 2, 200, 40, self.__game.font,
                           'Next Turn',
                           self.__on_click_next, False, ('#2a75a1', '#666666', '#333333'), center=True, hide=True)
        history = ListLabel("History", self.__game.history, int(self.__game.largeur / self.__game.hauteur * 20),
                            (0, 0, 0),
                            (10, 10), None,
                            False)

        return [bouton_attack_de_base, bouton_competences, bouton_ultime, label_stats, label_stats2, label_stats3,
                label_monster_stats, label_monster_stats2, label_monster_stats3, bouton_1, bouton_2, bouton_3,
                back_action, history, next_turn, label_status]

    def __widgets_pos_update(self):
        self.__widgets[0].update_pos((self.__game.largeur / 2), (self.__game.hauteur / 2))
        self.__widgets[1].update_pos((self.__game.largeur / 2), (self.__game.hauteur / 2) + 60)
        self.__widgets[2].update_pos((self.__game.largeur / 2), (self.__game.hauteur / 2) + 120)
        self.__widgets[3].update_pos(self.__game.largeur / 5 * 2, self.__game.hauteur / 2 + 350)
        self.__widgets[4].update_pos(self.__game.largeur / 5 * 2, self.__game.hauteur / 2 + 400)
        self.__widgets[5].update_pos(self.__game.largeur / 5 * 2, self.__game.hauteur / 2 + 450)
        self.__widgets[6].update_pos(self.__game.largeur / 5 * 3, self.__game.hauteur / 10)
        self.__widgets[7].update_pos(self.__game.largeur / 5 * 3, self.__game.hauteur / 10 + 50)
        self.__widgets[8].update_pos(self.__game.largeur / 5 * 3, self.__game.hauteur / 10 + 100)
        self.__widgets[9].update_pos((self.__game.largeur / 2), (self.__game.hauteur / 2))
        self.__widgets[10].update_pos((self.__game.largeur / 2), (self.__game.hauteur / 2) + 60)
        self.__widgets[11].update_pos((self.__game.largeur / 2), (self.__game.hauteur / 2) + 120)
        self.__widgets[12].update_pos((self.__game.largeur / 2), (self.__game.hauteur / 2) + 120 + 60)
        self.__widgets[13].update_pos_all(10, 10)
        self.__widgets[14].update_pos((self.__game.largeur / 2), (self.__game.hauteur / 2) + 120)
        self.__widgets[15].update_pos((self.__game.largeur / 2) - int(self.__game.largeur / self.__game.hauteur * 20),
                                      (self.__game.hauteur / 2) - 100)

    def get_character(self, id):
        for i in range(len(self.__game.all_characters)):
            if self.__game.all_characters[i].id == id:
                return self.__game.all_characters[i]

    def update_stats(self):
        for i in range(len(self.__game.all_characters)):
            self.__widgets[
                i + 3].text = f"{self.get_character(i + 1).name} : {self.get_character(i + 1).hp}/{self.get_character(i + 1).maxhp} HP | {self.get_character(i + 1).shield} SHIELD | {self.get_character(i + 1).ultpts}/{self.get_character(i + 1).maxultpts} ULTPTS | {self.get_character(i + 1).cooldown} CD"

    def update_status(self):
        if self.__func is not None:
            self.__widgets[-1].text = f"Choose your target !"
            return
        if self.__engine.is_win([i for i in self.__game.characters.values()]):
            self.__fin = True
            self.__game.stop_sound_fight()
            if not self.__sound_run:
                self.__sound_run = True
                self.__game.play_sound_lose_fight()
            self.__widgets[-1].text = f"Vous avez perdu !"
        elif self.__engine.is_win([i for i in self.__game.monsters]):
            self.__fin = True
            self.__game.stop_sound_fight()
            if not self.__sound_run:
                self.__sound_run = True
                self.__game.play_sound_win_fight()
            self.__widgets[-1].text = f"Vous avez gagné !"
        else:
            self.__fin = False
            try:
                self.__widgets[
                    -1].text = f"{self.get_character(self.__engine.next_character(self.__game.all_characters)).name}'s turn !"
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
        print(len(self.__widgets))
        self.__game.update_screen(self.__widgets, self.__background)
        pg.display.flip()
        self.__engine.final_list()
        self.__game.history = []
        self.__engine.reset_cooldown(self.__game.all_characters)
        self.__engine.reset_buf([i for i in self.__game.characters.values()])
        widgets_fin = [self.__widgets[-1],
                       Button((self.__game.largeur / 2), (self.__game.hauteur / 2) + 50, 400, 50, self.__game.font,
                              'Return to the Dungeon', self.__disable, False, ('#2a75a1', '#666666', '#333333'),
                              center=True)]
        while not self.__quit:
            self.__game.handle_fullscreen()
            widgets_fin[1].update_pos((self.__game.largeur / 2), (self.__game.hauteur / 2) + 50)
            if self.__func is not None:
                self.__func()
            self.__game.clock.tick(self.__game.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
                elif event.type == pg.QUIT:
                    pg.quit()
                    exit()

            self.update_status()
            if not self.__fin:
                self.update_stats()
                if not self.__running and self.__engine.next_character(self.__game.all_characters) is not None:
                    self.update_game()
                elif self.__engine.next_character(self.__game.all_characters) is None:
                    self.__widgets[-2].show()
                    for i in self.__widgets[:3]:
                        i.hide()
                self.__widgets_pos_update()
                self.__widgets[13].text = self.__game.history
                self.__game.update_screen(self.__widgets, self.__background)
            else:
                if self.__win:
                    self.__game.stop_sound_fight()
                    self.__game.stop_sound_lose_fight()

                    return False
                elif self.__lose:
                    self.__game.stop_sound_fight()
                    self.__game.stop_sound_win_fight()

                    return True
                self.__game.update_screen(widgets_fin, self.__background)

            pg.display.update()
