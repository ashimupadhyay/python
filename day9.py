"""#abc-> abstract base class
from abc import ABC , abstractmethod
class teahouse(ABC):
    def processcompleted(self):
        self.order()
        self.addingmatrial
        self.servein()
    @abstractmethod
    def order(self):
        pass
    
    @abstractmethod
    def addingmatrial(self):
        pass
    
    @abstractmethod
    def servein(self):
        pass

class milk(teahouse):
    def order(self):
        print("ordering milk tea")
    
    def addingmatrial(self):
        print("adding milk ")
    
    def servein(self):
        print(" milk in cup ")
        
    

class black(teahouse):
    def order(self):
        print("ordering black tea")
    
    def addingmatrial(self):
        print("adding masala ")
    
    def servein(self):
        print(" black in cup ")

user1 =milk()
user1.processcompleted()
user2 = black()
user2.processcompleted()


"""


#polymorphism -> 
class animal:
    def eat(self):
        print("eating grass")
        
class lion():
     def eat(self):
        print("eating meat")
        
class dog():
    def eat(self):
        print("eating done")
        
class human():
    def eat(self):
        print("eating rice")

obj1 = animal()
obj2 = lion()
obj3 = dog()
obj4 = human()

for i in [obj1,obj2,obj3,obj4]:
    i.eat()