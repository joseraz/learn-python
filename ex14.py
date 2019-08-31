# importing the argument variables
from sys import argv
# arguments for the script
script, user_name, test = argv
# this prompt is given to ask questions
prompt = f'  ({user_name})-> '
# print the first two arguments
print(f" Hi {user_name}, I'm the {script} script.")
print(" I´d like to ask you a few questions.")
# first input
print(f" Do you like me {user_name}?")
likes = input(prompt)
# second input
print(f" Where do you live {user_name}?")
lives = input(prompt)
# third input
print(" What kind of computer do you have?")
computer = input(prompt)
# print all the inputs into phrases.
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
I heard a rumor you like {test}. For real?
""")
