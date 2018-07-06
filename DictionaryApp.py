import json
import difflib
from difflib import get_close_matches

def extractj (userin):
    data=json.load(open("data.json"))
    out=difflib.get_close_matches(userin, data.keys(), 1)
    if userin in data:
        return (data[userin])
    elif len(out)>0:
        out2=difflib.get_close_matches(userin, data.keys())
        return "Closest matches: \n" + str(out2)
    else:
        return ("Word not in dictionary")

userin=input ("\nEnter a word: \n")
print (extractj(userin.lower()))
