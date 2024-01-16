# SYNTAX OF USING ELSE WITH LOOP 
# for counter in sequence:
#     #Statements inside for loop block
# else:
#     #Statements inside else block


# Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed. (means else is also the part of the loop, can't be executed when the loop is broken

for i in range(5):
    print(i,"is Inside")
else:
    print("just got outside...")


j = 0
while (j < 7):
    print("I am \"j\"",j)
    j += 1
else:
    print("Loop is ended...")


# IF THE LOOP IS BROKEN, ELSE BLOCK WOULD NOT RUN...
for k in range(5):
    print(k,"is Inside")
    if(k==2):
        break
else:
    print("just got outside...")
