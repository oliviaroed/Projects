print("Welcome New Adventure to TBD! ")

name = input("What is your name, new adventure? ")
print(f"Hello, {name}! Your journey will now comense...\n")

choice = input ("You see four doors displayed in front of you. Do you go Left or Right? ").lower()

if choice == "left":
    while True:
        door_choice = input("There are two more doors to be opened, door1 or door2?")
        if door_choice == "door1":
            print("Door is locked!")
        elif door_choice == "door2":
            print("You found a key and entered the next room!")
            break
        else:
            print("Invalid input. Please choose 'door1' or 'door2.")

