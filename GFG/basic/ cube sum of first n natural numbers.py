num =int(input("Enter No"))
## formula
# x=(n * (n + 1)  / 2)
# x = (x*x)
temp = num
sum =0
for i in range (1,num+1):
    sum = sum +(i*i*i)
print(sum)
