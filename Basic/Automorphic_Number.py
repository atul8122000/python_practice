#########################################
########### Automorphic_Number ##########
#########################################
num = int(input("Give a value: "))
square = num**2
print (num,"*",num,"=", square)
last= square%10
if num == last:
    print(num,"is Automorphic Number")
else:
    print(num, "is not Automorphic Number")