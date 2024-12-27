# 2.5.1.7 LAB: Palindromes
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    filtered_text = "".join(char.lower() for char in text if char.isalnum())
    # Check if the filtered text is the same as its reverse
    return filtered_text == filtered_text[::-1]

# Ask for user input
text = input("Enter some text: ")

# Check if it's a palindrome
if is_palindrome(text):
    print("It's a palindrome")
else:
    print("It's not a palindrome")
