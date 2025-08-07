dic1={
#dict contains keys and values
    "name" : "ashim",
    "age": 89,
    "city " :"kathmandu"
}
print(dic1)
print(dic1["name"])
dic1["name"]="asdafa"#methods
print(dic1.keys())
print(dic1.values())
print(dic1.items())
print(dic1.get("age"))
dic1.pop("age")
print(dic1)
#update
dic1.update({"name":"hary","age ": 34,"city":"japan"})
print(dic1)
#wap to print keys and vaues of dic name : hary
for keys,values in dic1.items():
    print(f"{keys}:{values}")#use of f directly operates within the braces

# loops-> for contonuous exec-for,while,nested
#break ,continue ,pass
#data type ->range(start,stop,step)
#range(0,101,2)
#print(range(0,10,2))->this must be in loop
a,b=0,1
print(a,b)

for i in (range(0,10,2)):#prints 2,4,6,8
    print(i)

#print hello world 100 times
for i in range(0,101):
    print("hello world",i)
    
#while loop
i=0
while(i<101):
    print("yo",i)
    i=i+1
    
#even number 0 = 100
for i in range(0,101,2):
    print("number",i)
#all prime 0-100 
print("1")
for i in range(3,101):
   
    print(f"{(i-1)+(i-2)}")
#multip of 7
"""
for i in range(0,11):
    print(f"value {7*i}")
    for j in range(0,11):
     print(f"{i}*{j}={i*j}")           

"""
#reverse the number
for i in (range(101,0)):
    print(i)

# fibonacci series 0-100
a,b=0,1
print(a)
print(b)
c=a+b
for i in range( 3 ,10):
    print(c)
    a = b
    b = c
    c = a + b
    i=i+1
  
# factorial your choice

'''''fact=1
num=int(input('enter number'))
if num==0:
    print(0)
elif num==1:
    print(1)
else:
    for i in range(1,num+1):
      fact*=i
    print(fact)
#sum  of all 0 to 100
sum=0
for i in range(0,101):
    sum=sum+i
    print(sum)'''''
#divisible by 2,5 ,both from 0 t0 100

for i in range(0,101):
    if(i%3==0 and i%5==0):
        print(i, "is fizzbuzz.")
    elif(i%3==0):
        print(i, "is fizz.")
    elif(i%5==0):
        print(i, "is buzz.")
        
#reverse 
#remainder = n % 10;
 #   reverse = reverse * 10 + remainder;
  #  n /= 10;
        
#pattern
""" 
*
**
***
****
*****
"""
for i in range(0,6):
    for j in range(i):
        print("*")
   

#break statemenrts ->
#break, continue,pass
for i in range(0,10):
    if(i==5):
        continue
    print(i)
    
for i in range(0,10):
    if(i==5):
        break
    print(i)
    
for i in range(0,10):
   pass
print("hello")