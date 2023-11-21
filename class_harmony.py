from __future__ import annotations
import random
from class_character import Character

random.seed()

class Harmony(Character):
    def buf_ability(self, target: Character):
        boost = random.randint(1, 3)
        if boost == 1:
            target._critdmg += 20
        elif boost == 2:
            target._critrate += 35
        elif boost == 3:
            target._atk += int((target._atk * (25 / 100)))
        pass