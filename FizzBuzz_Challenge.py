# Fizzbuzz challenge
# if a number is divisible by 3, print fizz
# if a number is divisible by 5, print buzz
# if divisible by both, print fizzbuzz
# if not divisible, print number

# My attempt
#
# for num in range (1, 100):
#     if num % 3 == 0:
#         if num % 5 == 0:
#             print ("fizzbuzz")
#         else:
#             print ("fizz")
#     elif num % 5 == 0:
#         print("buzz")
#     else:
#         print(num)

# Ryan's code (easier to understand in my opinion)

for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)