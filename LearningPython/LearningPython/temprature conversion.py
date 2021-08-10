# wap a programme to change celsius into farenheit

def change(temp):
    faren = temp*(9/5)+32
    return faren

temp = float(input("Enter the temrature in *C:\n"))
print(change(temp))