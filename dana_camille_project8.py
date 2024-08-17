# Name:Camille Dana
# ID:003277157

# Calculate whether a year is a leap year or not.

# Number of days per month.

year = int(input('Enter a year: '))
month = int(input('Enter the month (1-12): '))

if(year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print('{0} is a leap year' .format(year))
else:
    print('{0} is not a leap year' .format(year))
