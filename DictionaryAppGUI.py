import json
import difflib
from difflib import get_close_matches
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

data=json.load(open("data.json"))

#create dictionary class for looking up the word
class dictionary:
    #function to check the captialization
    def inputcasecheck(self,userin1):
        if userin1.title() in data:
            return (self.extractj(userin1.title()))
        elif userin1.upper() in data:
            return (self.extractj(userin1.upper()))
        else:
            return (self.extractj(userin1.lower()))
    #fucntion to check partial mathes and loop to ask correct word
    def partmatch (self,word):       
        self.word=str(word[0])
        windowUI.output("Did you want to see the meaning for '%s'" %self.word)
        userres=messagebox.askyesno(title="Confirm word", message="Did you want to see the meaning for '%s'" %word)
        if userres == True:
            return (data[self.word])
        elif userres == False:
            messagebox.showinfo(title="Confirm word", message="Enter the word")
        else:
            while userres != True or userres != False:
                windowUI.output("Enter the word")      
        # userin=input ("Did you want to see the meaning for '%s' \nYes or No?\n" %word
        # userin=windowUI.submit()
        # userin=userin.lower()
        # if userin == "yes" or userin == "y":
        #     return (data[self.word])
        # elif userin == "no" or userin == "n":
        #     windowUI.output("Enter the word")
        #     userin2=windowUI.submit()
        #     return self.inputcasecheck(userin2)
        # else:
        #     while userin != "yes" or userin != "y" or userin != "no" or userin != "n":
        #         windowUI.output("Please enter 'yes' or 'no': ")
        #         userin=windowUI.submit()
        #         # userin=input ("Please enter 'yes' or 'no': ")
        #         if userin == "no" or userin == "n":
        #             windowUI.output("Enter the word")
        #             userin3=windowUI.submit()
        #             return self.inputcasecheck(userin3)
        #         if userin == "yes" or userin == "y":
        #             return (data[self.word])
    #function to get partial or full match
    def extractj (self,userin):
        out=difflib.get_close_matches(userin, data.keys(), 1)
        if userin in data:
            return (data[userin])
        elif len(out)>0:
            out2=difflib.get_close_matches(userin, data.keys())
            windowUI.output("Closest matches to %s: \n" %userin + str(out2))
            windowUI.entry.delete(0,END)
            return self.partmatch(out)
        else:
            return windowUI.output("Word not in dictionary\n")

#class for the UI window front end
class windowUI(object):

    def __init__(self,window):
        self.window=window
        self.label=ttk.Label(window,text="Enter a word")
        self.label.pack()
        self.userin=StringVar()
        self.entry = ttk.Entry(window,textvariable=self.userin, width=30)
        self.entry.pack()
        submit = ttk.Button(window, text='submit', command=self.submit)
        submit.pack()
        self.list1=Listbox(window,height=10,width=100)
        self.list1.pack()
   
    def submit(self):
        self.list1.delete(0,END)
        self.checkDict(self.entry.get())
        
    def checkDict(self,userin):
        self.output(dictionaryObj.inputcasecheck(userin))
           
    def output(self,output):
        if type(output) == list:
            for item in output:
                self.list1.insert(END,"%s." %str(output.index(item)+1) +item+ "\n")
        else:
            self.list1.insert(END,output)

#intialize object of dictionary class
dictionaryObj=dictionary()
#main tk GUI loop
window=Tk()
windowUI=windowUI(window)
window.mainloop()    