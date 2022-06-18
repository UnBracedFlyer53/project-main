import random
import string
print("The key aspects of a strong password are length (the longer the better); a mix of letters (upper and lower case), numbers, and symbols, no ties to your personal information, and no dictionary words.")
print("Don't worry, Today I'll build a Strong Password For You.")
length=int(input("\nHow Long Do you want the Password to be? :"))
password=""
while len(password)<length:
    alphabets=random.choice(string.ascii_letters)
    digits=random.choice(string.digits)
    symbols=random.choice(string.punctuation)
    d=random.choice([alphabets, digits, symbols])
    password=password+str(d)
print("The Password Generated for You is: ",password)