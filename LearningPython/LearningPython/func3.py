def num_digit(num):
    num_strings = str(num)
    numdigit = len(num_strings)
    return numdigit

a = int(input("Enter the number you want the digits of:\n"))
b = num_digit(a)
print(b)