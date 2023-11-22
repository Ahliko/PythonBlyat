from class_character import Character


class Abundance(Character):
    @staticmethod
    def heal(target: Character):
        heal = int(target.hp + (target.maxhp * (15 / 100)))
        if target.maxhp <= heal:
            target.hp = target.maxhp
        else:
            target.hp = heal


if __name__ == "__main__":
    abd = Abundance("Abundance", 500, 10, 10)
    abd.hp = 250
    abd.heal(abd)
    print(abd.hp)
