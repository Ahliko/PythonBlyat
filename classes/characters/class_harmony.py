from __future__ import annotations
import random
from classes.class_character import Character

random.seed()


class Harmony(Character):

    def __init__(self, _id: int, name: str, critrate: int, critdmg: int):
        super().__init__(_id, name, critrate, critdmg)
        self.maxhp = 725
        self.hp = self.maxhp
        self.atk = 240
        self._def = 25
        self.maxultpts = 130
        self.speed = 11
        self.buf = {
            "id": 0,
            "ability": False,
            "atk": self.atk,
            "critrate": self.critrate,
            "critdmg": self.critdmg,
            "remaining": 0
        }

    def ability(self, target: Character, game):
        if target in game.monsters:
            target = [i for i in game.characters.values()][random.randint(0, len(game.characters) - 1)]
        if self.cooldown > 0:
            print("Vous ne pouvez pas utiliser cette compétence pour le moment")
            game.history.append("Vous ne pouvez pas utiliser cette compétence pour le moment")
            return self.cooldown
        if target.buf["remaining"] > 0:
            target.buf["remaining"] = 1
            print(f"Les stats de {target.name} ont déjà été améliorés ", end="")
            game.history.append(f"Les stats de {target.name} ont déjà été améliorés ")
            return
        print(f"{self.name} utilise sa compétence spéciale ! : Vitamines de Taurine")
        game.history.append(f"{self.name} utilise sa compétence spéciale ! : Vitamines de Taurine")
        print(f"Les stats de {target.name} ont été améliorés ", end="")
        game.history.append(f"Les stats de {target.name} ont été améliorés ")
        boost = random.randint(1, 3)
        if boost == 1:
            print(f"({target.critdmg} CRITDMG -> {target.critdmg + 20} CRITDMG)")
            game.history.append(f"({target.critdmg} CRITDMG -> {target.critdmg + 20} CRITDMG)")
            target.critdmg += 20
            target.buf["id"] = 1
        elif boost == 2:
            print(f"({target.critrate} CRITRATE -> {target.critrate + 35} CRITRATE)")
            game.history.append(f"({target.critrate} CRITRATE -> {target.critrate + 35} CRITRATE)")
            target.critrate += 35
            target.buf["id"] = 2
        elif boost == 3:
            print(f"({target.atk} ATK -> {int(target.atk + target.atk * (25 / 100))} ATK)")
            game.history.append(f"({target.atk} ATK -> {int(target.atk + target.atk * (25 / 100))} ATK)")
            target.atk += int((target.atk * (25 / 100)))
            target.buf["id"] = 3
        target.buf["remaining"] = 1
        target.buf["ability"] = True
        self.turn = False
        self.cooldown = 2
        self.add_ultpts(30)

    def ultime(self, target: [], game):
        if target in game.monsters:
            target = [i for i in game.characters.values()]
        if self.ultpts == self.maxultpts:
            print(f"{self.name} utilise son ultime ! : Overdose")
            game.history.append(f"{self.name} utilise son ultime ! : Overdose")
            for i in target:
                if i.is_alive:
                    i.atk += int(i.atk * (25 / 100))
                    i.critrate += 30
                    i.critdmg += 15
                    i.buf["remaining"] += 2
            self.turn = False
            print("Les stats de vos personnages ont été améliorés pour 2 tours (ATK +25%, CRITRATE +30, CRITDMG +15)")
            game.history.append(
                "Les stats de vos personnages ont été améliorés pour 2 tours (ATK +25%, CRITRATE +30, CRITDMG +15")
            self.ultpts = 0
        else:
            print("Vous n'avez pas assez de points d'ultime")
            game.history.append("Vous n'avez pas assez de points d'ultime")
