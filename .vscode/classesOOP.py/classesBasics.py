#OOP= object oriented programming
class classname:
    pass
instance=classname()
class students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
student1=students("larry",17,"11th")
print(student1.name)
print(student1.grade)