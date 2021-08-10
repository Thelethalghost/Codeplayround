

def simple_intrest(p,r,t):
    print(f"Principle is {p}")
    print(f"Rate is {r}")
    print(f"Time is {t}")
    Simple = (p*r*t)/100
    print(Simple)

a = int(input("Enter the Principle:\n"))
b = float(input("Enter the rate(Dont input symbol):\n"))
c = int(input("Enter the Time:\n"))
# For Default values
simple_intrest(a,10,2)
# For user defined
simple_intrest(a,b,c)
