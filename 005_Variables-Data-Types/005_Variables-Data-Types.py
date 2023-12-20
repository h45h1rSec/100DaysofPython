# Variables are like containers, in which we can store data, and these variables are stored in RAM of your computer.

# Syntax: Variable_Name = value

Variable = 20
Variable = 20*50 #overwritten
print(Variable)

Other_Variable = "Something"
Variable = Other_Variable
print(Variable)


# Data Type
Number = 85
String = "85"
Boolean = True #"True" not "true"! 
Null = None

#To see the variable data type, use type(value) function.
print("\nData types:")
print(type(Number))
print(type(String))
print(type(Boolean))
print(type(None))
print("\n")

# Python also contains some built-in datatypes like:

# Number -> int, float, complex
Number_F = 1.5
Number_C = complex(8,2)

# Sequenced data -> list, tuple
List = [8, 20.3, [-4,5], "Apple"]
Tuple = ("Parrot", 54, (52, "This is a tuple!"), List)

# Mapped data -> Dict
Dict = {"Name":"My Name","Age":20, "Eligible":Boolean}

print("Other data types:")
print(type(Number_F))
print(type(Number_C))
print(type(List))
print(type(Tuple))
print(type(Dict))

# EVERYTHING IN PYTHON IS AN OBJECT!!! "Just to remember till, Classes and Objects topic."