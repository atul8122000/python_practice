'''
 :- Taking input list from user
 :- split by ","
 :- Interchange by indexing
 :- convert str to int
'''
user = input("Enter no:")
user = user.split(",")
user[0],user[-1] = user[-1],user[0]
user = [int(i) for i in user]
print (user)
