P = int(input("Enter Ammount: "))
R = float(input("Enter Rate of interest: "))
t = float(input("Enter Time: "))

A = P * (pow((1 + R / 100), t))
CI = A-P
print("compund Interest :" ,CI) 