num1 = int(input("Enter Starting NO : "))
num2 = int(input("Enter Ending NO : "))
for i in range(num1, num2+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)