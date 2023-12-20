# For loops can iterate over a sequence  of iteraable objects in python.

for i in "Hello":
    # Every element in the given value is stored into i and then printed
    print(i)

Colors = ["Red", "Yellow", "Green", "Blue"]

for x in Colors:
    print(x)


#SYNTAX: range(start, stop, step)

for num in range(10,50): #Range() is to give range of number.
    print(num)

for num2 in range(10): #Range() will take starting from zero.
    print(num2)

for num3 in range(10,50,5): #Range()'s third argument defines step length (how much to skip in between the given two values)
    print(num3)


# We can iterate dictionaries and tuples etc.

UserTable = int(input("Enter a number to get its table till 12: "))
print("Print a multiplication table of: ",UserTable)

for Multiply in range(1,13):
    print(f"{UserTable} x {Multiply} = {UserTable*Multiply}")

