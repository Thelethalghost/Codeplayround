# wap a programme to find the greater of 3 integers
def maximum(a, b, c):
  
    if (a >= b) and (a >= c):
        largest = a
  
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
          
    return largest

a = int(input("Enter the first number:\n"))
b = int(input("Enter the second number:\n"))
c = int(input("Enter the third number:\n"))

print(maximum(a,b,c))
