# Built-In Functions/Standard Library Functions

y = max(87,90,50,71,64)
print("The maximum value is",y)

x = min(13,20,76,19,17)
print("The minimum value is",x)


#User-defined Functions
def name():
    print("Emmanuel")

name() # Calling a Function

def multiply():
    x = 10
    y = 2
    print(x * y)

multiply()

# Parameter/Variable and Argument/Value
def add(a, b):
    print(a + b)

add(3,4)
add(5,9)

def employee(name, gender, position, salary, age):
    print(name,gender,position,salary,age)

employee("Mark","Male","CEO","560000",50)
employee("John","Male","Marnaging Directer","500000",40)
employee("Mary","Female","HOD","450000",45)

#A program that displays details of five studentsuse a user-defined function with the paramiteran argument
#Fullname,age,course,gender


def students(fullname, age,course,gender):
    print(fullname,age,course,gender)

students("Mangi Tinga",18,"MIT","male")
students("Mjeni Masha",20,"MIT","female")
students("Furaha Karisa",19,"MIT","female")
students("Kalu Samuel",17,"MIT","male")
students("Baraka Safari",18,"MIT","male")