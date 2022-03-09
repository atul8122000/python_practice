######################### 14 Maximum frequency character in String##########################
from collections import Counter
a = ' GeeksforGeeks '
c =Counter(a)
m = max(c, key = c.get) 
print(m)