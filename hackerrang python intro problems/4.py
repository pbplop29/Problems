def leap_year(year):
    leap = False
    if(year % 400 == 0 and year % 4 == 0):
        leap = True
    elif(year % 4 == 0 and year % 100):
        leap = True
    return leap


year = int(input())
# Check wheter a given year is leap year or not
# conditions :
# leap if div by 4, but not if by 100 but yes if by 400
