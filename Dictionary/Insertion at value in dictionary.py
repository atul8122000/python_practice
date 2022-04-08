a = {'a':1, 'b':2}
b = {'c':3, 'd':4}
c = list(a.items())+list(b.items())
print(c)