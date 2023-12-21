ExampleList = [] #Created an empty list
print(ExampleList) #prints empty list

ExampleList = ["Item0", "Item1", "Item2","Item3","Item4","Item2"]
ExampleList2 = ["Some","New","Elements","Here!"]

ExampleList.append("Item5")
print(ExampleList) #prints list with appended item

ExampleList.reverse() #Reverses the order
print(ExampleList)

print(ExampleList.index("Item2")) # returns the index of the first occurance of the item in list.

print(ExampleList.count("Item2")) #Counts the specified element in the list

# TestList = ExampleList # TestList is a reference to ExampleList
# TestList[5] = 0 #5th index = 0
# print(ExampleList) #5th index is set to zero
# #DONT USE IT AS A BEGINNER, USE .COPY() instead

TestList = ExampleList.copy()
TestList[0] = 4
print(ExampleList) # not changed
print(TestList) # only this is changed

#Inserting a value at a specific index -> insert(index,value)
ExampleList.insert(0,"I am NEW!")
print(ExampleList)

ExampleList.pop(0) #Removes the element in 0th index
print(ExampleList)

ExampleList.extend(["Some","New","Elements","Here!"]) #Extends the given list with another list
print(ExampleList) #Changes the original list

#Concatinate lists
Merged = ExampleList + ExampleList2 + [45, 3, 77, 476]
print(Merged) #Original list not changed


NumExampleList = [44,64,8,89,475,1,0,35,5,7,90,0.31]

NumExampleList.sort() #Sorts in accending order (Only works with integers and float)
print(NumExampleList)

NumExampleList.sort(reverse=True) #Sorts in deccending order (Only works with integers and float)
print(NumExampleList)


# UNLIKE STRINGS, LISTS ARE CHANGED ON METHODS

