# 3.2.1.14 LAB: Essentials of the while loop
blocks = int(input("Enter the number of blocks: "))

# # Initialize variables
height = 0

# Build the pyramid
while blocks > height:
    height += 1 # Increase the height of the pyramid
    blocks -= height

print("The height of the pyramid:", height, ", blocks left:", blocks)
