import time
print(time.time())
def numbers(max):
    time1=time.time()
    for i in range(0,max):
        print(i)
        time2=time.time()
    print(str(time2-time1))
print(numbers(1000))

#2nd function
print(time.asctime())
tup=(2026,11,18,10,20,30,0,0,0)
print(time.asctime(tup))

#3rd function
print(time.localtime())
t=time.localtime()
year=t[0]
day=t[2]
month=t[1]
print(year)
print(day)
print(month)
print(str(day)+"/"+str(month)+"/"+str(year))
#4th function
for i in range(0,5):
    print(i)
    time.sleep(1)
