from class_character import Character
import random
import pygame

from game import Game


class Monster(Character):
    def __init__(self, _id, name, critrate, critdmg):
        super().__init__(_id, name, critrate, critdmg)

    def choice(self, lst: list, game: Game):
        ch = random.randint(0, 100)
        charach_to_att = random.randint(0, len(lst) - 1)
        if ch < 60:
            self.attack(lst[charach_to_att], game)
        else:
            if self.cooldown > 0:
                self.attack(lst[charach_to_att], game)
            else:
                self.ability(lst, game)
