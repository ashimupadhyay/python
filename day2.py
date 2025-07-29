#operstors and operands
print(5+5)
#operands -> number -> 5
#operators +
#python 7
#arithmetic
print("add",5+5)
print(5-5)
print(5/6)
print(5*5)
print(5%5)
print(5**5) #power
print(5//5) # gives the same dataype
#wap add sumber by asking input to user
 #f-> string {}
print(f"the sum of 2 number is {5+6}")#operations with in string

#assignment operator
# =,+=.-=/=,//=,**=
a =6
print (a)
a/=10
print (a)
a+=10
print (a)
a-=10
print (a)
a*=10
print (a)
a//=10
print (a)
a%=10
print (a)
a**=10
print (a)
#comparion operatoes ->always in boolen
# == < > >=
print(5==5)#output is True
print(5<5)
print(5>=5)
print(5<=5)
print(5!=5)

#logical operator -> AND OR NOT
# and operation
print(True and True)
print(True and False)
print(False and True)
print(False and False)
#OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# not
print(not True)# OUTPUT FALSE
print(not False)# OUTPUT TRUE
print("\n")
#identifier operator -> is . boolean
a=20
b=20
c="20"
print(a is b)
print(a is c)
print(a is not  c)
#memebership operato -> in ,not in bool
list1 = {1,2,3,4}
print(4 in list1)
print(5 not in list1)

#bitwise operstor -> | ,& , ^
print(5&4)
# -> 0101
# -> 0100
print(5|4)
print(5&4)
print(5^4)

#termoary operator
age=20
print("above 18 "if age>18 else "below 18")
 #wap to print the number is odd or even asking use input
num1=int(input("enter  value : "))
print("is even  "if num1%2==0 else "odd ")
age1=int(input("enter  age : "))
print("can drive "if age1>18 else "cannot drive")

#condition in python
#if ,else , elif->else ir , match->switch
if(num1 %2 !=0):
    print("is odd")
elif(num1 == 0):
    print("the value is 0")
else:
    print("even")
    
#wap to print if the given value is fizz ,buzz or fizzbuzz conditions are
#fizz-> div by 3
#buzz->by7
#fizzbuzz-> both 3 and 7
value=10
if (value%3==0):
   print("divisnle by 3")
elif(value%7==0):
    print("is divisble by 7")
elif(value==0):
    print("the value is zero")
elif(value%7==0 and value %3==0):
    print("fizzbuzz")
else:
   print("the number is not didvible by none")


#match->switch
day= "tuesday"
match(day):
    case"sunday":
        print("its sunday")
    case"monday":
        print("its monday")    
    case"tuesday":
        print("its tuesday")
    case _:#works as default
        print("non of the above")