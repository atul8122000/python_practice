print("Enter MARKS")
a=int(input("ENGLISH: "))
b=int(input("HINDI: "))
c=int(input("SO.SCIENCE: "))
d=int(input("SCIENCE: "))
e=int(input("MATHS: "))
if (a>33 and b>33 and c>33 and d>33 and e>33):
  total = a+b+c+d+e
  print ("Total=" ,total)
  per= total/5
if per>90:
     print("Grade A")
elif per>80:
    print("Grade B")
elif per>70:
    print("Grade C")
else:
    print("Grade D")

