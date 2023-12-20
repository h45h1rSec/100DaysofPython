

# Conditional Operators
# >, <, ==, <=, >=, !=

# a = 10
# b = 50

# print(a>b) #Checks if a is greater than b.
# print(a<b) #Checks if a is lesser than b.
# print(a==b) #Checks if a is equal to b.
# print(a<=b) #Checks if a is lesser than or equal to b.
# print(a>=b) #Checks if a is greater than or equal to b.
# print(a!=b) #Checks if a is not equal to b.
# #Returns a boolean value.

# Conditional Statements, takes value in boolean datatype
# if else elif

print("\nIf-else demo program")

Input = int(input("Enter your age: "))
if(Input > 18):
    print("You can eat pizza!")
else:
    print("You can't eat pizza!")

print("Out of the conditional statements...")

# SYNTAX:
# if(condition):
#     with indentation, if conditions here!
# else:
#     with indentation, else conditions here!

# To define a code block in python, we use indentation, unlike other languages which use braces {}.

print("\nIf-elif-else demo program, or if-else ladder")

Input = int(input("Enter your age: "))
if(Input > 18):
    print("You can eat pizza!")
elif(Input == 18):
    print("You just became eligible to eat pizza!")
else:
    print("You can't eat pizza!")

print("Out of the conditional statements...")

# SYNTAX:
# if(condition):
#     with indentation, if conditions here!
# elif(condition):
#     with indentation, elif conditions here!
# else:
#     with indentation, else conditions here!



print("\nIf-elif-else demo program, or nested if-else")

Input = int(input("Enter your age: "))
if(Input > 18):
    print("You can eat pizza!")
elif(Input == 18):
    print("You just became eligible to eat pizza!")
elif(Input <= 0):
    print("You are not born yet, are you a robot?")
else:
    print("You can't eat pizza!")

print("Out of the conditional statements...")

# SYNTAX:
# if(condition):
#     with indentation, if conditions here!
# elif(condition):
#     with indentation, elif conditions here!
# elif(condition):
#     with indentation, elif conditions here!
# elif(condition):
#     with indentation, elif conditions here!
# else:
#     with indentation, else conditions here!

