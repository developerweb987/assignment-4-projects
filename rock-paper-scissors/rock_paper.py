import random

def play():
    print("Welcome to Rock, Paper, Scissors!")
    user = input("Type Rock, Paper, or Scissors: ").lower()
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)

    if user not in choices:
        return "Invalid choice. Please try again."

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"

    # Define the winning rules
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'scissors' and computer == 'paper') or \
       (user == 'paper' and computer == 'rock'):
        return "You win! 🎉"

    return "You lose! 😢"

# Run the game
if __name__ == "__main__":
    while True:
        result = play()
        print(result)

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
