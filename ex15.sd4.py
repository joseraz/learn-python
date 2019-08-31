# open sys package and import the module argument variables
from sys import argv
# script and filename are variable assigned to the module
script, filename = argv
# var txt opens the filename given and holds the text
txt = open(filename)
# print the name of the file given in the argument
print(f" Here's your file {filename}:")
# here the command .read is used of the var txt and printed.
print(txt.read())
# asking for the file name again
