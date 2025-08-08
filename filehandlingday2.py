"""#with -> open and close
with open("nake.txt","w+") as fs:#w+ reads and write -- alternate way to initilize file

    for i in range (1,11):
        fs.write(f"7*{i}={7*i}\n")
    fs.seek(0)
    print(fs.read())
fs.close()

# wap to print the table for 0 to 10 in seprate file using file handling
for i in range(11):
    fs = open( f"abc{i}.txt",mode="w")
    for j in range(11):
        fs.write(f"{i}*{j}={i*j}\n")
fs.close()
for i in range (11):
    fs = open( f"abc{i}.txt",mode="r")
    fs.seek(0) 
    print(fs.read())
fs.close()"""

for i in range(11):
    fs = open( f"abc{i}.txt",mode="w+")
    for j in range(11):
        fs.write(f"{i}*{j}={i*j}\n")
        
    fs.seek(0)
    print(fs.read())
fs.close()


