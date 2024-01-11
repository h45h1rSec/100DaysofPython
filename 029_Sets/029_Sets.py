# Sets is a collection of well-defined objects in python. (in short, no repeated values in a set)

# set items are enclosed in curly brackets and separated by commas
Set = {10,20,75,10,98,10,1,10} #All duplicate values will be skimmed. And values are written in no order.
print(Set)

# All methods of list also applied to be sets 
# Sets are unchangeable at index level. (Sets have no orders, random values at randon indexes)

Set2 = {"Hello Python!",45,False,3.14} #Sets can contain multiple data types
print(Set2)

# Quick Quiz: Try to create an empty set and check its type 

# QuizSet = {} #It returns a dict class.
QuizSet = set()
print(type(QuizSet))  


# Print via loop
for SetValue in Set2:
    print(SetValue)


# SETS DO NOT MAINTAIN ORDER