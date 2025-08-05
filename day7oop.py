#oop
#programming paradigm based on the concept of program
#class obj decorators construcut magic/dunder
#4pillars -> inheritance , enchapuslation polymarphism abstratcion
#if we use decorators not need to make object
class AC:
    #ATTRIVBUTE METHODS CONSTRUCTORS
    name ="ashim"
    age =32
    gender = "male"
    #this == self in python refer to a class
    def printdetails(self):
        print(f"name :{self.name},age :{self.age},gender  :{self.gender}")
        
    def add(self ,a,b):
        return a +b

one = AC()
print(one.name)
one.name= "hari" #updates
print(one.age)
print(one.gender)
print(one.name)

#calling methods
one.printdetails()
print(one.add(20,40)) 

#WAP to certa class with name model year and methods start stop and display
class car:
     #name = " BMW"
     #model = "m3"
     #year =  2015
     
     #constructor->magic method, 1 constructor per class
     def  __init__(self, name, model, year):
         print("object created")
         self.name =name
         self.model = model
         self.year =year 
    
     def start(self): #any variable can used in place of self
         print("on")
        
    
     def stop(self):
          print("off")
          
     def info(self):
         print(f"name : {self.name},model : {self.model},year : {self.year}")
     
     
       
car1 = car("nissan","gtr","2014")
car1.info()
car1.start()
car1.stop()

car2=car("nisssan","magnite","2022")
car2.info()
car2.start()
car2.stop()

#wap to create class student with details
class student:
     #name = " BMW"
     #model = "m3"
     #year =  2015
     
     #constructor->magic method, 1 constructor per class
     def  __init__(self, name, age, classroom):
         print("object created")
         self.name =name
         self.age = age
         self.classroom =classroom 
    
     def studying(self): #any variable can used in place of self
         print(f"{self.name} is in the classs")
        
    
     def attendance(self):
          print(f"{self.name}'s attencance is regular")
          
     def info(self):
         print(f"name : {self.name } , age : {self.age} , classroom : {self.classroom}")
     
     
       
st1 = student("anish","32","bit 101")
st1.info()
st1.studying()
st1.attendance()



#decorators-> @classmethod @staticmethod @abstract method @property

class one:
    two ="this is a class variable"
    
    #normal metod
    def ones(self):
        print(f"this is megod one{self.two}")
        
    #class mehos
    @classmethod
    def twos(a):#a is self
        print(f"this is clas method{a.two}")
        
    @staticmethod
    def three(a,b):
        print(f"this is clas method {a+b}")
    
#to run ones create ong th only  
one.twos()
one.three(10,20)

#wap to create class student and use decorators
class student:
     name = " ashim"
     age = "33"
     classroom =  15
     
     @classmethod
     def studying(cls): #any variable can used in place of self
         print(f"{cls.name} is in the classs")  #cls work as self not tHE SAME 
        
     @staticmethod
     def attendance(name):
          print(f"{name}'s attencance is regular")
          
     @classmethod 
     def info(cls):
         print(f"name : {cls.name} , age : {cls.age} , classroom : {cls.classroom}")
     
     
       
st1 = student()
st1.info()
st1.studying()
st1.attendance("dada's ")

#FUNTION DECORATORS
def addfive(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)#this means the passed value is either keyword ARGUMENTS  or argument       
        return result+5
    return wrapper


@addfive
def addnumber(a):
    return a
print(addnumber(10)) 

#assignment decorator for exponent, power
