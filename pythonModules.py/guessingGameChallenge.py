#solve for reverse like computer have to guess
import random
low=0
high=100

while True:
    a=random.randint(low,high)
    print("my guess is: ",a)
    b=input()
    if b=="lower":
        high=a-1
    elif b=="higher":
        low=a+1
    elif b=="you got it":
        print("Less gooo mann")
        break