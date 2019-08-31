i = 0
numbers = []

this_point = int(input(" How many times do you want to repeat?"))

# while loops to repeat
for i in range(0, this_point):
    print(f"At the top i is {i}")
    numbers.append(i)
    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}\n")

print(numbers)
