start = int(input("Enter Starting Range for No: "))
end = int(input("Enter Ending Point for No: "))
l =[]
for i in range (start, end+1):
    if i % 2==0:
        l.append(i)
print(l)