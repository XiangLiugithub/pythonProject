# Asks the user to input a number, the program then uses the
# input number as the max range for fizzbuzz

import time

choice = int(input("What number would you like to choose?"))


def functions(choice):
    for num in range(1, choice):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)


# Message the user the program is about to run, waits 1 second

print("about to run the program...")
time.sleep(1)
functions(choice)

# Create a program that can take in input of the users name
# save the name in a variable
# pass the variable through a function and print "Hello _____"
# My attempt

fullname = input("What is your full name?")

def greeting(fullname):
    print(f"Hello {fullname}")

greeting(fullname)
