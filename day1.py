
#day 1--> syntax , operatoes, 
print( "namaste ashim dai")
a=10
print (a)
a= "ashim"
print(a)
"""
if True:
    pass #indentation works like parameters={}
    """
#reserve keywords-> if ,try ,except ,def, finally ,class, as, elif
# use camelcase-> camelCase
#comments -> # , """ 
#datatypes in python
#string collection of chat  in "", """", """"""
a= "shayam"
print(a)
b = '''
lal again
and again
'''
print(b)
print(type(b))
# +
print(a+b)
name = "ashim"
age ="27"
print("my name is "+name +" my age is " + age)#is int and string is joined it throws exception for use 27 as string 
num1=10
num2 =40
print(type(num1))
print(num1+num2)
#float
num5 =10.3
num6 =10
print(type(num5))
print(num5+num6)
#complex number
j=10
num4 =1+3j
print(type(num4))
print (num4)
#boolean true false
print(type(True))
print(False)
#none
'''noVlaue = None
print(noValue)
print(type(noValue))'''
#array
list1 ={ 1,2,3,4,5,True ,5.5 ,"ashim"}
print(list1)
print(list[4])
print(type(list1))
#tuples-> collection of item-> only one time and value cannot be changed
tup1=(1,2,3,4,5,2.3,23.4,"ashim")
print(tup1)
print(type(tup1))
#set-> ollection of unique value
set1={1,2,3,4,5,6}
print(set1)
#dictionary ->collection of key and values pairs
dict1 = {
    "name":"goat",
    "age":20,
    "gender":"male"
}
print(dict1)
print(dict1.values())
print(dict1.keys())
print(dict1["name"])
#type conversion and ask input from user
names = input ("enter your name")
print(names)
print(type(name))
#string->str()
#int->int()
#float->float()
#boolean->bool()
#dict->dict()
#set->set()
num44=int(input("enter 1st value : "))
num55=int(input("enter 2nd value : ")) #to concatinate remove int
print(num44+num55)


#to take input  command in termina; -> python filename.py