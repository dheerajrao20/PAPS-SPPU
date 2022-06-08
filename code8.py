#ASIGNMENT 05

def check(n):
    sum = 0
    for i in range(len(n)):
        sum = sum + int(n[i]) ** len(n)
    if (sum == int(n)):
        return True
    else:
        return False

n = input("Enter a number: ")
print(check(n))
