def is_prime(num):
    # Prime numbers must be greater than 1
    if num <= 1:
        return False

    # Check divisors from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    # If no divisors were found, num is prime
    return True

# Testing the function with numbers from 2 to 20
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
