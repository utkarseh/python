class students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displaystudents(self):
        return("Student name is "+self.name+" and age is "+str(self.age))
stu=students("lamine",18)
print(stu.displaystudents())