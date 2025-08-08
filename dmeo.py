class student:
    def __init__(self,name,age,roll, marks):
        self.name= name
        self.age= age
        self.roll= roll
        self.marks= marks
    def __str__(self):
        return f"name : {self.name},roll no:{self.roll} , age : {self.age}, ,marks : {self.marks}"
    def rint(self):
        print(self.name,self.age,self.roll,self.marks)
    
obj=student("ashim",20,312,45)
print(obj)