text_adventure.py

print ("Welcome to Escape the Dungeon!")

name = input("What is your name, adventurer? ")
print(f"Hello, {name}! Your journey begins now...\n")

choice = input ("You see two doors. Do you go LEFT or RIGHT? ").lower()

if choice == "left":
    print("A dragon appears! You were roasted. Game Over. ")
elif choice == "right":
    print("You find a treasure chest full of gold! You win!")
else:
    print("You hestate too long... a trap is triggered! Game Over. ")

