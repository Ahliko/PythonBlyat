from __future__ import annotations
import random
from class_character import Character

random.seed()


class Harmony(Character):

    @staticmethod
    def ability(target: Character):
        print(f"Les stats de {target.name} ont été améliorés ", end="")
        boost = random.randint(1, 3)
        if boost == 1:
            print(f"({target.critdmg} CRITDMG -> {target.critdmg + 20} CRITDMG)")
            target.critdmg += 20
        elif boost == 2:
            print(f"({target.critrate} CRITRATE -> {target.critrate + 35} CRITRATE)")
            target.critrate += 35
        elif boost == 3:
            print(f"({target.atk} ATK -> {int(target.atk + target.atk * (25 / 100))} ATK)")
            target.atk += int((target.atk * (25 / 100)))
        target.buf["remaining"] = 1

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

