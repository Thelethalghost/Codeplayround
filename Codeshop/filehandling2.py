# write a programme to display the size of a file in bytes
import os 

f = open("play.txt")

# positioning the cursor at the end 
f.seek(0,os.SEEK_END)

print("Size of file is :", f.tell(), "bytes")

print(os.path.getsize("play.txt"))