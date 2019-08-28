import random
from urllib.request import urlopen
import sys

WORLD_UR = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
        "class %%%(%%%):":
            "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)" :
            "Class %%% has-a __init__ that takes self and *** params.",
            }
# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines()
    WORDS.append(str(word.strip(), enconding="utf-8"))


def convert(snippet, phrase):
    class_name = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
other_names = random.sample(WORDS, snippet.count("%%%"))
results = []
param_names = []
