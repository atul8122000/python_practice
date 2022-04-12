######################### 12 Remove all duplicates from a given string in Python##########################
A = 'aabbccddeeffgghiijjkkll'
S = " ".join(A ).split(" ")
S = list(set(S))
print(S)