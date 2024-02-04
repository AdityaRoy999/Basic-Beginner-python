def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 ==0 and year % 400 == 0:
            print("leap year")
    else:
        print("NOT a leap year")
    
    return leap

year = int(input())
print(is_leap(year))