# Comment are defiend by '#'.

"""
Multi line comments
are defined as string literals
"""

'''
Also 
a multi 
line comment
'''
# ESCAPE SEQUENCE
print("Printing on a\nnew line.")
print("Print \"s\" in double qoutes")

print("Multiple different values", 5, 78, 2+1, sep=">") # sep='value' defines the value which is put into the gaps of the strings separated by comma in the statement. (by default is space)

print("Multiple different values", 5, 78, 2+1, sep=">", end="PopCorn ") # end='value' defiens on which chracter the statement ends, (by default is \n)
print("New line not here!")