# List and tuples in python are kind of similar things, but tuples are immutable (unchangeable) and lists are mutable (changeable)

# SYNTAX:
# TupleName = (value1, value2 ...)

MyTuple = (4,4,8,2013, True, "Other datatypes are supported")

print(MyTuple)
print(type(MyTuple))

MyTuple = (1) #this is an int, not a tuple
print(type(MyTuple))

MyTuple = (1,) #For making it a tuple insert a comma after the value.
print(type(MyTuple))

MyTuple = ("Hello") #It is a string, add a comma for tuple
print(type(MyTuple)) 

# TUPLES ARE NOT CHANGEABLE, BY METHODS OR BY ELEMENTS
TheTuple = (45,22,320,7)
print(TheTuple)
# TheTuple[0] = "Can't change!" #Gives error!, this can be done in lists

# Tuple indexing is same as lists...
print(TheTuple[3])

# Check item in tuple 
if 5 in TheTuple:
    print("Yes, present!")
else:
    print("Not present!")

# Slicing
print(TheTuple[1:3]) #The original tuple is not changed, it just returns the range!
print(TheTuple)

# ALL SLICING METHODS WORK IN TUPLES AS LISTS 


# ONLY DIFFERENCE BETWEEN LISTS AND TUPLES IS, TUPLE VALUES CANNOT CHANGE