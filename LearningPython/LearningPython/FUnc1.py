#def add (*p):
#    print(p)

#add(5,4,3,1,2)
def add (*p):
    total = 0 
    for i in p:
        total+=i
    print(total)

add(56,4,3,1,5)
