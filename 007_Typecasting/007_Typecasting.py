# Changing the data type of a variable is called typecasting

Value1 = "1"
Value2 = "2"

print(Value1+Value2) #Concatinated

# Coverting into integers with int()
print(int(Value1)+int(Value2)) #Now result is '3'


# Two types of typecasting:
# Exlicit -> I am doing the typecasting, can be achieved with the help of Python's built-in functions like int(), float(), hex(), oct(), str() etc.
print(int("90")+int(10))

# Implicit -> Python is doing the typecasting, Python converts a smaller data type to higher data type to prevemt data loss
print(5+4.5) 

