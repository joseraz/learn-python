# Page 150
# this set up the variable i
i = 0
# numbers list with empty brackets
numbers = []
# while loops to repeat
while i < 6:
    # the number that starts the loop
    print(f"At the top i is {i}")
    # adding the number to the list
    numbers.append(i)
    # increasing i by one
    i += 1
    # printing the numbers on the list
    print("Numbers now: ", numbers)
    # priting the number that finishes the list
    print(f"At the bottom i is {i}\n")

print(" The numbers: ")
# for loop to print out all the numbers in the list
for num in numbers:
    print(num)
