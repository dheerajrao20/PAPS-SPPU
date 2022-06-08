# ASSIGNMENT 03
num  = []
n = int(input("Enter the value of n :\n"))
for i in range(n):
    print("enter", i+1, "number")
    ele = float(input())
    num.append(ele)
print("maximum of numbers is: ",max(num))
print("minimum of numbers is: ",min(num))
print("sum of numbers is: ",sum(num))
print("Avarage of numbers is: ",(sum(num)/n))

