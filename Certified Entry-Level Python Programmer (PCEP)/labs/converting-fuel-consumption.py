# 4.3.1.10 LAB: Converting fuel consumption
def liters_100km_to_miles_gallon(liters):
    # 1 mile = 1609.344 meters
    # 1 gallon = 3.785411784 liters
    # 1 km = 1000 meters
    # Conversion formula: mpg = (100 km * meters per km / meters per mile) / (liters / liters per gallon)
    miles_per_100km = 100 * 1000 / 1609.344
    gallons = liters / 3.785411784
    return miles_per_100km / gallons

def miles_gallon_to_liters_100km(miles):
    # Conversion formula: liters/100km = (100 km / miles) * (liters per gallon / meters per km * meters per mile)
    km_per_100miles = 100 / (miles / 1609.344)
    liters = 3.785411784
    return km_per_100miles * liters / 1000

# Testing the functions
print(liters_100km_to_miles_gallon(3.9))  # Expected: 60.31143162393162
print(liters_100km_to_miles_gallon(7.5))  # Expected: 31.36194444444444
print(liters_100km_to_miles_gallon(10.))  # Expected: 23.52145833333333
print(miles_gallon_to_liters_100km(60.3)) # Expected: 3.9007393587617467
print(miles_gallon_to_liters_100km(31.4)) # Expected: 7.490910297239916
print(miles_gallon_to_liters_100km(23.5)) # Expected: 10.009131205673757
