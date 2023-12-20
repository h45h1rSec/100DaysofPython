# There are four types of arguments which can be passed in a function

# 1. Default Arguments
# 2. Keyword Arguments
# 3. Variable Length Arguments
# 4. Required Arguments

## Default Arguments
def SUM(a=4,b=6):
    print(a+b)

SUM() #Return with default arguments
SUM(7,4) #Overwrite the default arguments
SUM(b=1) #we can give one value, other is taken as default... 
SUM(8) #only the first argument variable is overwritten... 

def Greet(Fname="Mr",Mname="John",Lname="Doe"):
    print("Greetings,",Fname,Mname,Lname)

# Examples of taking default value if they are not specified
Greet("Harry")
Greet("Harry","James")
Greet("Harry","James","Potter")

#We can also change orders of arguments.
def DIFF(a,b):
    print("The difference of",a,"and",b,"is",a-b)

DIFF(7,5)
DIFF(b=5,a=7) # Same thing as above, but order changes... (order does not matter if we specify the variable name)

##Required Arguments
def MultBy2(a,b):
    print((a+b)*2)

MultBy2(4,5) #Both arguments are required, other wise you have to face an exception


##Keyword Arbitary Arguments

def Average(*Numbers): #Numbers is taken as a TUPLE, for DICTIONARY use **, like **Numbers
    sum = 0
    for i in Numbers:
        sum += i
    # print("The Average of",len(Numbers), "numbers is:",sum/len(Numbers))
    # print("The type of Numbers: ",type(Numbers))
    return sum/len(Numbers) #returns a value but not print it...
    return 7 #only the first return is considered, other than it will be ignored

c = Average(5,6,5)
print(c)
