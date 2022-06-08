#ASSIGNMENT 12 (list)

n = int(input("Enter the value of n :\n"))
print("Now Enter the numbers :\n")
even = []
odd = []
for i in range(n):
    ele = int(input())
    if (ele%2==0):
        even.append(ele)
    else:
        odd.append(ele)
print(even)
print(odd)


