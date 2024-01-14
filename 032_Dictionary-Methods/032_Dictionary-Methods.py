AnExampleDictionary = {
    "Item1":"Value1",
    "Item2":"Value2",
    "Item3":"Value3",
    "Item4":"Value4",
    "Item5":"Value5",
}

AnExampleDictionary.update({"Item5":"Value FIVE"}) #The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair. (can also append a second dictionary)

# AnExampleDictionary.clear() #Clears all items.
# print(AnExampleDictionary)

AnExampleDictionary.pop("Item1") #The pop() method removes the key-value pair whose key is passed as a parameter.

AnExampleDictionary.popitem() #The popitem() method removes the last key-value pair from the dictionary.

del AnExampleDictionary["Item4"] #Deletes the the item 4 in the dictionary...
del AnExampleDictionary #Deletes the whole dictionary...


