String = "Hellow, brother!"

print(len(String)) # Returns length of a string.

# String Slicing

# SYNTAX: String[startIndex:endIndex]
#Think string as an array of characters.

print(String[0:5]) # will print from 0 till 5th character (not the 5th character)...
print(String[0:10]) # will print from 0 till 10th character (not the 10th character)...
print(String[:5]) # Python will consider the starting index as zero.
print(String[0:]) # Python will consider the ending index as full string length.
print(String[:]) # Python will consider the ending index as len(String).

#Negative Slicing
print(String[0:-3]) # Will cut of last three characters. or "len(String)-3".
print(String[-5:-2]) # same as: String[len(String)-5:len(String)-1]

String2 = "Harry"
print(String2[-4:-2])
print (String2[len(String2)-4:len(String2)-2])
print(len(String2))
