######################### 13 Least Frequent Character in String##########################
from collections import Counter
a = ' GeeksforGeeks '
c =Counter(a)
m = min(c, key = c.get) 
print(m)