
#task1
class User:
    def __init__(self,name,email):
        self.name = name 
        self.email = email
    def login(self):
        print(f"{self.name} logged in successful")
    
#task2
class Patient(User):
    def __init__(self, name, email, health_id):
        super().__init__(name, email)
        self.__health_id = health_id
    def get_health_id(self):
        return self.__health_id
    def set_health_id(self, new_id):
        if len(new_id) >= 6:
            self.__health_id = new_id
            print("Health ID updated")
        else:
            print("Invalid Health ID")

class Doctor(User):
    def __init__(self, name, email, specialist):
        super().__init__(name, email)
        self.specialist = specialist
    def __str__(self):
        return (f"Dr. {self.name} - {self.specialist}")
#task 3
from abc import ABC, abstractmethod
class Consultation(ABC):
    @abstractmethod
    def prescribe(self):
        pass
class GeneralCheckup(Consultation):
    def prescribe(self):
        print("General checkup prescribed: vitamins")

class SpecialistSurgery(Consultation):
    def prescribe(self):
        print("Surgery scheduled")

#task 4
if __name__ == "__main__":
    print("             doctor details          ")
    dname = input("enter the doctor name")
    dmail = input("enter the doctor email")
    dspec = input("enter thew doctor specialization")
    doctor = Doctor(dname, dmail, dspec)
    print("             patient details          ")
    pname = input("enter the patient name")
    pmail = input("enter the patient email")
    pid = input("enter the patient health id")
    patient = Patient(pname, pmail, pid)
    print(doctor)
    doctor.login()
    patient.login()
    update = input("update health id? (yes/no)")
    if update == "yes":
        newid = input("enter the new health id ")
        patient.set_health_id(newid)
    else:
        print("thankyou")

    consultations = [GeneralCheckup(), SpecialistSurgery()]
    for i in consultations:
            i.prescribe()
