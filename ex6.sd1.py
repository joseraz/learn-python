# variable for number of people
types_of_people = 10
# x takes the previous variable and turns it into a sentence.
x = f"There are {types_of_people} types of people."
# defining the variable binary as binary
binary = "binary"
# defining second variable do not for the punchline of the joke
do_not = "don't"
# putting both variables together into the joke.
y = f"Those who know {binary} and those who {do_not}."
# printing types of people
print(x)
# printing the binary joke
print(y)
# restating the first print with a format inside a print
print(f"I said: {x}")
# printing the joke with again the format inside a print and between quotations
print(f"I also said: '{y}'")
# defining variable hilarious as false
hilarious = False
# new variable for joke as a string, interesting that the string has {} inside but empty.
joke_evaluation = "Isn't that joke so funny?! {}"
# print the joke using .format, this allows me to input something into the {} of the string.
print(joke_evaluation.format(hilarious))
# def of var w as left side of a string
w = "This is the left side of..."
# def of var e as right side of a string
e = "a string with a right side."
# putting both previous strings together to make a single statement when printed.
print(w + e)
