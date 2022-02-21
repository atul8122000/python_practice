#########################################
########### harshad_Number ##############
#########################################
num = int(input("Give a value: "))
rem=sum=0
n = num
while num>0:
    rem = n % 10
    sum = sum + rem
    num = num // 10
if n % sum == 0 :
    print(n, "is harshad No")
else:
    print(n,"is not harshad No")