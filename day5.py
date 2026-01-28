#functions
def add():
    a=int(input("enter 1st num"))
    b=int(input("enter the 2nd num"))
    return a+b
print(add())

#with parameters
def addd(a,b):
    return(a+b)
print(addd(3,5))

#default parameters
def sub(a,b=2):
    return a-b
print(sub(5))
print(sub(10,4))

#calculator functions
def cal(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b
    else:
        return "invalid"
a=int(input("enter the value of a"))
b=int(input("enter the value off b"))
op=input("enter the operator")
print(cal(a,b,op))

#password checker
def passwrd(p):
    if len(p) < 8:
        return "weak"
    elif len(p) >= 8 and len(p) <= 12:
        return "medium"
    else:
        return "strong"
p=input("enter your password")
print(passwrd(p))