# 2.3.1.18 Your own split
def my_split(string):
    # Return an empty list if the input string is empty or contains only whitespace
    if string.strip() == "":
        return []

    result = []
    word = ""
    for char in string:
        if char.isspace():  # If the character is a whitespace
            if word:  # If a word has been accumulated, add it to the result
                result.append(word)
                word = ""  # Reset the word
        else:
            word += char  # Accumulate the character into the current word

    if word:  # Add the last word if there is one
        result.append(word)

    return result

print(my_split("To be or not to be, that is the question"))
print(my_split("To be or not to be,that is the question"))
print(my_split("   "))
print(my_split(" abc "))
print(my_split(""))
