# 3.2.1.14 LAB: Essentials of the while loop
blocks = int(input("Enter the number of blocks: "))

# Initialize variables
height = 0
layer = 1 # The current layer to be built

# Build the pyramid
while blocks >= layer:
    blocks -= layer # Use blocks to build the current layer
    height += 1 # Increase the height of the pyramid
    layer += 1 # Move to the next layer

print("The height of the pyramid:", height, ", blocks left:", blocks)
