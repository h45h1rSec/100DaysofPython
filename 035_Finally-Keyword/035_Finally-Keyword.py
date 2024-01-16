#The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

# try:
#     num = int(input("Enter a Number: "))
# except ValueError:
#     print("Hey! this is not an integer!")
# else: 
#     print(f"OK, {num} is accepted as an integer!")
# finally:
#     print("Ok, have fun...")

###########################
# WHY FINALLY IS USED?
def SimpleFuntion():
    List = ["Karachi", "Lahore", "Multan", "Islamabad"]

    Index = 0
    for City in List:
        print(str(Index) + ".",City)
        Index += 1

    InputCity = int(input("\nEnter your home city Number: "))

    try:
        print("Hmm, you live in",List[InputCity])
        return List[InputCity]

    except IndexError:
        print("Maybe, your city is not listed...")
        return List

    finally:
        print("Even the function returned a value, but I'll still say: Goodbye!")

    print("This won't run as function returned a value, and exitted...")


Returned = SimpleFuntion()
print(f"\nThe value returned by the function is '{Returned}'") #Prints the returned value... as well.