from inventorysystem import inventory, show_inventory, remove_item


def three_item_door():
    print("\nYou approach a massive stone door with three empty slots.")
    print("It looks like it needs three specific items to open.")
    print("Commands: 'use items', 'inventory', 'back'")

    choice = input("> ").strip().lower()

    if choice == "inventory":
        show_inventory()
        return "three_item_door"

    if choice == "use items":
        required = {"Mark of Secrets", "Mark of Madness", "Mark of Whispers"}

        if required.issubset(inventory):
            print("You place the Marks of Secrets, Madness and Whispers to the slots.")
            print("The door rumbles and slowly opens.")
            
            for item in required:
                inventory.remove(item)

            return "inner_chamber"   
        else:
            missing = required - inventory
            print("You are missing:", ", ".join(missing))
            return "three_item_door"

    if choice == "back":
        return "hallway"

    print("Invalid command.")
    return "three_item_door"
