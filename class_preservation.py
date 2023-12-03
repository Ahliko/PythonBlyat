from random import randint

from class_character import Character


class Preservation(Character):

    def __init__(self, _id: int, name: str, critrate: int, critdmg: int):
        super().__init__(_id, name, critrate, critdmg)
        self.maxhp = 750
        self.hp = self.maxhp
        self.atk = 200
        self._def = 120
        self.maxultpts = 130
        self.speed = 9

    def ability(self, target: Character, game):
        if target in game.monsters:
            target = [i for i in game.characters.values()][randint(0, len(game.characters) - 1)]
        if self.cooldown > 0:
            print("Vous ne pouvez pas utiliser cette compétence pour le moment")
            return self.cooldown
        target.shield = int(target.maxhp * (15 / 100))
        self.ultpts += 20
        self.cooldown = 3
        return self.shield

    def ultime(self, target: list, game):
        if target in game.monsters:
            target = [i for i in game.characters.values()]
        if self.ultime == self.maxultpts:
            for i in target:
                i.shield = int(i.shield + (i._def * (40 / 100) + 20))
            self.ultpts = 0

