from __future__ import annotations
from class_character import Character
import random

class Chimere(Character):
    random.seed()

    def competence(self, target : list):
        self.aoe(target)

    def choice(self, lst : list):
        ch = random.randint(0, 100)
        charach_to_att = random.randint(0, len(lst)-1)
        if ch < 80:
            print("attack")
            self.attack(lst[charach_to_att])
        else:
            print("comp")
            self.competence(lst)

Chi = Chimere("Scar", 100, 12, 2)
Lelfe = Character("ed", 100, 12, 4)
Nain = Character("al", 100, 12, 2)
lst = [Lelfe, Nain]
Chi.choice(lst)