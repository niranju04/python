#oops

class car:
    def __init__(self): #constructor
        self.no_of_wheels = 4
        self.speed=0.0
        self.color=" "
    def moveforward(self,aribags):
            print("car is moving")
    def reverse(self):
                print("car is reverse")
car1=car()
car1.no_of_wheels=6
car1.color="black"
car1.moveforward(5)
print(car1.no_of_wheels)
print(car1.color)
print(car1.speed)
car1.reverse()

#encapsulation
class cmpy:
       def __init__(self):
        self.__cmpyname="google"
        print(self.__cmpyname) 
c1=cmpy()

#inheritance
#single level 
class dad:
      def phone(self):
            print("dads phone")
class son(dad):
      def laptop(self):
            print("sons laptop")
ram=son()
ram.phone()
ram.laptop()

#multiple
class dad1:
      def money(self):
            print("dads money")
class mom():
      def sweet(self):
            print("moms sweer")
class child(dad1,mom):
      def game(self):
            print("childs game")
ch=child()
ch.money()
ch.sweet()
ch.game()


#muliti level
class grandfather:
      def phonee(self):
            print("grandpa phone")
class father(grandfather):
      def amnt(self):
            print("fathers amnt")
class son1(father):
      def bike(self):
            print("sons bike")
ramu=son1()
ramu.phonee()
ramu.amnt()
suresh=father()
suresh.phonee()

#polymorphism
class bird:
      def fly(self):
            print("bird is flying")     
class aeroplane:
      def fly(self):
            print("aeroplane is flying")
def func(obj):
      obj.fly()
b1=bird()
a1=aeroplane()
func(b1)
func(a1)

class human:
    def speak(self):
        print("human is speaking")

class robot:
    def speak(self):
        print("robot is speaking")

def action(obj):
    obj.speak()

h = human()
r = robot()

action(h)
action(r)
#runtime polymorphism
class animal:
      def sound(self):
            print("animal make sound")
class dog(animal):
      def sound(self):
            print("dog barks")
obj=dog()
obj.sound()

#abstract class
from abc import ABC, abstractmethod

class payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class gpay(payment):
    def pay(self):
        print("payment done using GPay")

class phonepe(payment):
    def pay(self):
        print("payment done using PhonePe")

def make_payment(p):
    p.pay()

g = gpay()
p = phonepe()

make_payment(g)
make_payment(p)