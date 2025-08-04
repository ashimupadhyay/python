#list comprehension in py ->ouytput is a list
#like ternary operator simliar to one line code 
list1= [1,2,3,4,5]
for i in list1:
    print(i*2)
#expressiom-> expressiom for item in iterable
#expressiom-> expressiom for item in iterable if condition 
output1 = [i*2 for i in list1 if i%2==0]
print(output1)
#wap to print the square of even numbr from 1 to 10
output3 = [i*2 for i in range(101) if i%2==0]
print(output3)
#wap  multi table of 7
output2 = [(i*7) for i in range(1,11)]
print(output2)

