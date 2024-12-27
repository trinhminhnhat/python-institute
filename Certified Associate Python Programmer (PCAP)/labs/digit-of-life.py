# 2.5.1.9 LAB: The Digit of Life
def digit_of_life(birthday):
    # Repeat the summing process until a single digit is obtained
    while len(birthday) > 1:
        # Sum the digits of the current string
        birthday = str(sum(int(digit) for digit in birthday))
    return int(birthday)

# Ask the user for their birthday
birthday = input("Enter your birthday (YYYYMMDD or other format): ")

# Validate the input
if birthday.isdigit():
    result = digit_of_life(birthday)
    print("The Digit of Life is:", result)
else:
    print("Invalid input. Please enter your birthday as a numeric string (e.g., 19991229).")
