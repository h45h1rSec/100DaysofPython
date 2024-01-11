# Printing the Union of two sets.
Set1 = {"Karachi", "Lahore","Gwadar","Peshawar"}
Set2 = {"Hyderabad", "Peshawar","Gwadar","Multan"}

print(Set1.union(Set2)) #Union set will be printed

# Original set value is not changed.
print(Set1,Set2)

#To change 'Set1' to union of 'Set1' and 'Set2', we use ".update".
Set1.update(Set2)
print(Set1)

# FOR INTERSECTION OF SETS 
Set3 = {"Cat", "Sparrow","Rat","Fish"}
Set4 = {"Bear", "Fish","Cat","Dove"}

print(Set3.intersection(Set4)) #intersection set will be printed
# Original set value is not changed.
print(Set3,Set4)

#To change 'Set3' to intersection of 'Set3' and 'Set4', we use ".intersection_update".
Set3.intersection_update(Set4)
print(Set3)

#SYMMETRIC DIFFERENCE (All the value which are not common in sets)

Set5 = {1,2,3,4,5,7,20}
Set6 = {4,5,6,7,8,9}

print(Set5.symmetric_difference(Set6))
# .symmetric_difference_update also works to update the value into the set.

# DIFFERENCE (All unique value which are present in the original set)
Set7 = {1,2,3,4,5,7,20}
Set8 = {4,5,6,7,8,9}

print(Set7.difference(Set8))
# .difference_update also works to update the value into the set.


#########################
DummySet = {4,5,6,35,8}

# SEVERAL OTHER SET METHODS 

# .isdisjoint(), checks if items of given set are present in the other set (Returns Boolean)

# .issuperset(), checks all items of a specific set are present in the original set. (Returns Boolean)

# .issubset() checks if all the items of the original set are present in the particular set. (Returns Boolean)

# .add(), adds an item to a set.(one item only)
DummySet.add(400)
# print(DummySet)

# .update(), adds one or multiple items to the set.
DummySet.update("L","M")
# print(DummySet)

# .remove(), removes an item to a set.(one item only)
DummySet.remove(400)
# DummySet.remove(400) # Rasie an exception if item not found!
# print(DummySet)

# .discard(), removes an item to a set.(one item only)
DummySet.discard(400)
DummySet.discard(400) # Will not rasie an exception if item not found!
# print(DummySet)

# .pop(), removes the last element of the set, but we don't know the order of the set, as sets are unordered
print(DummySet.pop()) # We can print the popped value or store it into a variable.


# .clear(), clears all entries and returns empty set.
DummySet.clear()
print(DummySet)

# del keyword deletes the entire element
del DummySet
# print(DummySet) # Error


# USE THE 'in' KEYWORD TO CHECK THE ITEM EXISTS OR NOT 
CheckSet = {"one","two","three"}

if "one" in CheckSet:
    print("OK")

# print(CheckSet[0]) #Error, sets cannot be indexed