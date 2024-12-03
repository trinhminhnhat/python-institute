# read the initial value of c0
c0 = int(input("Enter a natural number: "))

# validate input
if c0 <= 0:
    print("The number must be a natural number (greater than 0).")
else:
    steps = 0  # initialize the step counter

# Perform Collatz steps
while c0 != 1:
    if c0 % 2 == 0:  # check if c0 is even
        c0 = c0 // 2
    else:  # if c0 is odd
        c0 = 3 * c0 + 1
    print(c0)  # print the current value of c0
    steps += 1  # increment the step counter

# print the total number of steps
print("Steps =", steps)
