inventory = set()

def add_item(item):
    inventory.add(item)
    print(f"You picked up {item}.")

def remove_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f"You used {item}.")
    else:
        print("You don't have that item.")

def has_item(item):
    return item in inventory

def show_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("You are carrying:")
        for item in inventory:
            print(f"- {item}")

print("You see a key on the floor.")
choice = input("Take it? (yes/no) ")

if choice.lower() == "yes":
    add_item("rusty key")
elif choice.lower() == "no":
    print("You leave the key to the floor")

print("You see a shovel on the ground.")
choice = input("Take it) (yes/no)")

if choice.lower() == "yes":
    add_item("shovel")
elif choice.lower() == "no":
    print("You leave the shovel on the ground")

print("You find a mythical Mark of Secrets from the chest.")
choice = input("Take it) (yes/no)")

if choice.lower() == "yes":
    add_item("Mark of Secrets")
elif choice.lower() == "no":
    print("You leave the Mark of Secrets to the chest")

print("From the fireplace peeks mythical Mark of Madness covered in ash.")
choice = input("Take it) (yes/no)")

if choice.lower() == "yes":
    add_item("Mark of Madness")
elif choice.lower() == "no":
    print("You leave the Mark of Madness in the fireplace")

print("From the confessional you find the Mark of Whispers.")
choice = input("Take it) (yes/no)")

if choice.lower() == "yes":
    add_item("Mark of Whispers")
elif choice.lower() == "no":
    print("You leave the Mark of Whispers")


command = input("> ")
if command == "inventory":
    show_inventory()




