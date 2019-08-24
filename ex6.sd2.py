types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# Here: (string inside a string)
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
#Here
print(f"I said: {x}")
#Here
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#Here: used teh special .format to place hilarious as a string inside joke_evaluation string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = " a string with a right side."
#This adds both the previous string as if they an array.
print(w + e)
