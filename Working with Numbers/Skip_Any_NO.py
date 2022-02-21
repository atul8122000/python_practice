#######################################
########### Skip_Any_NO #########
####################################### 
num = int(input("Enter Starting Range: "))
num2 = int(input("Enter Ending Range: "))
nlist =[]
for i in range(num,num2+1):
    if i%10 ==7:
        continue
    i= str(i)
    nlist.append(i)
nlist= "|".join(nlist)
print (nlist)