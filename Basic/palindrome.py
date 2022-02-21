num =int(input("Enter Any No. "))
temp = num
reverse = 0
while num>0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
if reverse == temp:
    print (temp, "is a pelindrome No")
else:
    print (temp, "is not pelindrome No")