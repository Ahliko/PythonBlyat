from class_character import Character

class Preservation(Character):
    def protection(self, target : Character):
        target._shield = int(target._shield + (target._maxhp * (15/100)))
        self._ultime += 20
        return self._shield

    def ultime(self, target : []):
        if self._ultime >= 150:
            for i in target:
                i._shield = int(i._shield + (i._def * (40/100) + 20 ))
        else :
            print("Vous n'avez pas assez de points d'ultime")
            return
        self._ultime = 0
        

                

