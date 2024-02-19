class Person:
    def __init__(self,firstname,age,gender):
        self.firstname=firstname
        self.age= age
        self.gender=gender
    def details(self):
        print(self.firstname, "is studying")

teacher = Person("Joe",34, "Male")
accountant = Person("Grace",19, "female")
doctor = Person("John",45, "Male")

print(teacher.firstname,teacher.age,teacher.gender)
print(accountant.firstname,accountant.age,accountant.gender)
print(doctor.firstname,doctor.age,doctor.gender)