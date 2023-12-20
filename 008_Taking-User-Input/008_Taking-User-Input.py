Inp = input()
print("My input is: ",Inp)

Inp2 = input("Enter your value: ")
print("Your value is: ",Inp2)

Inp3 = float(input("Enter int: ")) # generate error, if other than int provided

# by default input() takes values as strings...

value = input("Enter your number: ")
value2 = input("Enter your number 2: ")

print(value+value2) #Will concatinate
print(int(value) + float(value2))