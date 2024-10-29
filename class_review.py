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
        return f"{self.name} lets out a thunderous roar!"

class FlyingDinosaur(Dinosaur):
    def __init__(self, name, species, diet, age, wing_span):
        super().__init__(name, species, diet, age)
        self.wing_span = wing_span

    def roar(self):
        return f"{self.name} screeches in the sky!"

class WaterDinosaur(Dinosaur):
    def __init__(self, name, species, diet, age, swim_speed):
        super().__init__(name, species, diet, age)
        self.swim_speed = swim_speed

    def roar(self):
        return f"{self.name} roars underwater, creating bubbles!"

# Create instances of Dinosaur and its subclasses
jack_black = Dinosaur("Jack Black", "Tyrannosaurus Rex", "Carnivore", 10)
rubeus = FlyingDinosaur("Rubeus", "Pterodactyl", "Carnivore", 5, wing_span=12)
hurley = WaterDinosaur("Hurley", "Mosasaurus", "Carnivore", 7, swim_speed=20)

# Test roar method (polymorphism)
print(jack_black.roar())   # Expected: Standard roar
print(rubeus.roar())       # Expected: Screeching sound for flying dinosaur
print(hurley.roar())       # Expected: Roaring underwater, that bubbles are made

# Test encapsulation (accessing age via getter and setter)
print(rubeus.get_age())     # Should return 5
rubeus.set_age(8)           # Update age to 8
print(rubeus.get_age())     # Verify update

# Test invalid age setting
hurley.set_age(-3)          # Expected: Print warning about invalid age

# Demonstrate object identity
hurley_clone = WaterDinosaur("Hurley", "Mosasaurus", "Carnivore", 7, swim_speed=20)
print(id(hurley) == id(hurley_clone))  # Expected: False since they are different instances
