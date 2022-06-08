

n = input("Enter a number: ")
sum = 0
for i in range(len(n)):
    sum = sum + int(n[i])**len(n)
if(sum == int(n)):
    print("yes")
else:
    print("no")


