#########################################
########### Friendly_Pair ###############
#########################################
num = int(input("ENTER NO 1: "))
num2 = int(input("ENTER NO 2: "))
sum = 0
sum2 = 0
for i in range (1,num):
    if num % i == 0:
        sum = sum +i
for i in range (1,num2):
    if num2 % i == 0:
        sum2 = sum2 +i
if num == sum and sum2 == sum2:
    print(True)
else:
    print(False)