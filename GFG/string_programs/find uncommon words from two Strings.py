uc =""
a = "Geeks for Geeks" 
a = a.split()
b = "Learning from Geeks for Geeks"
b = b.split()
for i in a:
    if i not in b:
        uc=uc+" "+i
    for j in b:
        if j not in a:
            uc = uc+" "+j
print(uc)
