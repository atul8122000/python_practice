#######################################
# Prime_NO1_to_100
#######################################
for i in range(1,100):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)