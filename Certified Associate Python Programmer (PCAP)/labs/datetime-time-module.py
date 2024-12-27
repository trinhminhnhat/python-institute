# 4.5.1.22 LAB: The datetime and time modules
from datetime import datetime

# Create the datetime object
dt = datetime(2024, 12, 12, 11, 5, 0)

# Display the formatted datetime
print(dt.strftime("%Y/%m/%d %H:%M:%S"))                  # 2020/11/04 14:53:00
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))               # 20/November/04 14:53:00 PM
print(dt.strftime("%a, %Y %b %d"))                       # Wed, 2020 Nov 04
print(dt.strftime("%A, %Y %B %d"))                       # Wednesday, 2020 November 04
print(dt.strftime("Weekday: %w"))                        # Weekday: 3
print(dt.strftime("Day of the year: %j"))                # Day of the year: 309
print(dt.strftime("Week number of the year: %U"))        # Week number of the year: 44
