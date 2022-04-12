######################### 6 Words Frequency in String Shorthands ##########################
from collections import Counter
A = 'ram ram RAM KrisHna KRISHNA'

res = Counter(A.split())
print(res)