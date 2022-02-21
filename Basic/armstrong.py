num =int(input("Enter any number : "))
sum =0
temp = num

while temp>0:
    rem = temp %10
    sum += rem **3
    temp = temp // 10
if sum == num:
    print (num,"armstrong No")
else:
   print (num,"Not armstrong No")
