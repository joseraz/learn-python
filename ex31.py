print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There is a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bears eats your face off. You are dead.")
    elif bear == "2":
        print("The bear eats your legs off. You run away.")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Undestanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
elif door == "4":
    print("Aha! I see you are a man of knowledge.")
    print("You pass through the hidden door.")
    print("Inside a giant triangle with an eye stares into infinty.")
    print("Open your eyes and see the truth!")
    print("You have gained the power of articulation!")
else:
    print("You stumble around and fall on a knife and die. Dipshit.")
