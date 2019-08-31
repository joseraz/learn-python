# define the variable ten_things to a phrase
ten_things = "Apples Oranges Crows Telephone Light Sugar"
# print out some text
print("Wait there are not 10 things in that list. Let's fix that.")
# assigna new variable "stuff" where you split the list from the top
stuff = ten_things.split(' ')
# make an array with eight more words in it
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]
# this is a loop to add more itmes to the variable "stuff" while stuff is not ten
while len(stuff) != 10:
    # the pop() method removes the item at the given index from the list. The method also returns the removed item.
    next_one = more_stuff.pop()
    # print the item removed
    print("Adding: ", next_one)
    # take the removed item and append it to "stuff"
    stuff.append(next_one)
    #print how many items there now in the list
    print(f"There are {len(stuff)} items now.")
# print all the items in "stuff"
print("There we go: ", stuff)
# print a string
print("Let's do some things with stuff.")
# since it starts at zero, this one print the second item
print(stuff[1])
# prints the last item
print(stuff[-1]) #whoa! fancy
# print the last item in the list, similar to the last one but you popped it
print(stuff.pop())
print(">>>>>>>TEST")
# If I reprint stuff, it no longer has "Corn at the end of the list"
print(stuff)
print(' '.join(stuff)) #what? cool!
# This one joins the fourth and fifth item with a hashtag in the middle
# I changed it to add more items
print('#'.join(stuff[3:6])) # super stellar!
