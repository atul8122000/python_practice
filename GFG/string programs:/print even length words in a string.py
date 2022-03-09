######################### 8 print even length words in a string  ##########################
a = "This is a python language"
s =a.split(" ")

for i in s:
    b = len(i)
    if b %2==0:
        print (i)
