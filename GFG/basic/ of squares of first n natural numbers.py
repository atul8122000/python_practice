num =int(input("Enter No"))
# formula
# sum =(num * (num + 1) * (2 * num + 1)) // 6
temp = num
sum =0
for i in range (1,num+1):
    sum = sum +(i*i)
print(sum)
