# To receive year that the user wants to check

year = int(input("Enter the year you want to check: "))

# to check if the year is leap year or not

if year %4 == 0:
    if year %100 != 0:
        print ("Leap year")
    elif year %100 == 0 and year %400 == 0:
        print ("Leap year")
else:
    print ("Not Leap Year")