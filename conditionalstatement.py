temperature = 13

if temperature > 25:
    print("It is hot")
else:
    print("It is cold")

# A program that returns the lagest number among the three numbers
num1 = 45
num2 = 56
num3 = 21
if num1 > num2 and num1 > 3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 56
if number % 2 ==0:
    print(number, "is even")
else:
    print(number,"is odd")

# A program that checks whether a number is prime or not
num = int(input("enter a number:"))
if num > 1:
    for i in range(2 , num):
        if num % i == 0:
            print("is not a prime number")
            break
    else : print( "its  a prime number")
else: print("is not a prime number")

