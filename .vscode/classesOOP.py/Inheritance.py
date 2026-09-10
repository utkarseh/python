class parent:
    counter=10
    def __init__(self):
            print("class initialized.")
    def parentFunc(self):
          print("parentFunc being called")
    def setCounter(self,num):
          parent.counter=num
    def showCounter(self):
          print(str(parent.counter))
class child:
    def __init__(self):
          print("Child class being initialized")
    def childFunc(self):
          print("childFunc being called")
c=child()
c.childFunc()
c=parent()
c.parentFunc()
c.showCounter()
c.setCounter(20)
c.showCounter()