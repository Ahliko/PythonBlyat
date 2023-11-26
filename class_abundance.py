from class_character import Character


class Abundance(Character):
    @staticmethod
    def heal(target: Character):
        heal = int(target.hp + (target.maxhp * (15 / 100)))
        if target.maxhp <= heal:
            target.hp = target.maxhp
        else:
            target.hp = heal

    @staticmethod
    def use_ultime(self, target: []):
        heal = int(target.hp + (target.maxhp * (15 / 100) + 40))
        if self.ultime >= 130:
            for i in target:
                if i.maxhp <= heal:
                    i.hp = i.maxhp
                else:
                    i.hp = heal
        else:
            print("vous n'avez pas assez de points d'ultime")


if __name__ == "__main__":
    abd = Abundance("Abundance", 500, 10, 10)
    abd.hp = 250
    abd.heal(abd)
    print(abd.hp)
