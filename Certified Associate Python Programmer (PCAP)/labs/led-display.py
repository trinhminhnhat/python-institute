# 2.4.1.6 LAB: A LED Display
def seven_segment_display(number):
    # Define patterns for each digit in a seven-segment display
    digits = [
        ["###", "# #", "# #", "# #", "###"],  # 0
        ["  #", "  #", "  #", "  #", "  #"],  # 1
        ["###", "  #", "###", "#  ", "###"],  # 2
        ["###", "  #", "###", "  #", "###"],  # 3
        ["# #", "# #", "###", "  #", "  #"],  # 4
        ["###", "#  ", "###", "  #", "###"],  # 5
        ["###", "#  ", "###", "# #", "###"],  # 6
        ["###", "  #", "  #", "  #", "  #"],  # 7
        ["###", "# #", "###", "# #", "###"],  # 8
        ["###", "# #", "###", "  #", "###"],  # 9
    ]

    # Convert input number to string for easier processing
    number_str = str(number)
    output_lines = [""] * 5  # There are 5 rows in the display

    # Build the display row by row
    for digit in number_str:
        digit = int(digit)  # Convert each character back to an integer
        for i in range(5):
            # Append the corresponding row of the current digit
            output_lines[i] += digits[digit][i] + " "

    # Print the final display
    for line in output_lines:
        print(line.rstrip())  # Remove trailing whitespace for a clean display

# Test the function with sample inputs
print("Sample Input: 123")
seven_segment_display(123)

print("\nSample Input: 9081726354")
seven_segment_display(9081726354)
