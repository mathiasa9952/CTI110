# Alex Mathias
# 4/8/25   
# P5HW
# Creating a Game

import random

def createMiso():
    # Create variables for the dictionary
    name = "Miso the cat"
    health_points = 100 
    sneak_ability = 10  # starting sneak ability
    inventory = []

    add_item =  input(f"Should {name} have any items to begin with? (y/n): ")
    # Loop to keep getting items from the user
    while add_item.lower() != "n":
        obj = input("Enter an item to add to inventory (bandage, medkit, or sneak potion): ")
        # Add the object to the list
        inventory.append(obj)
        print()
        add_item =  input(f"Add another item? (y/n): ")
    # Loop breaks here
    print()
    print(f"You successfully created {name}'s inventory:")
    print()
    print(inventory)
    # Create the dictionary that represents the character
    character = {"name" : name, "inventory": inventory, "health_points" : health_points, "sneak_ability" : sneak_ability}
    return character 

def random_event(character):
    # Random events list with different outcomes
    events = [
        "You found a bandage!",
        "You found a medkit!",
        "A wild monster attacks you! You lose health.",
        "You find a quiet area to rest and regain health!",
        "You encountered a rival cat! You lose some health.",
        "You have encountered a huge snake! 🐍 ",
        "You found a rabid raccoon! 🦝",
        "You stepped on a beehive! 🐝 Run!"
    ]

    event = random.choice(events)
    print(event)
    if event == "You found a bandage!":
        character["inventory"].append("bandage")
    elif event == "You found a medkit!":
        character["inventory"].append("medkit")
    elif event == "A wild monster attacks you! You lose health.":
        damage = random.randint(20, 40)
        character["health_points"] -= damage
        print(f"{character['name']} lost {damage} health. Health is now {character['health_points']}.")
    elif event == "You find a quiet area to rest and regain health!":
        heal = random.randint(5, 15)
        character["health_points"] += heal
        print(f"{character['name']} rested and regained {heal} health. Health is now {character['health_points']}.")
    elif event == "You encountered a rival cat! You lose some health.":
        damage = random.randint(20, 40)
        character["health_points"] -= damage
        print(f"{character['name']} lost {damage} health in the encounter. Health is now {character['health_points']}.")
    elif event == "You have encountered a huge snake! 🐍 ":
        damage = random.randint(20, 40)
        character["health_points"] -= damage
        print(f"{character['name']} lost {damage} health in the encounter. Health is now {character['health_points']}.")
    elif event == "You found a rabid raccoon! 🦝":
        damage = random.randint(30, 50)
        character["health_points"] -= damage
        print(f"{character['name']} lost {damage} health in the encounter. Health is now {character['health_points']}.")
    elif event == "You stepped on a beehive! 🐝 Run!":
        damage = random.randint(10, 20)
        character["health_points"] -= damage
        print(f"{character['name']} lost {damage} health in the encounter. Health is now {character['health_points']}.")

def move(character):
    # Random event for movement
    print("You start moving...")
    random_event(character)

def use_item(character):
    print("Your inventory includes: ", character["inventory"])
    item = input("Do you want to use any item? (type 'bandage', 'medkit', or 'sneak potion' or 'no' to skip): ")
    if item in character["inventory"]:
        if item == "bandage":
            character["health_points"] += 10
            character["inventory"].remove(item)
            print(f"{character['name']} used a {item}. Health is now {character['health_points']}.")
        elif item == "medkit":
            character["health_points"] += 20
            character["inventory"].remove(item)
            print(f"{character['name']} used a {item}. Health is now {character['health_points']}.")
        elif item == "sneak potion":
            character["sneak_ability"] += 5
            character["inventory"].remove(item)
            print(f"{character['name']} used a {item}. Sneak ability is now {character['sneak_ability']}.")
        
    else:
        print(f"{item} is not in your inventory!")

def main():
    print()
    print("Welcome to Miso's silly adventure!🐱🐈")
    print()
    # Call the function to create the character
    character = createMiso()
    # Test: Print out character details
    print(character)

    while character["health_points"] > 0:
        print("\nYour current stats:")
        print(f"Health: {character['health_points']} | Sneak Ability: {character['sneak_ability']}")
        print(f"Inventory: {character['inventory']}")
        
        # Ask the player to choose direction
        direction = input("Take the path to the right or to the left (type 'right' or 'left'): ")
        print(".....")
        
        move(character)  # Random event happens no matter what direction is chosen
        
        # Ask the player if they want to use an item after every turn
        use_item_choice = input("Do you want to use an item from your inventory? (y/n): ")
        if use_item_choice.lower() == "y":
            use_item(character)

        # Check if the player is alive
        if character["health_points"] <= 0:
            print(f"\n{character['name']} has run out of health! Game Over.")
            break

        # Option to exit the game
        exit_game = input("Press Enter to continue or type 'exit' to quit the game: ")
        if exit_game.lower() == "exit":
            print("Exiting game.")
            break

# Call the main
if __name__ == "__main__":
    main()