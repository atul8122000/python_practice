#########################################
#Abundant number is a number whose sum of the divisors of the number is greater than the number
#########################################
num = int(input("Give a value: "))
sum = 0
n= num
for i in range (1,num):
    if n % i == 0:
        print(i)
        sum = sum +i
if sum> n:
    print(n,"is Abundant Number")
else:
    print(n,"is Not Abundant Number")