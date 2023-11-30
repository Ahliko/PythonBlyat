from class_character import Character

class Abundance(Character):
    def __init__(self, name: str, critrate: int, critdmg: int):
        super().__init__(name, critrate, critdmg)
        self.maxhp = 650
        self.hp = self.maxhp
        self.atk = 30
        self._def = 20
        self.maxultpts = 125
        self.speed = 10

    @staticmethod
    def ability(target: Character):
        heal = int(target.hp + (target.maxhp * (15 / 100)))
        if target.maxhp <= heal:
            target.hp = target.maxhp
        else:
            target.hp = heal

    def ultime(self, target: []):
        if self.ultpts == self.maxultpts:
            for i in target:
                heal = int(i.hp + (i.maxhp * (15 / 100) + 40))
                if i.maxhp <= heal:
                    i.hp = i.maxhp
                else:
                    i.hp = heal
        else:
            print("Vous n'avez pas assez de points d'ultime")
