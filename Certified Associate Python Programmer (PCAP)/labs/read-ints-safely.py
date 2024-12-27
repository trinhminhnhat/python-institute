# 2.8.1.4 Reading ints safely
def read_int(prompt, min, max):
    while True:
        try:
            # Prompt the user for input
            value = int(input(prompt))
            # Check if the value is within the specified range
            if value < min or value > max:
                print(f"Error: the value is not within permitted range ({min}..{max})")
            else:
                return value
        except ValueError:
            # Handle non-integer input
            print("Error: wrong input")

# Call the function and test
v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
