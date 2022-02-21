#######################################
########### aliquot_sum #########
#######################################
num = int(input("Enter a Number: "))
 
sum = 0
for i in range (1, num):
    if num %i ==0:
        sum = sum + i
print(sum)
