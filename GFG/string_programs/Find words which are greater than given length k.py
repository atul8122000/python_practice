######################### 17 Find words which are greater than given length k##########################

s = "hello geeks for geeks is computer science portal" 
a = s.split()
k = 4
for i in a:
    if len(i)>=k:
        print(i)