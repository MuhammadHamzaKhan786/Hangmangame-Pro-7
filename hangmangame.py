# Project 8 : Hangman Game in Python

import random
words = ['enum', 'python', 'collab', 'vscode', 'game']

word = random.choice(words)
guesses_letters = []
attempts = 6

print("Welcome to Hangman!")
print("_" * len(word))

while attempts > 0:
    guess = input ("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guesses_letters:
        print("You already guessed that letter.")
        continue

    guesses_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! {attempts} attempts left.")

    display_word = ''.join([letter if letter in guesses_letters else '_' for letter in word])
    print(display_word)

    if "_" not in display_word:
        print(f"Congratulations! You've guessed the word:{word}")
        break
else:
    print(f"Game Over! The word was: {word}")
# End of the Hangman game code
