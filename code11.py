#ASSIGNMRNT 15

def length(s):
    print(len(s))

def rev(s):
    print(s[::-1])

def eq(s):
    check = input("Enter string to check equality :\n")
    if (s == check):
        print("Yes")
    else:
        print("No")

def palidrome(s):
    if (s == s[::-1]):
        print("Yes")
    else:
        print("No")

def sub(s):
    substr = input("Enter the a string to check substring:\n")
    ind = s.find(substr)
    if ind != -1:
        print("yes")
    else:
        print("No")

def main():

    s = input("Enter a string:\n")
    flag = 1
    while flag ==1:
        print(
            "press 1 to get length of string\n press 2 to get its reverse string\n press 3 to check palidrome\n press 4 to check a substring\n press 5 to check equality\n")
        n = int(input("Enter a Number:\n"))
        if (n == 1):
            length(s)
        elif (n == 2):
            rev(s)
        elif (n == 3):
            palidrome(s)
        elif (n == 4):
            sub(s)
        elif (n == 5):
            eq(s)
        else:
            print("invalid chooice")

        con = int(input("Press 0 to stop\n"))
        if(con==0):
            flag = 0

main()