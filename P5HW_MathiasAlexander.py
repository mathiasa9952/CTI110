# Alex Mathias
# 4/8/25   
# P5HW
# Creating a Game

import random

def createDonald():
    # Create variables for the dictionary
    name = "Miso the cat"
    health_points = 100 
    sneak_ability = 0
    inventory = []

    add_item =  input(f"Should {name} have any items to begin? (y/n): ")
    # Loop to keep getting items from the user
    while add_item.lower() != "n":
        obj = input("Enter an item to add to inventory: ")
        # Add the object to list
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

def move_right(character):
    print("You have encountered a big hawk")
    print("🦅")
    print("It damaged your paw's.....")
    # Decrement the sneak_ability attribute by a random value from 2-10
    damage = random.randint(2,11)
    print()
    print(f"{character["name"]}, took paw damage of {damage}")
    print()
    character["sneak_ability"] -= damage
    print(f"{character["name"]}'s new sneak ability is {character["sneak_ability"]}")

def main():
    print()
    print("Welcome to Miso's silly adventure!🐱🐈")
    print()
    # Call the function to create the character
    character = createDonald()
    # Test
    print(character)

    direction = input("Take the path to the right or to the left: ")
    print(".....")
    if direction == "left":
        # Call a function
        print("To be continued....")
    if direction == "right":
        move_right(character)
    print(character)


# Call the main
if __name__ == "__main__":
    main()