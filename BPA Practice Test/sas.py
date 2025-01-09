import random

name = ""
medical_supplies = random.randint(50, 100)
energy = random.randint(70, 100)
ewoks_treated = 0

def display_status():
    print("--Status--")
    print("Medic", name, "has", medical_supplies, "supplies,", energy, "energy,", "and has treated", ewoks_treated, "Ewoks.")
    pass


def treat_ewok():
    
    encounter_ewok.random = random.randint('minor', 'Moderate', 'Severe')
    encounter_ewok.condition = random.choice(['minor', 'Moderate', 'Severe'])
    if encounter_ewok.condition == "Minor": 
        medical_supplies() -= 10
        energy() = +5
    elif encounter_ewok.condition == "Moderate":
        medical_supplies() -= 20
    elif encounter_ewok.condition == "Severe":
        medical_supplies() -= 30
        energy() = -10
    if medical_supplies <= 0:
        return f"Medic {name} is low on supplies. Unable to treat Ewok."
    if energy <= 0:
        return f"Medic {name} is low on energy. Unable to treat Ewok."
    print("Medic", name, "treated an Ewok.")
ewoks_treated = +1
pass


def start_shift():
    global name
    print("Welcome to the forest moon of Endor!")
    name = input("Enter your name, Medic: ")
    print(f"Welcome, Medic {name}. Ewoks are depending on you.")
    input("Press Enter when ready to begin your shift...")
   
    for _ in range(3):
        encounter_ewok()
        print(medical_supplies + energy)
        if medical_supplies <= 0 or energy <= 0:
            print("Medic", name, "is low on supplies or energy. Shutting down...")
            break
        display_status
        pass
    end_shift()
    pass


def encounter_ewok():
    print("An injured Ewok needs your help!")
    while True:
        try: 
             user_input = input("Do you want to treat the Ewok ('1') or skip ('2')? ")

             if user_input == '1':
                 print(treat_ewok())
                 break
             elif user_input == '2':
                 print("The injured Ewok has been skipped.")
                 break
             else:
                 raise ValueError("Invalid input. Please enter '1' or '2'.")
        except ValueError as e:
            print(e)
    pass


def end_shift():
   
    print("Medic", name, "ended their shift.")
    display_status
    print(f"They have {medical_supplies} supplies remaining, {energy} remaining, and treated {ewoks_treated} Ewoks.")
    print("Goodbye!")
    input("Press Enter to exit...")
    pass


# Start the shift
start_shift()
