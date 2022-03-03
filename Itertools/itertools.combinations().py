from itertools import combinations
word,n= input().split(" ")

for i in range(1,int(n)+1):
    for j in combinations(sorted(word),int(i)):
        print("".join(j))
