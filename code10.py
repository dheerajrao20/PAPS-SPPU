# Assignment 14

def convert(s):
    decimal = 0
    rno = s[ : : -1]
    for i in range(len(rno)):
        decimal = decimal + int(rno[i])*(2**i)
    print(decimal)

def main():
    s = input("enter the binary number")
    convert(s)
main()