from __future__ import annotations
import random
from class_character import Character

random.seed()


class Harmony(Character):
    @staticmethod
    def buf_ability(target: Character):
        boost = random.randint(1, 3)
        if boost == 1:
            target.critdmg += 20
        elif boost == 2:
            target.critrate += 35
        elif boost == 3:
            target.atk += int((target.atk * (25 / 100)))
