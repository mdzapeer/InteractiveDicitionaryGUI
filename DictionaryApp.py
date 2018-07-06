import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))

class dictionary:
    #intialize class
    def __init__(self):        
        global userin        
        userin=input ("\nEnter a word: \n")
    #fucntion to check the captialization
    def inputcasecheck(self,userin):
    #Alternative way
    #    if userin[0].isupper():
    #        return(extractj(userin))
        if userin.title() in data:
            return ( self.extractj(userin.title()))
        elif userin.upper() in data:
            return ( self.extractj(userin.upper()))
        else:
            return ( self.extractj(userin.lower()))
    #fucntion to check partial mathes and loop to ask correct word
    def partmatch (self,word):       
        self.word=str(word[0])
        userin=input ("Did you want to see the meaning for '%s' \nYes or No?\n" %word)
        userin=userin.lower()
        if  userin == "yes" or userin == "y":
            return (data[self.word])
        elif userin == "no" or userin == "n":
            userin2=input ("Enter the word: \n")
            return self.inputcasecheck(userin2)
        else:
            while userin != "yes" or userin != "y" or userin != "no" or userin != "n":
                userin=input ("Please enter 'yes' or 'no': ")
                if userin == "no" or userin == "n":
                    userin3=input ("Enter the word: \n")
                    return  self.inputcasecheck(userin3)
                if userin == "yes" or userin == "y":
                    return (data[self.word])
    #function to get partial or full match
    def extractj (self,userin):
        out=difflib.get_close_matches(userin, data.keys(), 1)
        if userin in data:
            return (data[userin])
        elif len(out)>0:
            out2=difflib.get_close_matches(userin, data.keys())
            print ("Closest matches to %s: \n" %userin + str(out2))
            return  self.partmatch(out)
        else:
            return ("Word not in dictionary\n")

#intialize object of dictionary class
dictionaryObj=dictionary()
output1=dictionaryObj.inputcasecheck(userin)

if type(output1) == list:
    for item in output1:
        print("%s." %str(output1.index(item)+1) +item+ "\n")
else:
    print(output1)
