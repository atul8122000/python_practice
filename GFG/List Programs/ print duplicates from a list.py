List = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
duplicates =[]
for i in List:
    if i in i:
        duplicates.append(i)
print(duplicates)