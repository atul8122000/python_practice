from operator import itemgetter
lis = [{ "name" : "Nandini", "age" : 20},{ "name" : "Manjeet", "age" : 20 },{ "name" : "Nikhil" , "age" : 19 }]
newlist = sorted(lis, key=itemgetter('name','age')) 
print(newlist)