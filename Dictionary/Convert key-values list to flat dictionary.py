A = {'month' : [1, 2, 3],'name' : ['Jan', 'Feb', 'March']}
# res = dict(zip(A['month'], A['name']))
Z = zip(A['month'],A['name'])
D = dict(Z)
print(D)