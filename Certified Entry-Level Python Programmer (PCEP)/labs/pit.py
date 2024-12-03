# 3.1.1.11 LAB: Essentials of the if-else statement
income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = (0.18 * income) - 556.02

    if tax < 0:
        tax = 0.0
else:
    tax = 14839.02 + (0.32 * (income - 85528))

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
