# def convertRec(no):  
#     if(no==0): 
#        return 0
#     digit=no%10
#     if(digit==0): 
#         digit=5 
#     return int(convertRec(no//10))*10+digit 
# no=int(input("Enter the integer:"))
# print("Converted integer:",convertRec(no))
n = int(input("Enter no : "))
n = str(n)
num = n.replace('0', '1')
num = int(num)
print(num)