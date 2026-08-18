sen = "Hello %s,you're invited to my birthdayparty"
print(sen % "AKANKSHA AMAN SANU AATIKSH GAURAV GHANCHEKKER PRIYANK ")
print(sen % "AKANKSHA")
print(sen % "AKANKSHA","AMAN","SANU","AATIKSH","GAURAV","GHANCHEKKER","PRIYANK")
arr = ["AKANKSHA","AMAN","SANU","AATIKSH","GAURAV","GHANCHEKKER","PRIYANK"]
for i in arr:
 print(sen%i)
sen = "Hello %s %s,you're invited to my birthdayparty"
print(sen%("AKANKSHA"," MISHRA"))
sen = "I am %s and %d yrs old"
print(sen%("Utkarsh", 18))