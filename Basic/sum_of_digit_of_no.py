num =int(input("Enter Any No. "))
sum =0
for i in range (0,num):
    rem = num % 10
    sum = sum + rem
    num =num // 10
print(sum)
