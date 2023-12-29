ExampleTuple = ("Tuples", "Are", "Unchangable", "!")

#Converting tuple into a list
TempVar = list(ExampleTuple) #Will make the tuple's copy and convert into list ORIGINAL TUPLE IS NOT CHANGED

print(type(TempVar))
TempVar.append("And lists are mutable!")
TempVar.pop(0)
TempVar[0]= "Lists"
TempVar[2]= "Changeable"

print(TempVar)

# ExampleTuple = tuple(TempVar)
print(ExampleTuple)
print(type(ExampleTuple))

#Tuples can be concatinated

# TUPLE METHODS
print(len(ExampleTuple)) #Returns the length of the tuple.
print(ExampleTuple.count("Are")) #Counts the given element in the tuple.
print(ExampleTuple.index("Are")) #Returns the index of the first occurance of given element in the the tuple. (Will raise an exception if value not found)
print(ExampleTuple.index("Tuples", 0, 5)) # Finds the value in the specifed start-end range (Will raise an exception if value not found)
