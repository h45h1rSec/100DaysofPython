# A piece of code which has to be used multiple time in a program.

# For example we write a program which prints the average of two numbers, we dont have to write the statements in that program again and again, we build a function and call it multiple times.

def AvgOfTwo(Num1, Num2): # Defining a function.
    #Function body
    Avg = (Num1 + Num2) / 2
    print(Avg)

    if Num1>Num2:
        print(Num1, "is greater than", Num2)
    elif(Num1 == Num2):
        print("Both numbers are equal!")
    else:
        print(Num2, "is greater than", Num1)

AvgOfTwo(4,9) #Calling the function...



def BigFunction():
    pass # The pass statement in Python is a null operation; it doesn't do anything. It's often used as a placeholder when syntactically some code is required, but you don't want to execute any statements.

BigFunction() #nothing happens if function body is empty!




# 1. Built-in functions -> min(), max(), sum(), etc
# 2. User-defined functions -> user has to build that function by himself.


# SYNTAX:
# def FunctionName(Arguments,OtherArguments):
#     Function body