user = input("Enter no:")
user = user.split(",")
user = [int(i) for i in user]
rm = [2,5]


# user = [i for i in user if i not in rm ]
# print(user) 


for i in rm:
    user.remove(i)
print(user)