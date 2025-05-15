import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator")

    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        password_length = int(input("What should be the length of each password? "))

        print("\nHere are your passwords:")
        for i in range(num_passwords):
            print(f"{i + 1}: {generate_password(password_length)}")

    except ValueError:
        print("❌ Please enter valid numbers for quantity and length.")

# Run the generator
if __name__ == "__main__":
    main()
