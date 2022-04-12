######################### 11  Count the Number of matching characters in a pair of string  ##########################
s=0
string1 = 'asdfghjkl'
string2 = 'qazolpwsxedcrfvtgbyhnujmik'
for i in string1:
    if i in string2:  
        s =s +string1.count(i)
        print(i, end=",")
        # print(' = ',string1.count(i))
print('total = ',s) 