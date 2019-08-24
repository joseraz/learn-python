# first line to be printed
print("Mary had a little lamb.")
# this prints a bracket that is formated in the same parenthesis after the string
print("Its fleece was white as {}." .format('snow'))
# third line to be printed for the rhyme
print("And everywhere that Mary went.")
# this prints a dot ten times
print("." * 10) # what'd that do?
# setup twelve variables, one for each letter of cheeseburger
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. Try removing it to see what happens.
# this prints the chees part of the word and joins the second half
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# prints the second part, burger.
print(end7 + end8 + end9 + end10 + end11 + end12)
