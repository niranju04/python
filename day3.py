#loops
#for loop multiplication table
n=int(input("enter a num"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
#while loop
i=0
while i<10:
    print(i)
    i += 1
#jump
#continue
for j in range(1,10):
    if(j==9):
        continue
    print(j)
#break
for k in range(1,10):
 if k==5:
        break
 print(k)
 #number guessing game
 import random
 number=random.randint(1,50)
 guess=int(input("guess number b/w 1-50"))
 while(guess!= number):
     if(guess<number):
         print("you need to guess high")
         guess=int(input("guess number b/w 1-50"))
     else:
         print("you need to guess low")
         guess=int(input("guess number b/w 1-50"))
print("your guess in correct")
 
 