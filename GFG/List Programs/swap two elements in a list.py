'''List = [3,2,1,4]
List[0],List[2] =List[2],List[0]
print(List)
'''
def swap_no(user,position1,position2):
    user = user.split(",")
    user[position1],user[position2] = user[position2],user[position1]
    user = [int(i) for i in user]
    return user
user = input("Enter no:")
position1 = int(input(""))
position2 = int(input(""))
print(swap_no(user,position1,position2))