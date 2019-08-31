# definition of the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# take the first argument and use it in a formated print
    print(f" You have {cheese_count} cheeses!")
# take the second argument and use it in a formated print
    print(f" You have {boxes_of_crackers} boxes of cracker!")
# print funny stuff
    print(" Man that's enough for a party!")
    print(" Get a blanket. \n")
# print for user
print(" We can just give the function numbers directly:")
# use function with numbers in arguments
cheese_and_crackers(20, 30)
# print alternative for users
print(" OR, we can use variables from our script:")
# use internal variables for function
amount_of_cheese = 10
amount_of_cracker = 50
cheese_and_crackers(amount_of_cheese, amount_of_cracker)
# print how to use math inside the arguments
print(" We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
# print that you can combine both variables and numbers in the brackets
print(" And we can combine the two, variables and math")
# example of combining both numbers and variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_cracker + 1000)
