#caulator app using fun -> add,sub,dev, mul ,**,//,% and ask the 3 input for the user 2 will be number and 1 will
#be option and use the  recursion to call the functon again and again untill the user tghe exit
x= False
def add(a,b):
        print("the sum is " , a+b)
        
def diff(a,b):
    print("the difference is " , a-b)    
    
def mul(a,b):
        print("the multiplication is " , a*b)
        
def powe(a,b):
    print("the power of the number is " , a**b)
       
def div(a,b):
        print("the divides is " , a//b)
        
def remainder(a,b):
    print("the remainder is " , a%b)    
def calculator():  
    print("Calculator")
    print("1 . addition")
    print("2 . subtraction")
    print("3 . multipilication")
    print("4 . diviion")
    print("5 . power")
    print("6 . //")
    print("7 . exit ")
    print("CHOOSE THE OPTION")
    num44=int(input("enter your option : "))
    a=int(input("enter 1st number : "))
    b=int(input("enter 2nd number : "))
   
    match num44:
      case 1 :
         add(a,b)
         rec()
      case 2 :
        diff(a,b)
        rec()
      case 3 :
         mul(a,b)
         rec()
      case 4 :
        remainder(a,b)
        rec()
      case 5 :
         powe(a,b)
         rec()
      case 6 :
        div(a,b)
        rec()
      case 7 :
         x=False
         print("Exiting the calculator.")
         return  # Exit the recursion
        
      case _ :
        print("out of range")
        return
        
def rec():
    calculator()
rec()       
      


        
        
 