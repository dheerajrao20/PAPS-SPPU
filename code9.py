#ASSIGNMENT 06
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
def power(a, b):
    return a**b
def fac(a):
    c=1
    for i in range(1, a+1):
        c = c*i
    return c
user = 1
a = int(input("Enter the 1st number\n"))
b = int(input("Enter the 2nd number\n"))
while(user != 0):
    print(
        "What you want to do?\nType 1 for add \nType 2 for subtration\nType 3 for Multiplication\nType 4 for Division\nType 5 for Exponent\nType 6 for Factorial")
    ch = int(input())
    if (ch == 1):
        print(add(a, b))
    elif (ch == 2):
        print(sub(a, b))
    elif (ch == 3):
        print(mul(a, b))
    elif (ch == 4):
        print(div(a, b))
    elif (ch == 5):
        print(power(a, b))
    else:
        print("factorial of 1st number is :", fac(a))
    user = int(input("press any key to continue and 0 to exit"))

