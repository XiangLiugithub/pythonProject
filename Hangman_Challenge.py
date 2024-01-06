import random

print("Welcome to Shawn's Hangman challenge")

wordlist = ["orange", "banana", "apple", "grape"]
secret_word = random.choice(wordlist)
display_word = []
for letter in secret_word:
    display_word += '_'
print(display_word)


game_over = False
while not game_over:
    guess = input("Guess a letter ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    print(display_word)

    if '_' not in display_word:
        print("You win")
        game_over = True
