from __future__ import annotations
import random
from class_character import Character

from class_hunt import Hunt

random.seed()


class Harmony(Character):

    @staticmethod
    def ability(target: Character):
        boost = random.randint(1, 3)
        if boost == 1:
            target.critdmg += 20
        elif boost == 2:
            target.critrate += 35
        elif boost == 3:
            target.atk += int((target.atk * (25 / 100)))

    def ultime(self, target : []):
        if self.ultpts == self.maxultpts:
            print("UTILISATION DE LULTIME")
            for i in target:
                if i.is_alive:
                    i.atk += int(i.atk * (25 / 100))
                    i.critrate += 30
                    i.critdmg += 15
                    i.buf["remaining"] = 2
        else:
            print("Vous n'avez pas assez de points d'ultime")

