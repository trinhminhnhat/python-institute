# 3.1.1.12 LAB: Essentials of the if-elif-else statement
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian Calendar!")
elif year % 4 != 0:
    print("Common Year")
elif year % 100 != 0:
    print ("Leap Year")
elif year % 400 != 0:
    print ("Common Year")
else:
    print("Leap Year")
