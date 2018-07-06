userin=input ("Did you want to see the meaning for word \n Yes or No?\n")

while userin != "yes" or userin != "y" or userin != "no" or userin != "n":
    userin=input ("Please enter 'yes' or 'no'")
    if userin == "no" or userin == "n":
            print ("whatever")
            break
    if userin == "yes" or userin == "y":
            print ("hoo boy")
            break
