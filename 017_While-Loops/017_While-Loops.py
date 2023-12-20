i = 2

while i<=10: # Parenthesis are optional
    print(i)
    i += 2 # same as: "i = i + 2"

# Mostly while loop is used with complex conditions, (not with numbers mostly)

# Check = int(input("Enter the number: "))

# while(Check<=100): # we have to false the conditon to stop the loop
#     Check = int(input("Enter the number: "))

# print("Exit...")

# We can use else with while loop 
while i >= 15:
    print(i)
else:
    print("I am outside the loop, but inside the else block!")
    #When loop's condition become false, else statement is executed.


# There is no 'do-while' loop in python

# but we emulate the do-while loop via break statements with if-else
