# open the sys package and import the argument variable module
from sys import argv
# take the script name and filename as argument for the argv module
script, filename = argv
# tell user what file they are opening
print(f"We're going to erase {filename}.")
# tell user whatis going to happen, give them a way out
print("If you don't want that, hit CTRL-C (^C).")
# use RETURN to proceed
print("If you do want that, hit RETURN.")
# ask what they want
input("?")
# tell user we are opening file
print("Opening the file...")
# target variable is assigned by opening up filename
# the w is to say open the file in 'write' mode
target = open(filename, 'a')
# print the truncating action
print("Truncating the file. Goodbye!")
# takes the variable target and truncate the whole file
target.truncate()
# now we ask for three lines
print("Now I'm going to ask you for three lines.")
# asks for three lines
line1 = input(" line 1: ")
line2 = input(" line 2: ")
line3 = input(" line 3: ")
# print that the lines are being written
print("I'm going to write these to the file.")
# take variable target and write the three lines taken previously
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#print that we are closing the file
print("And finally, we close it.")
# close the file
target.close()
