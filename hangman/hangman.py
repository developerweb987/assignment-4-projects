import random
import string

# Word list (you can expand this or load from a file)
word_list = ["python", "hangman", "challenge", "programming", "developer", "kylie", "project"]

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    word = get_valid_word(word_list)
    word_letters = set(word)        # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()            # Letters guessed by the user

    lives = 6

    print("🎮 Welcome to Hangman!")
    print("You have 6 lives. Try to guess the word, one letter at a time.\n")

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Show current state
        print("You have", lives, "lives left.")
        print("Used letters:", ' '.join(sorted(used_letters)))

        # Show current word progress
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_display))

        # Get user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct!\n")
            else:
                lives -= 1
                print("Wrong! That letter is not in the word.\n")
        elif user_letter in used_letters:
            print("You've already guessed that letter. Try again.\n")
        else:
            print("Invalid input. Please enter a letter.\n")

    # End of game
    if lives == 0:
        print(f"☠️ You died! The word was: {word}")
    else:
        print(f"🎉 You guessed the word: {word}!")

# Run the game
if __name__ == "__main__":
    hangman()
