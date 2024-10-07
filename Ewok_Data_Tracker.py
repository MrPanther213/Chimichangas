#Ewok Data Tracker- created by Zechariah
ewok_data = {
    "name" : "Wicket",
    "age" : 25,
    "weapon": "Spear",
    "rank" : "Warrior"
}
print("Ewok Name:", ewok_data["name"])
print("Ewok Age:", ewok_data["age"])
print("Ewok Weapon:", ewok_data["weapon"])
print("Ewok rank:", ewok_data["rank"])

ewok_data["weapon"] = "Bow and Arrow"  # Updating the weapon
ewok_data["rank"] = "Chief"  # Updating the rank
ewok_data["homeworld"] = "Endor"  # Adding a new attribute for homeworld

ewok_tribe = {
    "Wicket": ewok_data,
    "Chief Chirpa": {
        "name": "Chief Chirpa",
        "age": 30,
        "weapon": "Staff",
        "rank": "Chief",
        "homeworld": "Endor"
    }
}

print("\nEwok Tribe Data:")
for ewok_name, ewok_info in ewok_tribe.items():
    print(f"\nEwok: {ewok_name}")
    for key, value in ewok_info.items():
        print(f"{key}: {value}")
