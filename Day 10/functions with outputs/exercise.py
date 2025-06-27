def is_leap_year(year):
    isLeap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                isLeap = True
            else:
                isLeap = False
        else:
            isLeap = True
    else:
        isLeap = False
    return isLeap


    
yearInp = int(input("Year: "))

print(f"{is_leap_year(yearInp)}")