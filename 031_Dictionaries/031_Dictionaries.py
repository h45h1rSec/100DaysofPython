Dictionary = {
    "Any Key":"Any Value"
}

# A simple method for storing combinations of key:value pairs
# Dictionaries are ordered collection of data items. They store multiple items in a single variable.
# Dictionaries items are key-value pairs that are separated by commas and enclosed within brackets '{}'.
# Before Python 3.7, Dictionaries were unordered

EmployeeID = {
    1020:"A",
    1021:"B",
    1022:"C"
}

print(EmployeeID) #Prints whole dictionary
print(EmployeeID[1020]) #Prints only the required key's value

#Two ways to access a key!
print(EmployeeID[1022]) # Returns error, IF key is not found.
print(EmployeeID.get(10022)) #Do not returns error, if key is not found.
print(EmployeeID.keys()) #Returns all the keys of the dictionary.
print(EmployeeID.values()) #Returns all the values of the dictionary.
print(EmployeeID.items()) #Returns all the keys and value in pairs of the dictionary.


#############################
# FOR LOOP TO ACCESS ALL KEYS OR VALUES
for Key in EmployeeID.keys():
    print(f"The value for key {Key} is {EmployeeID[Key]}")


###################################
# FOR LOOP TO ACCESS KEY AND VALUES AT THE SAME TIME
for Key, Value in EmployeeID.items():
    print(f"The value for key {Key} is {Value}")
