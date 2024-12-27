# 2.5.1.8 LAB: Anagrams
def are_anagrams(text1, text2):
    # Remove spaces and convert to lowercase
    clean_text1 = "".join(char.lower() for char in text1 if char.isalnum())
    clean_text2 = "".join(char.lower() for char in text2 if char.isalnum())

    # Check if sorted versions of the strings are the same
    return sorted(clean_text1) == sorted(clean_text2)

# Ask the user for two inputs
text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

# Check and print the result
if are_anagrams(text1, text2):
    print("Anagrams")
else:
    print("Not anagrams")
