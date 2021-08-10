# write a programme to diplay the number of lines in the file 
with open("play.txt")  as file:
    print(len(file.readlines()))


counter = 0

with open("play.txt") as text:
    co = text.read()
    collist = co.split("\n")
    for i in collist:
        if i :
            counter +=1

print(f"The number of the lines in the file which are written is:\n{counter}")