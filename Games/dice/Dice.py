"""
Step 1: Develop random number
Step 2: Check the number
Step 3: print the face
Step 4: looping
"""

import random
print("This is a dice simulator.")

x = "y"
   
while x == "y": 
    number = random.randint(1,6)

    if number == 1:
        print("---------")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print("---------")

    elif number == 2:
        print("---------")
        print("|       |")
        print("| o   o |")
        print("|       |")
        print("---------")

    elif number == 3:
        print("---------")
        print("|       |")
        print("| o o o |")
        print("|       |")
        print("---------")
    elif number == 4:
        print("---------")
        print("| o   o |")
        print("|       |")
        print("| o   o |")
        print("---------")

    elif number == 5:
        print("---------")
        print("| o   o |")
        print("|   o   |")
        print("| o   o |")
        print("---------")

    elif number == 6:
        print("---------")
        print("| o o o |")
        print("|       |")
        print("| o o o |")
        print("---------")
        
    x=input("press y to roll again and n to exit:") 
    print("\n") 