class Bender:
    def __init__(self, name, element):
        self.name=name
        self.element=element

    def bend(self):
        return f"{self.name} is bending {self.element}"
    
class Firebender(Bender):
    def __init__(self, name):
        super().__init__(name, "Fire")

class Earthbender(Bender):
    def __init__(self, name):
        super().__init__(name, "Earth")

class Waterbender(Bender):
    def __init__(self, name):
        super().__init__(name, "Water")

class Airbender(Bender):
    def __init__(self, name):
        super().__init__(name, "Air")

Zuko= Firebender

Toph= Earthbender

print(Zuko.bend())
print(Toph.bend())
