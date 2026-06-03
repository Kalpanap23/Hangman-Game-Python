import random

# List of predefined words
words = ["python", "laptop", "coding", "mobile", "camera"]

# Randomly select a word
secret_word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(secret_word)

# Store guessed letters
guessed_letters = []

# Maximum wrong attempts
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", guessed_letters)
    print("Remaining Attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet!")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Correct Guess
    if guess in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

        print("Correct Guess!")

    else:
        attempts -= 1
        print("Wrong Guess!")

# Result
if "_" not in guessed_word:
    print("\nCongratulations!")
    print("You guessed the word:", secret_word)

else:
    print("\nGame Over!")
    print("The word was:", secret_word)