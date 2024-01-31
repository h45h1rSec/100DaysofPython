# The enumerate() function adds a counter to an iterable and returns it as an enumerate object (iterator with index and the value).

Marks = [25, 56, 75, 98, 12, 3]
# if marks reach at 98, print "impressive"

for Temp in Marks:
    
    if Temp == 98:
        print("Impressive!")
        continue

    print(Temp)
########################################################

languages = ['Python', 'Java', 'JavaScript']

# enumerate the list
enumerated_languages = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_languages))

# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

# SYNTAX:
# enumerate(iterable, start=0) #you can change the start index

# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# By default enumerate() returns a tuple, we used "index, fruit", so the tuple is unpacked.

# Linter is a process for identifying bugs and styling errors in our code.