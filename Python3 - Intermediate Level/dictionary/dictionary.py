"""
A dictionary program for Pugger! 

Step 1: Interface
Step 2: develop the word matching
Step 3: modify the program
"""
import json
from difflib import get_close_matches 

def translateword(word):
    word = word.lower()
    if word in data:
        return data[word]
    
    elif word.title() in data:
        return data[word.title()]
    
    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("Press 'y' for yes or 'n' for no: ")

        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("Pugger your paw steps on wrong keys.")
        else:
            return("You have entered wrong input, please enter 'y' or 'n'.")
    else:
        print("Pugger your paw steps on wrong keys.")

data = json.load(open("data.json"))

i = "y" 
while i == "y":
    word = input("Enter the word Pugger want to search: ")
    output = translateword(word)

    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    i = input("Want to search more words? If yes, enter 'y' otherwise enter 'n' to exist the program: ")

    if(i == "y"):
        continue
    else:
        break

