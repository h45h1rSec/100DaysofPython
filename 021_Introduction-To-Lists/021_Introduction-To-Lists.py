#Facny name for an ARRAY.
List = [3,5,68,6]
print(type(List))

# Lists can contain multiple datatypes, unlike arrays (in other programming languages)
ListMultiple = ["A string!", 45, True, 7.2, "DummyText","Playing With Lists","Python"]
print(ListMultiple)
print(ListMultiple[2]) #Access the 2nd element (from zero) in the list.

#Negative indexing
print(ListMultiple[-2]) # len(ListMultiple)-3, gives the index of this.

# Suppose the length of list is 5, and we want index at -3, we subtract 5-3 and get 2, now what element is standing at 2? (thats the answer)
#or count the 3rd element from last.

# Using 'in' keyword for checking an element inside the list.
if 45 in ListMultiple:
    print("Yes it is here!")
else:
    print("You have to find that elsewhere!")

######################################################
# same we can do with strings!
if "con" in "Falcon":
    print("Found it!")
else:
    print("No, not here!")
######################################################

# List Slicing
print(ListMultiple[1:5]) #from index one till index five (5th index not included)
print(ListMultiple[1:]) #from index one till end
print(ListMultiple[1:-4]) #from index one till (covert the -ve index into positive by subtracting it from the length)
print(ListMultiple[1::2]) #from index one till end, every 2nd element is selected
print(ListMultiple[1:100]) #Still whole list is selected, with no error
print(ListMultiple[1::100]) #Only print the first index, can't skip 100 elements so leaves it there.

# List Comprehension
ListOnTheFly = [Item for Item in range(10)]
print(ListOnTheFly) # will print from 0 till 10 (not 10)

ListOnTheFly = [Item*2 for Item in range(10)]
print(ListOnTheFly) # will print from 0 till 10 (not 10), multiplying by 2

ListOnTheFly = [Item*Item for Item in range(10) if Item%2 == 0]
print(ListOnTheFly) # will print from 0 till 10 (not 10), Squaring them, and printing only characters which are divisible by 2

Names = ["Camel", "Cow", "Ant", "Horse", "Bat", "Crow", "Eagle", "Cat" ]
NamesWithC = [CNames for CNames in Names if CNames.startswith("C")]
print(NamesWithC)
NamesWithC = [CNames for CNames in Names if CNames.endswith("t")]
print(NamesWithC)