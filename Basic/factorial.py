############ WITH FUNCTION ##################
# import math as mm
# num = int(input("Enter a value : "))

# fact= mm.factorial(num)
# print ("Factorial of",num ,"is",fact) 

############ WITHOUT FUNCTION ##################

num = int(input("Enter a value : "))
fac =1
for i in range (1,num+1):
    fac = fac * i
print ("Factorial of",num ,"is",fac) 