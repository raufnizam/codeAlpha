import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "kiwi", "strawberry", "melon", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    while True:
        word = choose_word()
        guessed_letters = []
        attempts = 6
        
        print(word)
        print("Welcome to Hangman!")
        print(display_word(word, guessed_letters))

        while attempts > 0:
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess not in word:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")

            print(display_word(word, guessed_letters))

            if "_" not in display_word(word, guessed_letters):
                print("Congratulations! You've guessed the word:", word)
                break

        if attempts == 0:
            print("Sorry, you've run out of attempts. The word was:", word)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

hangman()
