# dinosaur.py

class Dinosaur:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species
        self.diet = diet
        self._age = age  # Encapsulated age attribute

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

# Create instances of Dinosaur and its subclasses
Rex = Dinosaur("Rex", "Tyrannosaurus Rex", "Carnivore", 10)
Thunderclap = FlyingDinosaur("Thunderclap", "Pterodactyl", "Carnivore", 5, wing_span=12)
Meuse = WaterDinosaur("Meuse", "Mosasaurus", "Carnivore", 7, swim_speed=20)

# Test roar method (polymorphism)
print(Rex.roar())   # Expected: Standard roar
print(Thunderclap.roar())       # Expected: Screeching sound for flying dinosaur
print(Meuse.roar())       # Expected: Roaring underwater, that bubbles are made

# Test encapsulation (accessing age via getter and setter)
print(Thunderclap.get_age())     # Should return 5
Thunderclap.set_age(8)           # Update age to 8
print(Thunderclap.get_age())     # Verify update

# Test invalid age setting
Meuse.set_age(3)          # Expected: Print warning about invalid age

# Demonstrate object identity
Meuse_clone = WaterDinosaur("Meuse", "Mosasaurus", "Carnivore", 7, swim_speed=20)
print(id(Meuse) == id(Meuse_clone))  # Expected: False since they are different instances


