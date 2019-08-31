#function for adding
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
#function for subracting
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
#functino for multiplying
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
#function for dividying
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

#print the start
print("\nLet's do some math with just functions!")
# do some math operations with the functinons
age = add(30, 5)
# debugging statement to see that adding function works
print(">>>> age=", age)
height = subtract(78, 4)
print(">>>> height=", height)
weight = multiply(90, 2)
print(">>>> weight=", weight)
iq = divide(100, 2)
print(">>>> iq=", iq)
#print results
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age,
            subtract(height,
                multiply(weight,
                    divide(iq, 2)
                )
            )
        )

print("That becomes: ", what, "Can you do it by hand?\n")
# translating the puzzle to the math operatinos
what2= 35+74-180*50/2
#print the result to see if it matches
print(what2)
