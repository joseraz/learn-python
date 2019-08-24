name = 'Jose Raz'
age = 35
height_inches = 74 # inches
height_standard = height_inches * 2.54
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_inches} inches tall.")
print(f"He's {round(height_standard)} cm tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"He's teeth are usually {teeth} depending on the coffee.")

# this line is tricky try to get it exactly right
total = age + height_inches + weight
print(f"If I add {age}, {height_inches}, and {weight} I get {total}.")
