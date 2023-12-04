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
            target = [i for i in game.characters.values()][randint(0, len(game.characters) - 1)]
        if self.cooldown > 0:
            print("Vous ne pouvez pas utiliser cette compétence pour le moment")
            game.history.append("Vous ne pouvez pas utiliser cette compétence pour le moment")
            return self.cooldown
        print(f"{self.name} utilise sa compétence spéciale ! : Voix du Protecteur")
        game.history.append(f"{self.name} utilise sa compétence spéciale ! : Voix du Protecteur")
        target.shield = int(target.maxhp * (15 / 100))
        self.add_ultpts(30)
        print(f"{target.name} se fait un bouclier de {target.shield} HP")
        game.history.append(f"{target.name} se fait un bouclier de {target.shield} HP")
        self.cooldown = 3
        self.turn = False
        return self.shield

    def ultime(self, target: list, game):
        if target in game.monsters:
            target = [i for i in game.characters.values()]
        if self.ultime == self.maxultpts:
            print(f"{self.name} utilise son ultime ! : Invocation du Protecteur")
            game.history.append(f"{self.name} utilise son ultime ! : Invocation du Protecteur")
            for i in target:
                i.shield = int(i.shield + (i._def * (40 / 100) + 20))
            print("Tous les personnages recoivent un bouclier de 40% de leur DEF +20 HP")
            game.history.append("Tous les personnages recoivent un bouclier de 40% de leur DEF +20 HP")
            self.ultpts = 0
            self.turn = False
        else:
            print("Vous n'avez pas assez de points d'ultime")
            game.history.append("Vous n'avez pas assez de points d'ultime")
            return

