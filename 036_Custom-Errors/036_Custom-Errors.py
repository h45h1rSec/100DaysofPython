# In python, we can raise custom errors by using the raise keyword.


# a = int(input("Enter any value between 5 and 9: "))

# if(a<5  or a>9):
#     raise  ValueError("Value should be between 5 and 9")
#   #To raise a different error, check pythons error docs.  

# else:
#     print("The value is:",a)

# THIS WILL MAKE SENSE WHEN WE STUDY CLASSES

# class CustomError(Exception):
#   # code ...
#   pass
# try:
#   # code ...
# except CustomError:
#   # code...


# QUIZ
# write a program which raises an error like the above one, but not when user inputs "quit"

Input = input("Enter any number between 5 and 9: ")
    
if (Input.lower() == "quit"):
    print("Exiting...")

elif (Input.isdigit()):
    if (int(Input)>5 and int(Input)<9):
        print("You number is:",Input)
    else:
        raise ValueError("The number in not Matched")
        
else:
    raise ValueError("Please enter a valid integer!")


