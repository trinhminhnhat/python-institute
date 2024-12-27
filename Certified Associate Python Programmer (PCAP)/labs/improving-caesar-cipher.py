# 2.5.1.6 LAB: Improving the Caesar cipher
def caesar_cipher():
    # Ask the user for the text to encrypt
    text = input("Enter the text to encrypt: ")

    # Validate the shift value
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if 1 <= shift <= 25:
                break
            else:
                print("Shift value must be between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 25.")

    # Encrypt the text
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            start = ord('A') if char.isupper() else ord('a')  # Determine case
            # Shift the character within the alphabet
            encrypted_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += encrypted_char
        else:
            # Keep non-alphabetical characters unchanged
            encrypted_text += char

    # Print the encrypted text
    print("Encoded text:", encrypted_text)

# Run the function
caesar_cipher()
