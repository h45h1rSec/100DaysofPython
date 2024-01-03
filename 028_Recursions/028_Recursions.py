# Recursions are basically also functions, but inside a funtions you call the same function is called recursion! (A function which calls itself is called recursion)



def Factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return (n*Factorial(n-1)) #Fucntion calls itself

print(Factorial(5))

## Flow of the program
# The 'if' block is not executed as n!= 0 or n!=1
# In the 'else' block, it returns 5 multiplied by the output of Factorial(4).
# Same it does agian and again until, it becomes 1.
# After the fuctions runs with argument as '1' then the if block is executed and function is not called again.

# QUIZ OF FIBONACCI SEQUENCE

def Fibonacci(num):
    if (num == 0) or (num == 1):
        return num
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)

print(Fibonacci(7)) 

#Start: The Fibonacci sequence starts with two initial numbers: 0 and 1.
# Rule: Each subsequent number in the sequence is the sum of the two preceding numbers.
# So, it goes like this:
# 0, 1, 1 (0 + 1), 2 (1 + 1), 3 (1 + 2), 5 (2 + 3), 8 (3 + 5), 13 (5 + 8), and so on.