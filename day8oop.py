def exponents(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        return res**2
    return wrapper
    
@exponents
def calculate(A,b):
    return(A+b)
print(calculate(10,20))


#property->use for the last name and first name ==full naem
class person:
    def __init__(self,firstname,lastname):
        self.firstname =firstname
        self.lastname =lastname
        
    @property
    def fullname(self):
        return  f"{self.firstname} {self.lastname}"
    
ob1 =person("ashim", "upadhyay")
print(ob1.firstname)
print(ob1.lastname)
print(ob1.fullname)



#4 pilars pf oop -> encapsulation inheritsnce abstraction polymorphism
class parent:
    
    def __init__(self,lastname):
        self.lastname = lastname
        
    def hello(A):
        print("yo",A.lastname)
        
class child(parent):
      
    def __init__(self,firstname,lastname):
       
        self.firstname = firstname
        super().__init__(lastname)#calls parent class construc
        
    def hi(self):
        print("yo ko chora",self.firstname)   
        
obj2 = child("ashim ","upadhyay")
obj2.hello()
obj2.hi()


# wap to create a parent class named Classes with attribute like class_name section and
# have to inherit it to child class named Students with attributes like name, age, and methods like
# study, attend_class, and display_info using constructor and use super() to access parent class attributes and methods




class Bank:
    def __init__(self,name,balance):
        self._name=name
        self.__balance=balance
        
    @property
    def getbalance(self):
        return self.__balance
    
    @getbalance.setter
    def setbalance(self,balance):
        self.__balance=balance
        
    def __calculateminbalance(self):
        if self. __balance > 500:
            print("hello")
            
    def calling(self):
        self.__calculateminbalance()
        
obj1= Bank("ashim",89765)
print(obj1._name)    
print(obj1.getbalance)
obj1.setbalance=3000
print(obj1.getbalance)
obj1.calling()



# abstraction in python -> hidding complex logic from user
from abc import ABC, abstractmethod
class Coffee(ABC):
    def makeCoffee(self):
        self.gason()
        self.addCoffee()
        self.addMaterials()
        self.servein()

    @abstractmethod
    def gason(self):
        pass
    @abstractmethod
    def addCoffee(self):
        pass
    @abstractmethod
    def addMaterials(self):
        pass
    @abstractmethod
    def servein(self):
        pass

class Espresso(Coffee):
    def gason(self):
        print("coffee machine on")
    def addCoffee(self):
        print("addCoffee beans and exxtract it")
    def addMaterials(self):
        print("water, sugar and milk")
    def servein(self):
        print("serve in cup")
    
class Cappuccino(Coffee):
    def gason(self):
        print("coffee machine on")
    def addCoffee(self):
        print("extracted coffee powder")
    def addMaterials(self):
        print("water, sugar and milk")
    def servein(self):
        print("serve in cup")

exp = Espresso()
exp.makeCoffee()

cap = Cappuccino()
cap.makeCoffee()