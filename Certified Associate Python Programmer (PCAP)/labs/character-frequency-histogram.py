# 4.3.1.15 LAB: Character frequency histogram
from os import strerror

# Ask the user for the input file's name
file_name = input("Enter the name of the file: ")

try:
    # Dictionary to store letter frequencies
    letter_counts = {}

    # Open and read the file
    with open(file_name, 'r') as file:
        for line in file:
            for char in line:
                # Normalize to lowercase and check if it's a Latin letter
                if char.isalpha():
                    char = char.lower()
                    if char in letter_counts:
                        letter_counts[char] += 1
                    else:
                        letter_counts[char] = 1

    # Print the histogram in alphabetical order
    for letter in sorted(letter_counts):
        print(f"{letter} -> {letter_counts[letter]}")

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
