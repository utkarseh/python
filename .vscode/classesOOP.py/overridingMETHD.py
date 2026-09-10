class parent:
    def func(self):
           print("This a parent function")
class child(parent):
    def func(self):
           print("This a child function")
c=child()
c.func()