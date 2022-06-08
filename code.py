# ASSIGNMENT 01

Basic_pay = int(input("Enter the value of Basic Pay "))
Days=int(input("Enter the no. of days"))
wages=Basic_pay/30
Basic_pay=wages*Days
hra = Basic_pay*0.1
ta = Basic_pay*0.05
Sal = Basic_pay + hra + ta
tax = Sal*0.02
net_sal = Sal - tax
print("Basic pay\n", Basic_pay , "HRA \n", hra , "TA \n ",ta, "Gross Salary \n",Sal, "Tax\n",tax,"Net Salary \n", net_sal   )