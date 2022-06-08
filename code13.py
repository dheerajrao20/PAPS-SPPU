#ASSIGNMENT 16

def fileop(ch):
    with open("test.txt", "r") as f1:
        contents = f1.read()
        if ch== 'a':
            contents = contents.replace('.', ',')
        elif ch== 'b':
            contents = contents.upper()
        elif ch== 'c':
            contents = contents.lower()

    with open("output.txt", "w") as f2:
        out = f2.write(contents)
    with open("output.txt", "r") as f3:
        cout = f3.read()
        print(cout)

ch = ''
while ch in 'abc':
    ch = input("Enter a to replace . by ,\nEnter b to uppercase\nEnter c to lowercase\n")
    if ch in 'abc':
        fileop(ch)
    else:
        print("Invalid operation")





