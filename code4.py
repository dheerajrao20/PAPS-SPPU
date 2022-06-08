#ASSIGNMENT 04

nums = []
for i in range(5):
    print("enter", i+1, "subject score")
    ele = int(input())
    if(ele >100 and ele<0):
        print("Invalid marks")
        break
    elif(ele<40):
        break
    nums.append(ele)
total = sum(nums)/5
if (total > 75):
    print("Distinct with total marks : ", total)
elif (total >= 60 and total < 75):
    print("First Division with total marks : ", total)
elif (total >= 50 and total < 60):
    print("second divsion with total marks : ", total)
elif (total >= 40 and total < 50):
    print("third division with total marks : ", total)
else:
    print("Fail")

