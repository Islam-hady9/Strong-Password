import string
import random

s1 = list(string.ascii_lowercase) #30%
s2 = list(string.ascii_uppercase) #30%
s3 = list(string.digits) #20%
s4 = list(string.punctuation) #20%

characters_number = input("How many characters for the password?: ")

while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6:
            print("You neet at least 6 characters")
            characters_number = input("Please enter the number again: ")
        else:
            break
    except:
        print("Please enter numbers only")
        characters_number = input("How many characters for the password?: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(characters_number * (30 / 100))
part2 = round(characters_number * (20 / 100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:])
print("The password is\t" + password)