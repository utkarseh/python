import random
a=random.randint(0,100)
while True:
    b=int(input("guess a number between 1 and 100: "))
    if b>a:
        print("try lower number")
    elif b<a:
        print("try higher number")
    else :
        print("YOU WONN BITCHH")
        break

