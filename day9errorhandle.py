#error handling and exception handling 
# try except else finally
print("hi")
try:
    print(10/0)
#except ZeroDivisionError:
 #   print("cannot devide by zero")
 #or
except Exception as e:
    print(e)
#else :
 #   print("the code runs after  without exception") #if uder input is taken and just to check
finally:
    print("good to go after wither finding or not finding exception")
    
print("hello")

#wap eception of odd or not with user inpt
def numcheck():

    try: 
         num= int(input("enter a number "))
        
         if num%2==1:
             print("odd")
    
    except Exception as e:
        print (e)
        
    
    finally:
        print("number checked")
        
            
        
numcheck()
