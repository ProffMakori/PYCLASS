# Class is a blueprint of an object
#


class Person:
    # Properties/Attributes/Characteristics
    age = 23
    name = "BILL"
    # Method/Function/Behaviour
    def talk(self):
        print("Person is talking")

teacher = Person()
print(teacher.name)
print(teacher.age)

teacher.talk()
