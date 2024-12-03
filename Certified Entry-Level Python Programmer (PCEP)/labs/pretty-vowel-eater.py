# 3.2.1.11 LAB: The continue statement - the Pretty Vowel Eater
word_without_vowels = ""
user_word = input("Enter a word : ")
user_word = user_word.upper()

for letter in user_word:
    if (letter in ("U", "E", "O", "A", "I")):
        continue
    word_without_vowels += letter

print(word_without_vowels)
