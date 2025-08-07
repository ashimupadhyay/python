"""#  file handling -> read write upfate delete read 
#mode r,w,a,r+ ......
#delete ->os -> import modeule -> dlete
# r-> read ->exisitng file

fs = open("hi.txt",mode="r")
#read propertires read() readline() readlines()
print(fs.read())
print(fs.readline())
print(fs.readlines())
fs.close()
#write w-> existing file not neded
fs = open("hi.txt",mode="w")
fs.write("hello world")
fs.close()

fs = open("hi.txt",mode="w+")
fs.write("hello world")
fs.seek(0) #index goes to 0
one =fs.read()
print(one)
fs.close()
#a+ 0->
fs3 = open("hi.txt",mode="a+")
fs3.write(" \n hello world")
fs3.seek(0) #index goes to 0
one =fs3.read()
print(one)
fs3.close()

#delete -> remove => import os 
import os
os.remove("bye.txt") #error auca if no file
"""


# wap to print the table of 7 using file handling

fs=open("abcd.txt", mode="w")
for i in range(11):
    fs.write(f"7*{i}={7*i}\n")

fs.close()

# wap to print the table for 0 to 10 in seprate file using file handling
for i in range(11):
    fs = open( f"abc{i}.txt",mode="w")
    for j in range(11):
        fs.write(f"{i}*{j}={i*j}\n")
fs.close()