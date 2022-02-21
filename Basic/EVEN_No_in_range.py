i = int(input("Give Range for EVEN NO: "))
num = int(input("Give Range for EVEN NO: "))
### using for loop
# for p in range(i,num+1):
#     if p%2==0:
#         print(p)
### using while Loop
sum =0
while num>=i:
    if i%2==0:
        print(i)
        sum = sum+i
    i=i+1
    
print("sum of all even no is" ,sum)