class Animal:
    def __init__(self, name, habitat, sound):
        self._name = name         # Encapsulated attribute
        self._habitat = habitat   # Encapsulated attribute
        self._sound = sound       # Encapsulated attribute


    # Getter methods to access encapsulated attributes
    def get_name(self):
        return self._name


    def get_habitat(self):
        return self._habitat

 # Method to output the animal’s sound
    def speak(self):
        return f"{self._name} makes a sound: {self._sound}"

# Dog subclass inheriting from Animal
class Dog(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, habitat, "Woof!")  # Dog-specific sound


    # Overriding the speak method to show polymorphism
    def speak(self):
        return f"{self.get_name()} says: {self._sound} loudly in {self.get_habitat()}"


    # Unique Dog behavior
    def fetch(self):
        return f"{self.get_name()} is fetching the ball!"




# Cat subclass inheriting from Animal
class Cat(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, habitat, "Meow")  # Cat-specific sound


    # Overriding the speak method to show polymorphism
    def speak(self):
          return f"{self.get_name()} softly says: {self._sound} in {self.get_habitat()}"


    # Unique Cat behavior
    def climb(self):
        return f"{self.get_name()} is climbing a tree!"

# Testing the Animal, Dog, and Cat classes
def main():
    # Create Dog and Cat objects
    buddy = Dog("Buddy", "the backyard")
    whiskers = Cat("Whiskers", "the living room")


    # Call the speak method on each object
    print(buddy.speak())      # Demonstrates polymorphism in the Dog class
    print(buddy.fetch())       # Dog-specific behavior


    print(whiskers.speak())    # Demonstrates polymorphism in the Cat class
    print(whiskers.climb())    # Cat-specific behavior


# Run the main function
if __name__ == "__main__":
    main()
