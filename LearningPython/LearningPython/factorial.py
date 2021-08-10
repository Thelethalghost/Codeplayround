# WAP a python function to calculate the factorial of a number(a non negative interger).

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

fac = int(input("Enter the number you want the factorial of :\n"))

print(factorial(fac))