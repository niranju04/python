#expection handling
try:
    a=int(input("enter a num"))
    b=int(input("enter b num"))
    c=a/b
    print("the division is",c)
except ZeroDivisionError as e:
    print("cant divide by zero",e)

