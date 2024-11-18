import random

# Define lists of random elements for the story
characters = ["Sarah", "John", "Emily", "Michael", "Daniel", "Alice", "Ethan", "Sophie"]
locations = ["an old abandoned house", "a dark forest", "a desolate cabin", "an eerie graveyard", "a haunted mansion"]
objects = ["a cursed mirror", "an ancient book", "a rusted key", "a mysterious photograph", "a strange locket"]
creatures = ["a ghostly figure", "a shadowy demon", "a vengeful spirit", "a lurking werewolf", "a twisted witch"]
events = ["the lights flickered", "a loud scream pierced the air", "whispers echoed from nowhere", "footsteps followed close behind", "the door slammed shut", "an icy wind blew through the room"]
twists = ["they found an unexpected ally", "another creature emerged from the shadows", "they discovered a hidden passage", "the cursed object began to glow", "a familiar voice called their name", "they realized they were not alone"]
endings = ["and they were never seen again.", "but no one believed their story.", "and the nightmare continued.", "and their fate remained a mystery."]

# Define story templates
templates = [
    "{character} went to {location} one evening. As they explored, they found {object}. Suddenly, {creature} appeared, and {event} {ending}",
    "It was a cold night when {character} decided to visit {location}. They stumbled upon {object}, unaware that {creature} was watching. Soon after, {event} {ending}",
    "{character} always knew something was wrong with {location}. One night, they found themselves face to face with {creature}. As {event}, they realized they had made a grave mistake. {ending}",
    "Nobody believed {character} when they said {location} was cursed. But one night, they discovered {object}. When {creature} appeared and {event}, it was too late. {ending}"
]

# Function to generate the first part of a random scary story
def generate_initial_story():
    story = random.choice(templates).format(
        character=random.choice(characters),
        location=random.choice(locations),
        object=random.choice(objects),
        creature=random.choice(creatures),
        event=random.choice(events),
        ending=""
    )
    return story

# Function to add to the story with more twists and events
def add_to_story(current_story):
    # Randomly add a twist, new event, or a sudden appearance of another creature
    addition = random.choice(twists) + ". " + random.choice(events) + "."
    return current_story + " " + addition

# Function to end the story
def end_story(current_story):
    return current_story + " " + random.choice(endings)

# Main function to manage story continuation
if __name__ == "__main__":
    story = generate_initial_story()
    print("Here's the beginning of your scary story:")
    print(story)
    
    while True:
        next_action = input("\nWhat would you like to do next? Type 'add' to continue the story, 'end' to finish the story, or 'quit' to exit: ").lower()
        
        if next_action == 'add':
            story = add_to_story(story)
            print("\nThe story continues:")
            print(story)
        elif next_action == 'end':
            story = end_story(story)
            print("\nThe story ends:")
            print(story)
            break
        elif next_action == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please type 'add', 'end', or 'quit'.")
