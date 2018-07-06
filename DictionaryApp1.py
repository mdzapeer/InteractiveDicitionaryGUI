import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))

def extractj (userin):
    out=difflib.get_close_matches(userin, data.keys(), 1)
    if userin in data:
        return (data[userin])
    elif len(out)>0:
        out2=difflib.get_close_matches(userin, data.keys())
        print ("Closest matches to %s: \n" %userin + str(out2))
        partmatch(out)
        return ""

    else:
        return ("Word not in dictionary\n")

def partmatch (word):
    word=str(word[0])
    userin=input ("Did you want to see the meaning for '%s' \nYes or No?\n" %word)
    userin=userin.lower()
    if userin == "yes" or userin == "y":
        print(data[word])
    elif userin == "no" or userin == "n":
        userin2=input ("Enter the word: \n")
        extractj(userin2.lower())
    else:
        while userin != "yes" or userin != "y" or userin != "no" or userin != "n":
            userin=input ("Please enter 'yes' or 'no'")
            if userin == "yes" or userin == "y":
                print (word)
                break
            if userin == "no" or userin == "n":
                userin2=input ("Enter the word: \n")
                extractj(userin2.lower())
                break
    return ""

userin=input ("\nEnter a word: \n")
print (extractj(userin.lower()))
