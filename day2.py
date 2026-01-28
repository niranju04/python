#conditions and operators
#age eligibility
age=int(input("enter your age"))
if(age>=18):
    print("adult")
else:
    print("youth")
#even odd
a=int(input("enter a valure"))
if(a%2==0):
    print("even num")
else:
    print("odd num")
#large among 3 values
b=int(input("enter the 1st num"))
c=int(input("enter the 2nd num"))
d=int(input("enter the 3rd num"))
if(b>c and b>d):
    print("1 is large")
elif(c>d and c>b):
    print("2 is large")
else:
    print("3 is large")
#grade checker
grade=int(input("enter your mark"))
if(grade>=90):
    print("A grade")
elif(grade>=80):
    print("B grade")
elif(grade>=70):
    print("C grade")
elif(grade>=60):
    print("fail")   
else:
    print("invalid")
