######################### 10 accept the strings which contains all vowels  ##########################
a='ateiuou'.lower()
t= ['a','e','i','o','u']
if a:
    for i in a:
        if i not in t:
            print(i,"Not accepted")
            break
    else:
        print("accepted")
####  method 2
a='aeiwouy'.lower()
t= ['a','e','i','o','u']
for i in a:
    if i in t:
        print(i,"accepted")
    else:
        print(i,"Not accepted")