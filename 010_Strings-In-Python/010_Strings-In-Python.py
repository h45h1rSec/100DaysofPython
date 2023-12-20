# Every thing enclosed in qoutes is a string
Example = "An example of a string"
Challange = '100DaysOfPython'
AnotherExample = "25"

print("He said he won't eat an apple") #enclose in double qoutes if the string contains single qoutes
print('He said he want eat an "apple"') #enclose in single qoutes if the string contains double qoutes
print("He said he doesn\'t like \"Peas\"") #Use escape sequences if both are required.

# print("
# String can 
# span 
# multiple 
# lines?
# ") #unterminated string literal, or EOL (End Of Line Error)

print("""
String can 
span
multiple 
lines?
""") # Using triple qoutes, it is possible!

#################################

print(Challange[0]) #Return 0th character of string... '1' in this case.
#String is LIKE AN array of characters.

# for character in Example:
#     print(character) # Prints all characters one by one