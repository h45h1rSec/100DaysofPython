# Match case is a new edition which is added in python v3.10 and onwards.

import os
# https://docs.python.org/3/library/os.html

# os.system runs commands from the computers CLI, i.e. CMD 
print("Hey, I am using", end=' ')
os.system("python --version")

print("\nMatch case statements are similar to switch-case statements in C, C++ or JAVA!\n")

# A match statement will compare a given varible's value to different shapes, also called pattern. The central idea is to keep on comparing the variable's value with all the present patterns until it fits into one, if not default value is executed.

X = int(input("Enter unknown value: "))

match X:

    case 0:
        print("Block 0 is executed!")
    case 1:
        print("Block 1 is executed!")
    case 2:
        print("Block 2 is executed!")
    case 3:
        print("Block 3 is executed!")
    case _:
        print("Default is executed, when none of the values match.")

# Default is defined as '_' and is optional, but a good practice.
# In python there is no need for the 'break' statement, unlike other programming languages.


# We can blend the if statements with the default case.

Y = int(input("\nEnter the second unknown value: "))

match Y:

    case 0:
        print("Block 0 is executed!")
    case 1:
        print("Block 1 is executed!")
    case 2:
        print("Block 2 is executed!")
    case 3:
        print("Block 3 is executed!")

    case _ if(Y==X):
        print("Yes, X = Y")
    case _ if(Y<0):
        print("Negative...")
    case _:
        # if none of the if statements match, default will run.
        print("Default is executed, when none of the values match.")