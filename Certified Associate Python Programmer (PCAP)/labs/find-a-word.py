# 2.5.1.10 LAB: Find a word!
def are_characters_hidden(word, combination):
    # Initialize position to start searching
    position = 0
    for char in word:
        # Find the character in the combination starting from the current position
        position = combination.find(char, position)
        if position == -1:  # If the character is not found
            return "No"
        position += 1  # Move to the next position
    return "Yes"

# Input from the user
word = input("Enter the first string (word): ").lower()
combination = input("Enter the second string (combination): ").lower()

# Output the result
print(are_characters_hidden(word, combination))
