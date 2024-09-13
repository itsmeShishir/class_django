#file handling

#open
#read
#write
#append
#close
#readline
#readlines
a = open("04read.txt", mode="r")
print(a.read())
a.close()
b = open("04read.txt", mode="r")
print(b.read())
a.close()

with open("04write.txt", mode = "w") as file:
    file.write("hello my name is shishir Bhandari\n")
    file.write("hello my name is shishir\n")
    file.write("hello my name is shishir\n")
    file.write("hello my name is shishir\n")

with open("04write.txt", mode = "r") as file:
    c = file.read()
    print(file.read())


    