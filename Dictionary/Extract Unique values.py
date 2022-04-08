test_dict = {'a' : [5, 6, 7, 8],'t' : [10, 11, 7, 5],'u' : [6, 12, 10, 8],'l' : [1, 2, 5]}
l=[]
for i in test_dict.values():
    res = list(sorted(set(i)))
    for j in res:
        l.append(j)
print(list(set(l)))