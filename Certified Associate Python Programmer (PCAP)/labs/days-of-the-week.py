# 3.4.1.13 LAB: Days of the week
class WeekDayError(Exception):
    """Custom exception for invalid weekday."""
    pass

class Weeker:
    # List of valid weekdays
    __days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in Weeker.__days:
            raise WeekDayError("Invalid day provided")
        self.__current_day_index = Weeker.__days.index(day)  # Store the index of the current day

    def __str__(self):
        return Weeker.__days[self.__current_day_index]  # Return the current day as a string

    def add_days(self, n):
        # Update the day forward by n days
        self.__current_day_index = (self.__current_day_index + n) % len(Weeker.__days)

    def subtract_days(self, n):
        # Update the day backward by n days
        self.__current_day_index = (self.__current_day_index - n) % len(Weeker.__days)


# Test the Weeker class
try:
    weekday = Weeker('Mon')  # Initialize with "Mon"
    print(weekday)           # Output: Mon
    weekday.add_days(15)     # Move forward 15 days
    print(weekday)           # Output: Tue
    weekday.subtract_days(23)  # Move backward 23 days
    print(weekday)           # Output: Sun
    weekday = Weeker('Monday')  # Invalid day should raise WeekDayError
except WeekDayError:
    print("Sorry, I can't serve your request.")
