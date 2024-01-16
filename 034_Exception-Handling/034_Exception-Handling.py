# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

# Table = input("Enter the number: ")
Table = "5" #Assuming that user entered "45".

try:
    Table = int(Table)

    for num in range(1,13):
        String = f"{Table} X {num} = {Table*num}"
        print(String)
        
except Exception as error:
    print(error)
    print("That was unexpected!")


print("This line must run!")

# Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

try:
    num = int(input("Enter an integer: "))
    List = ["A", "B", "C", "D"]
    print(List[num])

except ValueError: # Multiple types of errors can be handled
    print("Number entered is not an integer.")

except IndexError: #multiple exceptions can be used with single 'try' statement.
    print("This is an index error...")