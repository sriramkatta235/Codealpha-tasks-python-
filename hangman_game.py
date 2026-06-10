import random

words = ["python", "apple", "house", "river", "music"]
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")

while incorrect_guesses < max_incorrect:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        guessed_letters.append(guess)
        incorrect_guesses += 1
        print("Wrong guess! Remaining attempts:", max_incorrect - incorrect_guesses)

if incorrect_guesses == max_incorrect:
    print("Game Over! The word was:", word)
