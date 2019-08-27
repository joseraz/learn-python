import random
from urllib.request import urlopen
import sys

WORLD_UR = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
        "class %%%(%%%):":
            "Make a class named %%% that is-a %%%.",
            }
# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False
