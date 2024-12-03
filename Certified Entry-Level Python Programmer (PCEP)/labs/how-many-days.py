# 4.3.1.7 LAB: How many days: writing and using your own functions
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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end=" ")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK", result, "days")
	else:
		print("Failed.", "Right answer is", result, "days")

# Additional user input
input_year = int(input("Enter a year: "))
input_month = int(input("Enter a month (1-12): "))
days = days_in_month(input_year, input_month)
if days is None:
    print("Invalid input.")
else:
    print(f"The year {input_year}, month {input_month} has {days} days.")
