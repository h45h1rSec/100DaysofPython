# The break statement enables a program to skip over a part of the code. It terminates the very loop it lies with in.

# In short the break statement helps us to jump out of the current code block of loop...

for i in range(12):
    i+=1 # i = i + 1
    print("5 X", i, "=", 5*i)
    # print(i)
    if(i == 5):
        print("Get out of loop!")
        break
        print("Okay, getting out!") #This will not be executed! Because the loop broke at the previous statement.

print("I am out of the loop!\n\n\n")

# The continue statement enables a program to skip over an iteration of the code. It skips the very loop it lies with in for only a specific condition.

SomeTuple = ("Goat", "Hen", "Sheep", "Duck", "Cow", "Camel")

for j in SomeTuple:

    if (j == "Duck" or j == "Hen"):
        continue #Will continue to iterate the loop, but skipping the rest of the code (code written after continue) inside the loop body.

    print(j) # Will skip the name of both birds...



    #########################

# Emulating the do-while loop via break statement

k = 5

while True:
    print(k,"=",50%k)
    k+=1 # do block

    if(50%k == 0):
        print("Beacause, the remainder of 50 /",k,"=",50%k)
        break # while block