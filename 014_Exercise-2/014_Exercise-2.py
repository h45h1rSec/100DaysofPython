# HINT: https://docs.python.org/3/library/time.html#time.strftime

import time

Hours = time.strftime('%H')
Minutes = time.strftime('%M')
Seconds = time.strftime('%S')
Day = time.strftime('%A')

Hours = int(Hours)

if(Day!="Sunday"):

    if(Hours<12 and Hours>5):
        print("Good Morning Sir!")
    elif(Hours>=12 and Hours<17):
        print("Good afternoon sir!")
    elif(Hours>=17 and Hours<=19):
        print("Good Evening sir!")
    elif(Hours>19 and Hours<=23 or Hours<=5):
        print("Good Night sir!")
    else:
        print("Invalid Time sir!")
else:
    print("Happy Sunday Sir!")


print(f"\n{Hours}:{Minutes}:{Seconds} And today is: {Day}")
