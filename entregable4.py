year = input("Write the year to check: ")

def leap_year(year):
    if type(year) != int:
        year = int(input("Not valid, please write a number"))
    else:
        print("Valid")
    
    if (year % 400 == 0) and (year % 100 == 0):
        return 'a leap year'
    elif (year % 4 == 0) and (year % 100 != 0):
        return 'a leap year'
    else:
        return 'not a leap year'

print(f"{year} is", leap_year(year))