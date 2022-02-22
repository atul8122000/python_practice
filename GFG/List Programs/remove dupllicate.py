num = [1,1,1,2,4,6,3,7,34,78,32,7,23]
# Method 1
# using set     
num= list(set(num))
print(num)       


# Method 2
# using for loop
l=[]
for i in num:
    if i not in l:
        l.append(i) 
