from __future__ import annotations
import random
from class_character import Character

random.seed()

class Harmony(Character):
    def buf_ability(self, target: Character):
        boost = random.randint(1, 3)
        if boost == 1: # HP Boost
            print("HPMAX BOOSTED")
            target._maxhp += int((target._maxhp * (20 / 100)))
        elif boost == 2: # DEF Boost
            print("DEF BOOSTED")
            target._def += int((target._def * (20 / 100)))
        elif boost == 3: # ATK Boost
            print("ATK BOOSTED")
            target._atk += int((target._atk * (20 / 100)))
        pass