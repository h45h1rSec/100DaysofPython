String = "python is a WONDERFUL language..."

print(len(String)) #prints length of a string
print(String.upper()) # Converts the sting into upper case
print(String.lower()) # Converts the sting into lower case

# Strings are immutable (unchangeable) and if any function like .upper() is applied, it creates a copy of that string, doesnt change that.

print(String) #Original string is printed

print(String.rstrip(".")) # Strips or removes the trailing characters.
print(String.replace("WONDERFUL", "powerful")) # Replaces a given part of string with another given part of string. it is case-sensitive
print(String.split("a")) #Splits the string into a list using the given parameter. does not inclue the given parameter in the list.
print(String.capitalize()) # Converts first letter to upper case. and others to lower case
print(String.center(50)) # Adds (whitespaces) characters to reach the specified length, in this case '50'. if the string length is 30, it will add 20 spaces.
print(String.count("n")) # counts the given string in the specified string.
print(String.endswith("...")) # checks if the given string is ended with the passed string. returns boolean
print(String.startswith("...")) # checks if the given string is started with the passed string. returns boolean
print(String.find("Wonder")) # Returns index of the string (detects the first occurance), returns -1 if string not found.
print(String.index("WON")) # Also returns index of the string (detects the first occurance), but raises an exception if string not found.
print(String.isalnum()) # Checks if the string only contains letters and number, otherwise it will return false.
print(String.isalpha()) # Checks if the string only contains letters, otherwise it will return false.
print(String.islower()) # Checks if the string don't contains upper case letters, otherwise it will return false. (numbers and special characters don't matter)
print(String.isupper()) # Checks if the string don't contains lower case letters, otherwise it will return false. (numbers and special characters don't matter)
print(String.isprintable()) # Checks if the string only contains printable charcters, no escape sequences etc.
print(String.isspace()) #Checks if string contains only whitespaces, returns 'true' if so.
print(String.istitle()) # Checks if every word's first letter is capital, returns 'true' if so.
print(String.title()) # Converts if every word's first letter in capital.
print(String.swapcase()) # Toggle case