# Write a program that prompts the user to enter their score (out of 100) and
# displays their corresponding grade.

score = input("What is your score?")
score = int(score)

if score >= 90:
    print("Your score is A")
elif score >= 80:
    print("Your score is B")
elif score >= 70:
    print("Your score is C")
elif score >= 60:
    print("Your score is D")
else:
    print("Your score is F")

