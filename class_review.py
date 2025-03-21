# dinosaur.py

class Dinosaur:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species
        self.diet = diet
        self._age = age   

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Invalid age: Age must be a non-negative number")

    def roar(self):
        return f"{self.name} roars"

class FlyingDinosaur(Dinosaur):
    def __init__(self, name, species, diet, age, wing_span):
        super().__init__(name, species, diet, age)
        self.wing_span = wing_span

    def roar(self):
        return f"{self.name} rawrs"

class WaterDinosaur(Dinosaur):
    def __init__(self, name, species, diet, age, swim_speed):
        super().__init__(name, species, diet, age)
        self.swim_speed = swim_speed

    def roar(self):
        return f"{self.name} bubble noises"

Rex = Dinosaur("Rex", "Tyrannosaurus Rex", "Carnivore", 10)
Thunderclap = FlyingDinosaur("Thunderclap", "Pterodactyl", "Carnivore", 5, wing_span=12)
Meuse = WaterDinosaur("Meuse", "Mosasaurus", "Carnivore", 7, swim_speed=20)

# Test roar method 
print(Rex.roar())   # Expected to have a standard roar
print(Thunderclap.roar())       # Screeching roar for flying dinosaur
print(Meuse.roar())       #Roaring underwater, where bubbles are made

# Test encapsulation
print(Thunderclap.get_age())     
Thunderclap.set_age(8)           
print(Thunderclap.get_age())    

# Test invalid age setting
Meuse.set_age(3)          # Expected: Print warning about invalid age

# Demonstrate object identity
Meuse_clone = WaterDinosaur("Meuse", "Mosasaurus", "Carnivore", 7, swim_speed=20)
print(id(Meuse) == id(Meuse_clone))  # Expecting to be False since they are different


