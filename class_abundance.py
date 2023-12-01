from random import randint

from class_character import Character
from game import Game

class Abundance(Character):
    def __init__(self, name: str, critrate: int, critdmg: int):
        super().__init__(name, critrate, critdmg)
        self.maxhp = 650
        self.hp = self.maxhp
        self.atk = 30
        self._def = 20
        self.maxultpts = 125
        self.speed = 10

    def ability(self, target: Character, game: Game):
        if target in game.monsters:
            target = [i for i in game.characters.values()][randint(0, len(game.characters) - 1)]
        if self.cooldown > 0:
            print("Vous ne pouvez pas utiliser cette compétence pour le moment")
            return self.cooldown
        heal = int(target.maxhp * (15 / 100))
        print(f"{self.name} utilise sa compétence spéciale ! \n"
              f"{target.name} se fait soigne de 15% de ses HP max (+{heal})")
        if target.maxhp <= heal + target.hp:
            target.hp = target.maxhp
        else:
            target.hp = heal
        self.cooldown = 3
        

    def ultime(self, target: [], game: Game):
        if target in game.monsters:
            target = [i for i in game.characters.values()]
        if self.ultpts == self.maxultpts:
            for i in target:
                heal = int(i.hp + (i.maxhp * (15 / 100) + 40))
                if i.maxhp <= heal:
                    i.hp = i.maxhp
                else:
                    i.hp = heal
        else:
            print("Vous n'avez pas assez de points d'ultime")
