# Mad Libs Project - Kylie Ying Inspired

def mad_libs():
    print("Let's play Mad Libs!\nFill in the blanks below:\n")

    # Get user inputs
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    noun2 = input("Enter another noun: ")
    verb1 = input("Enter a verb (past tense): ")
    adjective2 = input("Enter another adjective: ")
    noun3 = input("Enter one more noun: ")

    # Create the story using an f-string
    story = (
        f"Today I went to the {noun1}. I saw a(n) {adjective1} {noun2} "
        f"jumping up and down in its tree. He {verb1} through the large tunnel "
        f"that led to its {adjective2} {noun3}."
    )

    # Display the story
    print("\nHere's your Mad Libs story:\n")
    print(story)

# Run the game
if __name__ == "__main__":
    mad_libs()
