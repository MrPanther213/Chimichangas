import random

# Starting attributes
health = random.randint(7,10) * 10
gold = 0
strength = random.randint(12,17)
level = 1
monster_health = random.randint(15,25) * 1
damage = random.randint(strength - 5, strength + 5)
# Start the game
def display_character():
    print( "name: {name}", "weapon: {Weapon}", "hp: {health}", "gold: {gold}","Strength: {strength}","Level: {level}")
# Start the game
def main():
    start_game()

def start_game():
    print("Welcome to the dungeon!")
    name = input("What is your name, adventurer? ")
    weapon = input("What is your weapon of choice? ")
    print("Your journey begins!")
    print(f"Your name is {name}, your weapon of choice is {weapon}.")
    battle_mode()
    return True

def battle_mode():
     global health
     global monster_health
     global damage
     while monster_health > 0:
        print(f"A wild monster appears! It has {monster_health} health points.")
        player_choice = input("Do you want to attack(1) or Run(2)? ")
        if player_choice == "1":
            monster_health -= damage
            print(f"You hit the monster for {damage} damage!")
        if monster_health <= 0:
            print("You defeated the monster!")
            player_gold = random.randint(1,5) * 10
            gold += player_gold
            print(f"You found {player_gold} gold!")
            break
        monster_damage = random.randint(strength - 5, strength + 5)
        monster_health -= monster_damage
        print(f"The monster hits you for {monster_damage} damage!")
# Main game loop
if health <0:
     print("You have died!")

else:
     print("You have completed the dungeon!")
     print("Your final score is: ", gold)
     print("Game Over!")
     exit()

start_game()



#Press Enter to continue
#___ gold
        
    #Choice: ___

#a health potion. You restored ___ health
#Hello, ___
#In this dungeon, you will fight three monsters.
#If you survive to the end, treasure awaits!
#You have your trusty ___, I see.
#Good. You will need it.
#Press Enter when you are ready to begin...
#You made it to the treasure! You found ___ gold!
#You didn't find the treasure, but you survived to fight again another day...
#You fought as best you could, but didn't make it. 
#The treasure waits for the next adventurer...

# Write your functions herestart_game()
