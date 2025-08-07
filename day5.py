"""#wap to use all paramerts in a single funtion
def name(a=10,b=60):
    print(a+b)
name()
name(100)
name(100,200)

#named parameter manages potition
def fun (name ,age):
    print(f"name is {age} age is {name}")
fun(45,"hari")#namages placement

def abde(a,b,c,*args,**kwargs):
    print(f"a:{a} ,b={b} ,c={c}")
    print("additional",args)
    print("keyword args",kwargs)

abde(10,20,30,40,50,name="ashim",age=25,gender="male")

#anonymus function->we cannot use def ->lamda funtion
x= lambda:  22
print(x())

x= lambda:  "ashim"
print(x())

x= lambda a,c:  a+c
print(x(10,25))

#wap to print the given values is even or odd using lambda

x= lambda:  22
if(x()%2==0):
    print("even")
else:
    print("odd")


#or
#num=int(input("enter value : "))
#a = lambda num: "even" if num % 2==0 else "odd"
#print(f"the value {num} is {a(num)}")

#recusion -> a functon calling itself"""

def rec(n):#set condition
    if n==0:
        return 0
    else:
        return n +rec(n-1)

print(rec(67))

