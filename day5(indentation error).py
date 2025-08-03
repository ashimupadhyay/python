#FUNCTION ->A block of code runs when it is called
def hello():
    print("hello g")
    hello()
    hello()
    hello()
#funtions->paramtetres, arguments
    name = "raja"
    def printname(name):
        print(f"name is {name}")
        printname(shyam)
        printname(bam)
        printname(ram)
        
    #return statement
    def add(a,b):
        return a+b
    print(add(2,4))
    #no parameter but retuen statement
    def getinfo():
        return f"hello world" #f-string without plccae holdre
    print(getinfo())
    #funtion types return ,no return
    # no parametr noreturn
    #parameter no return
    #no para return
    #parameter return
    
    #paramater types in python
    #default parameter
    def defaultpara(a=0,b=21):
        print(a+b)
    defaultpara()
    defaultpara(10)
    defaultpara(20,10)
     
     #wap rto print sum ,diff
    def sum(a=234,b=98):
        print(a+b)
        print(a-b)
      
    #wap to print power
    def power(a=76,b=67):
        print(a**b)
        power()
    #named parameytr
    def normalfunc(name,age):
        print(f"name is {name} and age is {age}")
        normalfunc( age =25 ,name = "ashim")
    #postitinal parameytr
    def normalfunc(name,age):
     print(f"name is {name} and age is {age}")
    #*args parameter
    def abc(a,b,*args):
        print(a,b)
        for i in args:
            print (i)
            abc(10,1090,202)
    #**kwargs paramater
    def xyz(*args,**kwargs):
        print(kwargs)
        print(args)
    xyz("kathmandu" "butwal" , "palpa",name ="ashim" , age =20) 
    