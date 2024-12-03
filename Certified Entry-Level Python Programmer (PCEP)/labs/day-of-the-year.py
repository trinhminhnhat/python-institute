# 4.3.1.8 LAB: Day of the year: writing and using your own functions
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    return True

def days_in_month(year, month):
    # Validate inputs
    if year < 1 or month < 1 or month > 12:
        return None

    # List of days for each month
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust for February in leap years
    if month == 2 and is_year_leap(year):
        return 29

    # Return the number of days for the given month
    return days_in_months[month - 1]

def day_of_year(year, month, day):
    # Validate inputs
    if month < 1 or month > 12 or day < 1:
        return None

    # Check if the day is valid for the given month and year
    days_in_current_month = days_in_month(year, month)
    if days_in_current_month is None or day > days_in_current_month:
        return None

    # Calculate the day of the year
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)

    total_days += day
    return total_days

# Testing the functions
test_cases = [
    (2000, 12, 31, 366),  # Leap year, last day
    (2000, 2, 29, 60),    # Leap year, last day of February
    (1900, 3, 1, 60),     # Non-leap year
    (2024, 1, 1, 1),      # Leap year, first day
    (1987, 11, 30, 334)   # Non-leap year
]

for year, month, day, expected in test_cases:
    result = day_of_year(year, month, day)
    print(f"Year {year}, Month {month}, Day {day} ->", end=" ")
    if result == expected:
        print(f"OK (Day of year: {result})")
    else:
        print(f"Failed (Expected: {expected}, Got: {result})")

# Additional user input
input_year = int(input("Enter a year: "))
input_month = int(input("Enter a month (1-12): "))
input_day = int(input("Enter a day (1-31): "))
day_of_year_result = day_of_year(input_year, input_month, input_day)
if day_of_year_result is None:
    print("Invalid input.")
else:
    print(f"The year {input_year}, month {input_month}, day {input_day} is day {day_of_year_result} of the year.")
