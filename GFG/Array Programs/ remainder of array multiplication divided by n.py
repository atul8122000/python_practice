n = int(input("Enter No to divide: "))
arr = [12, 10, 5, 6, 52, 36]
multi = 1
for i in arr:
    multi =multi*i
    div = multi % n
print(div)