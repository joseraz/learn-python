# adds features to the script from the Python feature set
# "features" are more commonly known as "modules"
from sys import argv
# read the WYSS section for how to run this
# this line takes what is in argv, unpacks the argv, then assigns it four different variables
script, first, second, third = argv
# print the variables
print(" The script is called: ", script)
print(" The first variable is: ", first)
print(" The second variable is: ", second)
print(" The third variable is: ", third)

x = input(" Give me a number: ")

print("\t", x*2)
print(" There now you have more. ")
