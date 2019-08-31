# open the sys package and import the argument variable module
from sys import argv
# take to parameters to iniate the script
script, input_file = argv
# this function takes the input file and prints it out
def print_all(f):
    print(">>> print_all: f=", f)
    print(f.read())
    print("<<< print_all: f=", f)
# this function goes back to the beginning of the file
def rewind(f):
    f.seek(0)
# this function prints out the number line, and the line
def print_a_line(line_count, f):
    print(line_count, f.readline())
# assign variable to the open file
current_file = open(input_file)

print("First let's print a whole file:\n")
# call the print_all function
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# call the rewind function
rewind(current_file)

print("Let's print three lines:")
# assing a varlue to current_line and run print_a_line
current_line = 1
print_a_line(current_line, current_file)
# go up by one
current_line += 1
print_a_line(current_line, current_file)
# go up by one again
current_line += 1
print_a_line(current_line, current_file)
