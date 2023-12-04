from random import randint

from class_character import Character
from game import Game


class Abundance(Character):
    def __init__(self, _id: int, name: str, critrate: int, critdmg: int):
        super().__init__(_id, name, critrate, critdmg)
        self.maxhp = 960
        self.hp = self.maxhp
        self.atk = 190
        self._def = 20
        self.maxultpts = 125
        self.speed = 10
        self.buf = {
            "id": 0,
            "ability": False,
            "atk": self.atk,
            "critrate": self.critrate,
            "critdmg": self.critdmg,
            "remaining": 0
        }

    def ability(self, target: Character, game: Game):
        if target in game.monsters:
            target = [i for i in game.characters.values()][randint(0, len(game.characters) - 1)]
        if self.cooldown > 0:
            print("Vous ne pouvez pas utiliser cette compétence pour le moment")
            game.history.append("Vous ne pouvez pas utiliser cette compétence pour le moment")
            return self.cooldown
        heal = int(target.maxhp * (25 / 100))
        print(f"{self.name} utilise sa compétence spéciale ! : Prière de la fleur de l'abîme \n"
              f"{target.name} se fait soigne de 15% de ses HP max (+{heal})")
        game.history.append(f"{self.name} utilise sa compétence spéciale ! : Prière de la fleur de l'abîme")
        game.history.append(f"{target.name} se fait soigne de 15% de ses HP max (+{heal})")
        if target.maxhp <= heal + target.hp:
            target.hp = target.maxhp
        else:
            target.hp += heal
        self.turn = False
        self.cooldown = 3
        self.add_ultpts(30)

    def ultime(self, target: [], game: Game):
        if target in game.monsters:
            target = [i for i in game.characters.values()]
        if self.ultpts == self.maxultpts:
            print(f"{self.name} utilise son ultime ! : Talisman de guérison")
            game.history.append(f"{self.name} utilise son ultime ! : Talisman de guérison")
            for i in target:
                heal = int(i.maxhp * (15 / 100) + 40)
                if i.maxhp <= heal + i.hp:
                    i.hp = i.maxhp
                else:
                    i.hp += heal
            print("Tous les personnages ont été soignés de 15% de leurs HP max +40 pv")
            game.history.append("Tous les personnages ont été soignés de 15% de leurs HP max +40 pv")
            self.turn = False
            self.ultpts = 0
        else:
            print("Vous n'avez pas assez de points d'ultime")
            game.history.append("Vous n'avez pas assez de points d'ultime")
