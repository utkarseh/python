class students:
    def __init__(self,name,age):
        self.name= name
        self.age=age
stu1=students("thor",366)
stu2=students("tony",43)
print(hasattr(stu1,"age"))
print(hasattr(stu2,"grade"))
setattr(stu1,'grade',"11th")

print(getattr(stu1,"age"))
delattr(stu1,"grade")
print(hasattr(stu1,"grade"))