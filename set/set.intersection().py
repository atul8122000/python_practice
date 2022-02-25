name1 = input()
roll1 =input().split()
s1 = set(roll1)

name2 = input()
roll2 =input().split()
s2 = set(roll2)

add = s1.intersection(s2)
print(len(add))
