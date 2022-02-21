#########################################
########### Perfect Number ##############
#########################################
num = int(input("ENTER NO: "))
sum = 0
for i in range (1,num):
    if num % i == 0:
        sum= sum +i
if sum == num:
    print(num,"is Perfect No.")
else:
    print(num,"is not Perfect No")