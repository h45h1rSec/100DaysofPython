# F-Strings allows us to palce variables in strings, this feature was introduced in python 3.6

RealName = "HASHIR"
Location = "HOME"

# F-Strings removed the frustation of string formatting
Sentence = "Hey! I am {} and I live in my {}"
print(Sentence)
print(Sentence.format(RealName,Location)) #It puts the values in the brackets.

###################

Sentence2 = "Hey! I am {1} and I live in my {0}"
print(Sentence2)#It puts the values in the brackets, but format is out of order, so we specified the numbers in the brackets.
print(Sentence2.format(Location,RealName)) 


# FSTRINGS MADE THIS ALOT EASIER
Sentence3 = f"Hey my name is {RealName}, and I live in my {Location}"
print(Sentence3)


# IF YOU HAVE TO PRINT THE STRING AS IT IS (in fstrings), USE DOUBLE BRACKETS 
Sentence4 = f"Hey my name is {RealName}, and I live in my {{Location}}"
print(Sentence4)
