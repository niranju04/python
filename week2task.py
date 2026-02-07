
from abc import ABC, abstractmethod
# Task 1
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} logged in successfully")


# Task 2: Patient Class (Encapsulation)
class Patient(User):
    def __init__(self, name, email, health_id):
        super().__init__(name, email)
        self.__health_id = health_id 

    # Getter
    def get_health_id(self):
        return self.__health_id

    # Setter 
    def set_health_id(self, new_id):
        if len(new_id) >= 5:
            self.__health_id = new_id
            print("Health ID updated successfully")
        else:
            print("Invalid Health ID! Must be at least 5 characters")

# Task 2: Doctor Class + __str__

class Doctor(User):
    def __init__(self, name, email, specialization):
        super().__init__(name, email)
        self.specialization = specialization

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

# Task 3: Abstraction

class Consult(ABC):

    @abstractmethod
    def prescribe(self):
        pass

# Polymorphism 
class GeneralCheckup(Consult):
    def prescribe(self):
        print("General Checkup: Prescribed vitamins and basic tests")


class SpecialistSurgery(Consult):
    def prescribe(self):
        print("Specialist Surgery: Surgery scheduled")

# Task 4: Main 
if __name__ == "__main__":
    doctor = Doctor("kavya", "kavya@hospital.com", "Cardiologist")
    patient = Patient("vaishu", "vaishu@gmail.com", "vai12345")
    print(doctor)
    doctor.login()
    patient.login()
    print("Patient Health ID:", patient.get_health_id())
    patient.set_health_id("USER3234")
    consultations = [
        GeneralCheckup(),
        SpecialistSurgery()
    ]

    print("consultation Prescriptions")
    for consult in consultations:
        consult.prescribe()
