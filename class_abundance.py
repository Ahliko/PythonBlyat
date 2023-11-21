from class_character import Character

class Abundance(Character):
    def heal(self, target : Character):
        heal =  int(target._hp + (target._maxhp * (15/100)))
        if target._maxhp < target._hp + heal:
            target._hp = target._maxhp
        else :
            target._hp += heal
