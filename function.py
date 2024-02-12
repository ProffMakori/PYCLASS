# Inbuilt functions
number = max(89, 70, 23, 45, 123)
print(number)

x = min(78, 46, 65, 42, 2)
print(x)

z = pow(2, 3)
print(z)


# user-defined function
def name():
    print("James")


name()# Calling a function

def student():
    name = "Vincent"
    age = 18
    course = "MIT"
    print(name, age, course)

student()

# Parameters/variables and arguments/values
def student(name, age, course):
    print(name, age, course)

student("Vincent", 18, "MIT")
student("Grace", 17, "cybersecurity")
student("Jane", 16, "Datascience")
student("John", 21, "software engineering")

# Create a user-defined function
# called employees. It should display
# details of five employees.Parameters are
# fullname, age, gender, position, salary

def employees(fullname, age, gender, position, salary):
    print(fullname, age, gender, position)

employees("James Makori", 19, "male", "CEO", "Ksh 800000")
employees("Grace Mweu", 18, "Female", "Marketing & sales", "Ksh 50000")
employees("Brian Mwetaita", 20, "male", "Production manager", "Ksh 100000")
employees("Samwel Fatali", 21, "male", "IT Specialist", "Ksh 80000")
employees("Prudence Mwikali", 19, "female", "Accountant", "Ksh 250000")
