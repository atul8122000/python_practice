######################### 5 Check if a Substring is Present in a Given String ##########################
A = 'aTUL yadav'
a = A.lower().replace(" ","")
f= 'a'
for i in range (len(a)):
    if f not in a:
        print(" Not Found")
        break    
else:
    print(f,"Present in ",A)