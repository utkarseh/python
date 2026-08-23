students = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
#print(students["Charlie"])
students["Charlie"] = 999
print(students["Charlie"])
del students["Charlie"]
print(students)
clears = students.clear()
print(clears)
del students
#print(students)
#.clear fxn is used to clear the dictionary and del fxn is used to delete the dictionary
studentst = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
length = len(studentst)
print(length)
KEYS = studentst.keys()
print(KEYS)
VALUES = studentst.values()
print(VALUES)
#.keys fxn is used to get the keys of the dictionary and .values fxn is used to get the values of the dictionary
studentst2 = {"Eve": 88, "Frank": 95, "Grace": 82, "Henry": 91}
studentst.update(studentst2)
print(studentst)
#.update fxn is used to update the dictionary with another dictionary
