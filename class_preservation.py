from class_character import Character

class Preservation(Character):
    def protection(self, target : Character):
        target._shield = int(target._shield + (target._maxhp * (15/100)))
        return self._shield
    
