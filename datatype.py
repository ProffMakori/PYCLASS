# Data Type
number = 45  # int
num = 56.78  # float
greeting = "Hello there "  # str
isPythonInteresting = True  # bool

# variable storing multiple values
languages = ["python", "php", "java"]  # List
fruits = ("apple", "banana", "pineapple")  # Tupple
countries = {"Kenya", "China", "USA"}  # Set

# Dictionary
details = {
    "firstname": "Grace",
    "age": "17",
    "course": "MIT",
    "nationality": "kayole",

}

print(number)
print(countries)
print(isPythonInteresting)
print(details)
print(details["course"])
print(greeting)

print(type(details))
print(type(countries))

# Type casting - converting one data type to another
print(float(number))
print(int(num))