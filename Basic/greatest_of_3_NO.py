a = int(input("Enter First NO. "))
b = int(input("Enter First NO. "))
c = int(input("Enter First NO. "))

if a<b and c<b:
    print(b," is greater than " ,a,"and", c)
elif a<c and b<c:
    print(c, " is greater than " , b,"and",a)
else:
    print (a, " is greater than " , c,"and",b)