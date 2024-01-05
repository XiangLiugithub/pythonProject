# Write a program that prompts the user to enter their score (out of 100) and
# displays their corresponding grade.

score = input("What is your score?")
score = int(score)

# NestedIfStatements: If you are under the age
# of 10, and you got an A or B, you get a +

if score >= 90:
    age = int(input("What is your age?"))
    if age < 10:
        print("Your score is an A+")
    else:
        print("Your score is A")
elif score >= 80:
    age = int(input("What is your age?"))
    if age < 10:
        print("Your score is an B+")
    else:
        print("Your score is B")
elif score >= 70:
    print("Your score is C")
elif score >= 60:
    print("Your score is D")
else:
    print("Your score is F")