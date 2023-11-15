# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# this imports the random library
import random

# explains what program does
print('This program determines if a caller is a telemarketer or not.')

# this series of variables chooses a number between 1 and 9
num1 = random.randint(1,9)

print(num1)

num2 = random.randint(1,9)

print(num2)

num3 = random.randint(1,9)

print(num3)

num4 = random.randint(1,9)

print(num4)

# this function determines if the number aligns with known telemarketer numbers
def call_id():
    if num1 == 8 or num4 == 8 or num1 == 9 or num4 == 9 or num2 == num3:
        print('telemarketer')
    #elif num2 == num3:
        #print('telemarketer')
    else:
        print('caller')

call_id()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
