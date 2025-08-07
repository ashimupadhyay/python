
""" '#strinbg manipulation
name = "hari krishna"
# \n,\\
print("hari\nkrishna")
print("shot\thai")
print(name)
print("hi's its me")
#string slicing
print(name[0])
print(name[0:4])
print(name[-1:-6:-1])
print(name[::-1])
#string methods
#.upper(),.lower(),.titlt(),.capatilize(),.strip(),.replace(),.find(),.count(),
one ="two"
two ="  three"
three ="FOUR"
print(one.upper())
print(three.lower())
print(one.title())
print(one.capitalize())
print(two.strip())#removes space
print(two.split())
print(one.replace("two","ashim"))
print(two.find("ee"))
print(one.count("t"))
print(one.isupper())#false
print(one.islower())#true
print(one.istitle())#true
print(two.isalpha())#conains space or not
print(two.isdigit())#contains number onlt
print(two.isalnum())#contains num letter and space
 #wap to chek the num is palindrom or not
x=str(input("enter a string " ))
y=x[::-1]
if(x==y):
    print("paindrome")
else:
    print("sorry wrng")

#list in python
list1 =[1,2,3,4,5]#be careful its an array
#index and length
print(list1)
#methods
list1.clear()#clears list
print(list1.index(5))
list1.append(6)#adds to lAST VALUW
print(list1)
list1.insert(0,7)#adds valuw in the index
print(list1)
list1.pop()#removes last index
print(list1)
list1.remove(3)
print(list1)
list1.reverse()
print(list1)
list1.sort()#ascending
print(list1)
list1.sort(reverse=True)#decending
print(list1)
#tuple in python
tup1 = (1,2,23,23,5)
list2 = [163,232,1]
print(tup1)
list2[1]=10
print(list2)
print(tup1.count[1])#counts the occurance
print(tup1.index[3])#displays value at 3  index


#wap to add item in tup by converting tup in list use appends to add the item in the provided 
#
tup2 = (1,2,3,4,5)#tup ko datatype ani value in tup
list3=list(tup2)
print(list3)
list3.append(7)

tup2=tuple(list3)
print(tup2)
print(type(tup2))

#for loop in python
for i in tup2:
    print (i)
for i in list3:
    print (i)

#set->collection unique items
set1={1,2,3,4,5,6,7,8}
set2={76,4,2,5,6,3,1,23,27}
print(set1)
#set1[0]=10 cannot be done
set1.add(21)
print(set1)
set1.remove(1)
print(set1)
set1.pop()#removes first item
print(set1)
set3=set1.union(set2)
print(set3)
set4=set1.intersection(set2)
print(set4)
set5=set1.difference(set2)
print(set5)
set5.clear()
print(set5)
for i in set1:
    print(set1)"""
#wap to print the union items in thtr list
list2=[1,2,3,4,5,67,6,54,3,21,5]
set0=set(list2)
print(set0)
