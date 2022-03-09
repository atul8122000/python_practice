num = int(input("Enter any No: "))
temp=num
sum=0
for i in range (1, num+1):
    rem = temp %10
    sum = sum +rem**3
    temp = temp //10
if sum ==num:
    print("True")
else:
    print("False")

