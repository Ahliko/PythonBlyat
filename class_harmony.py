from __future__ import annotations
import random
from class_character import Character

random.seed()


class Harmony(Character):

    def __init__(self, name: str, critrate: int, critdmg: int):
        super().__init__(name, critrate, critdmg)
        self.maxhp = 700
        self.hp = self.maxhp
        self.atk = 50
        self._def = 25
        self.maxultpts = 130
        self.speed = 11
        self.competence_need_turn = 2

    def ability(self, target: Character):
        print(f"Les stats de {target.name} ont été améliorés ", end="")
        boost = random.randint(1, 3)
        if boost == 1:
            print(f"({target.critdmg} CRITDMG -> {target.critdmg + 20} CRITDMG)")
            target.critdmg += 20
            target.buf["id"] = 1
        elif boost == 2:
            print(f"({target.critrate} CRITRATE -> {target.critrate + 35} CRITRATE)")
            target.critrate += 35
            target.buf["id"] = 2
        elif boost == 3:
            print(f"({target.atk} ATK -> {int(target.atk + target.atk * (25 / 100))} ATK)")
            target.atk += int((target.atk * (25 / 100)))
            target.buf["id"] = 3
        target.buf["remaining"] = 1
        target.buf["ability"] = True 
        self.competence = False
        

    def ultime(self, target : []):
        if self.ultpts == self.maxultpts:
            print("UTILISATION DE LULTIME")
            for i in target:
                if i.is_alive:
                    i.atk += int(i.atk * (25 / 100))
                    i.critrate += 30
                    i.critdmg += 15
                    i.buf["remaining"] += 2
        else:
            print("Vous n'avez pas assez de points d'ultime")

