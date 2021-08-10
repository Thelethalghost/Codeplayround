def solve(rooms, target):
     for i in rooms:
        if i >= target:
                return i 
     return -1

rooms = [15, 10, 30, 50, 25]
target = 20
b = solve(rooms,target)
print(b)