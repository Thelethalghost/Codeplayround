# WaP a python programme using function to calculate leap year

def leap(year):

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

year  = int(input("Enter he number you want to check for leap year:\n"))
if (leap(year)):
    print("leap year")
else:
    print("not a leap year")