# 4.6.1.13 LAB: the calendar module
from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
        count = 0

        for month in range(1, 13):  # Loop through all months
            for week in self.monthdays2calendar(year, month):  # Retrieve weeks
                for day, day_week in week:  # Retrieve days within the week
                    if day != 0 and day_week == weekday:  # Exclude padding days (zeros)
                        count += 1

        return count

# Example usage
my_cal = MyCalendar()

# Test cases
print(my_cal.count_weekday_in_year(2019, 0))  # Expected output: 52 (Mondays in 2019)
print(my_cal.count_weekday_in_year(2000, 6))  # Expected output: 53 (Sundays in 2000)
print(my_cal.count_weekday_in_year(2024, 1))  # Example: Tuesdays in 2024

