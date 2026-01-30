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

 