num = int(input("Enter Range for Prime No: "))

for i in range(2, num):
    if num% i== 0:
        print("Not Prime NO")
        break
    else:
        print("Prime NO")