# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import random
import string

def Encoding(Message):
    if len(Message) > 3: #if the word is greater than 3
        Encoded = Message[1:] + Message[0] #Remove first character and append to last...
        Encoded = ''.join([random.choice(string.ascii_letters) for _ in range(3)]) + Encoded + ''.join([random.choice(string.ascii_letters) for _ in range(3)]) #Add random 3 chracters to first and last.
        return Encoded
    else:
        return Message[::-1]

def Decoding(Message):
    if len(Message) > 3: #if the word is greater than 3
        Decoded = Message[3:-3] #Remove random 3 chracters from first and last.
        Decoded = Decoded[-1] + Decoded[:-1] #Remove the last character and append to the beginning
        return Decoded
    else:
       return Message[::-1] 

###FUNCTIONS DEFINED###

print("Hello, this is your secret coder agent...\n")

Secret = input("Hmm! No one is watching... Hurry up. Type the message: ")

SelectMethod = input("Press (E) for encoding.\nPress (D) for decoding.\nEnter your option: ").lower()
print(SelectMethod)

if SelectMethod == 'e':

    EncodedMessage = ' '.join([Encoding(Secret) for word in Secret.split()])
    print("Encoded Message:", EncodedMessage)

elif SelectMethod == 'd':

    DecodedMessage = ' '.join([Decoding(Secret) for word in Secret.split()])
    print("Decoded Message:", DecodedMessage)

else:

    print("Hmm... Looks like I don't know what to do...")