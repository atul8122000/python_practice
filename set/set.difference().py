name1 = input()
roll1 =input().split()
s1 = set(roll1)

name2 = input()
roll2 =input().split()
s2 = set(roll2)

dif = s1.difference(s2)
print(len(dif))
