num =int(input("Enter No"))
n1 = 0
n2 = 1
for i in range (2,num+1) :
    n3 = n1+n2
    n1=n2
    n2=n3
    print (n3)