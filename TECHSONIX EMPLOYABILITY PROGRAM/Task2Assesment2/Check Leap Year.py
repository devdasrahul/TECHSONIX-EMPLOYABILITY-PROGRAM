# This script checks if a given year (input by user) is a leap year.

year = int(input("Enter a year: "))

# Leap year logic:
# Divisible by 4 AND (not divisible by 100 OR divisible by 400)
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
