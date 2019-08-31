# Pag 161
from sys import exit
# start in the character's room
def sleep(zzz):
    print(zzz, "You fall asleep.")
    exit(0)

def start():
    print("\nYou wake up in your room, rested.")
    print("The dinosaur is still there.")
    print("What do you do?")
    print("1. Look around.")
    print("2. Get up.")
    print("3. Back to sleep")
    choice = input("> ")
    if choice == "1":
        look_around("\nYou look around the room.")
    else:
        sleep(" The dino uses pheromones.")

def look_around(look):
    print(look)
    print("You notice the sun coming through the window.")
    print("There is a door to the main room on the left.")
    print("There is a door to the bathroom on the right.")
    print("The dinosaur is staring out the window.")

start()
