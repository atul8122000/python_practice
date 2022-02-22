num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l= []
for i in num:
    if i>0:
        for j in range(2,i):
            if i%j== 0:
                break
        else:
            l.append(i)
print(l)