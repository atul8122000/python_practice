num = int(input("Enter any Number"))

if num>1:
    for i in range(2,num):
        if num % i == 0:
         print (num,"is a Not prime Number")
         break
    else:
         print (num, "is a prime number")