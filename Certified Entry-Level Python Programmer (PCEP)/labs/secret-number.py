# 3.2.1.3 LAB: Essentials of the while loop - Guess the secret number
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = int(input("Enter an integer: "))

while guess != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess = int(input("Please, try again: "))

print("Well done, muggle! You are free now.")

